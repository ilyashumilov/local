from django.db import models
from django.contrib.auth.models import User
# python manage.py migrate --run-syncdb
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.TextField(max_length = 50)
    def __str__(self):
        return str(self.country) + ': ' + str(self.user.username)

class existing(models.Model):
    number = models.TextField(max_length = 50)

class Empresa(models.Model):
    name =  models.TextField(max_length = 50)
    trader =  models.TextField(max_length = 50)
    def __str__(self):
        return str(self.name)

class Materials(models.Model):
    name = models.TextField(max_length = 50)
    def __str__(self):
        return str(self.name)

class Ports(models.Model):
    port =  models.TextField(max_length = 50)
    country =  models.TextField(max_length = 50)

    def __str__(self):
        return str(self.port)

class SO(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    number =  models.TextField(max_length = 50)
    client = models.ForeignKey(Empresa,on_delete = models.CASCADE)
    destination = models.ForeignKey(Ports, on_delete=models.CASCADE)
    date =  models.TextField(max_length = 50)
    material =  models.TextField(max_length = 50)
    cntr = models.IntegerField()
    Tons = models.DecimalField(max_digits=10, decimal_places=2)
    min = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=20)
    comment = models.TextField(max_length = 1000)
    cpt = models.CharField(max_length = 10)

    stat = models.BooleanField(default=False)

    def __str__(self):
        return str(self.number)

class PO(models.Model):
    so = models.ForeignKey(SO, on_delete= models.CASCADE)
    Proveedor = models.ForeignKey(Empresa, on_delete= models.CASCADE)
    Origin = models.ForeignKey(Ports, on_delete=models.CASCADE)
    date = models.CharField(max_length = 30)
    material = models.ForeignKey(Materials, on_delete=models.CASCADE)
    number = models.TextField(max_length = 50)
    cntr = models.IntegerField()
    Tons = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=20)
    spt = models.CharField(max_length = 10)

    def __str__(self):
        return str(self.number)

class Readiness(models.Model):
    po = models.ForeignKey(PO, on_delete= models.CASCADE)
    Proveedor = models.TextField(max_length = 200)
    Origin = models.TextField(max_length = 200)
    date = models.TextField(max_length = 200)
    number = models.TextField(max_length = 200)
    cntr = models.IntegerField()
    Tons = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(max_length = 200)

    def __str__(self):
        return str(self.po.number)


class Shipment(models.Model):
    po = models.ForeignKey(PO, on_delete = models.CASCADE)
    number = models.TextField(max_length = 50)
    forwarder = models.TextField(max_length = 50)
    carrier = models.TextField(max_length = 50)
    cntr = models.IntegerField()
    bknumber = models.TextField(max_length = 50)
    ETD = models.TextField(max_length=200)
    ETA = models.TextField(max_length=200)
    margin = models.DecimalField(max_digits=10, decimal_places=2)
    marginEUR = models.CharField(max_length=10)
    BK = models.BooleanField(default=False)
    SI = models.BooleanField(default=False)
    Magic = models.BooleanField(default=False)

    shipinstr = models.TextField(max_length = 50)
    equip = models.TextField(max_length=200)
    Truck = models.BooleanField(default=False)
    comment = models.TextField(max_length=200)
    link = models.TextField(max_length=200)

    def numero(self):
        return float(self.marginEUR)

    def __str__(self):
        return str(self.number)

class Monthly(models.Model):
    po = models.TextField(max_length = 300)
    sodate = models.TextField(max_length = 50)
    podate = models.TextField(max_length = 50)

    Supplier =  models.TextField(max_length = 50)
    client =  models.TextField(max_length = 50)

    origincity =  models.TextField(max_length = 50)
    origincountry =  models.TextField(max_length = 50)

    destinationcity =  models.TextField(max_length = 50)
    destinationcountry =  models.TextField(max_length = 50)
    line = models.TextField(max_length=50)
    forwarder = models.TextField(max_length=50)
    number = models.TextField(max_length = 50)
    bknumber = models.TextField(max_length = 50)
    material = models.TextField(max_length = 50)
    cntr = models.CharField(max_length=20)
    Tons = models.DecimalField(max_digits=10, decimal_places=2)
    Tonsact = models.DecimalField(max_digits=10, decimal_places=2)
    min = models.CharField(max_length=20)

    transaction = models.TextField(max_length = 50)
    margin = models.DecimalField(max_digits=10, decimal_places=2)
    marginEUR = models.TextField(max_length = 50)

    ETD = models.TextField(max_length = 50)
    ETA = models.TextField(max_length = 50)

    shipinstr = models.TextField(max_length = 50)

    Truck = models.BooleanField(default = False)
    equip = models.CharField(max_length=30)

    link = models.TextField(max_length=200)

    def numero(self):
        return float(self.marginEUR)

    def __str__(self):
        return str(self.material)

class upd(models.Model):
    index = models.CharField(max_length=20)
    st = models.BooleanField(default = False)

class back(models.Model):
    file = models.TextField(max_length = 50)


class MonthlyCosts(models.Model):
    monthly = models.ForeignKey(Monthly, on_delete=models.CASCADE)
    name =  models.TextField(max_length = 50)
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length = 20)

class invoices(models.Model):
    number = models.TextField(max_length = 50)

class Containers(models.Model):
    us = models.ForeignKey(User, on_delete = models.CASCADE)

    shipment = models.ForeignKey(Shipment, on_delete = models.CASCADE)
    number = models.TextField(max_length = 50)
    seal = models.TextField(max_length = 50)
    bales = models.IntegerField()
    gross = models.DecimalField(max_digits=10, decimal_places=2)
    tara = models.DecimalField(max_digits=10, decimal_places=2)
    vgm = models.DecimalField(max_digits=10, decimal_places=2)



    def __str__(self):
        return str(self.shipment)

class counter(models.Model):
    name = models.TextField(max_length = 50)
    volume = models.IntegerField()

    def __str__(self):
        return str(self.name)

class counterupd(models.Model):
    index = models.CharField(max_length=20)
    st = models.BooleanField(default = False)

class Claims(models.Model):
    Monthly = models.ForeignKey(Monthly, on_delete= models.CASCADE)
    date = models.CharField(max_length = 20)
    bl = models.TextField(max_length = 50)
    reason = models.TextField(max_length = 50)
    comment = models.TextField(max_length = 50)
    currency = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    photos = models.TextField(max_length = 1000)

    forwarder = models.TextField(max_length = 1000)
    carrier = models.TextField(max_length = 1000)

    picCust = models.BooleanField(default=False)
    picVipa = models.BooleanField(default=False)
    Sent = models.BooleanField(default=False)
    settlement = models.BooleanField(default=False)

    cntrs = models.IntegerField()
    tons = models.DecimalField(max_digits=10, decimal_places=2)


    cn = models.BooleanField(default=False)

    cn_currency = models.CharField(max_length=20)
    cn_amount = models.DecimalField(max_digits=10, decimal_places=2)

    dn = models.BooleanField(default=False)

    dn_currency = models.CharField(max_length=20)
    dn_amount = models.DecimalField(max_digits=10, decimal_places=2)

    settlement_date = models.CharField(max_length=20)

    profit = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    def number(self):
        return float(self.profit)

    def __str__(self):
        return str(self.Monthly)

class ClaimsUkr(models.Model):
    monthly = models.ForeignKey(Monthly, on_delete = models.CASCADE)
    humidper = models.DecimalField(max_digits=10, decimal_places=2)
    humidton = models.DecimalField(max_digits=10, decimal_places=2)
    impur = models.DecimalField(max_digits=10, decimal_places=2)
    docs = models.BooleanField(default=False)
    claimsupp = models.DecimalField(max_digits=10, decimal_places=2)
    set = models.CharField(max_length=20)

class Freight(models.Model):
    forwarder = models.TextField(max_length = 50)
    Line = models.TextField(max_length = 50)
    POL = models.TextField(max_length = 50)
    POD = models.TextField(max_length = 50)
    terms = models.CharField(max_length = 30)
    rate = models.CharField(max_length = 30)
    currencyrate = models.CharField(max_length = 30)
    period = models.CharField(max_length = 30)
    contract = models.TextField(max_length = 50)
    additional = models.CharField(max_length = 30)
    currencyadd = models.CharField(max_length = 30)

    margin = models.CharField(max_length = 30)

class Costs(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete = models.CASCADE)
    name =  models.TextField(max_length = 50)
    volume = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.CharField(max_length=20)

class FinCosts(models.Model):
    monthly = models.ForeignKey(Monthly, on_delete=models.CASCADE)
    name =  models.TextField(max_length = 50)
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=20)

class Buffer(models.Model):
    number = models.TextField(max_length = 50)
    proveedor = models.TextField(max_length = 50)
    Origin = models.CharField(max_length = 20)
    carrier = models.TextField(max_length = 50)
    cntr = models.IntegerField()
    bknumber = models.TextField(max_length = 50)
    ETD = models.CharField(max_length=10)
    ETA = models.CharField(max_length=10)
    comment = models.TextField(max_length = 50)

class ShipmentRate(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    rate = models.CharField(max_length=10)

class MonthlyRate(models.Model):
    monthly = models.ForeignKey(Monthly, on_delete=models.CASCADE)
    rate = models.CharField(max_length=10)

class track(models.Model):
    bknumber = models.TextField(max_length=50)
    number = models.TextField(max_length=50)
    Supplier = models.TextField(max_length = 50)
    origincountry = models.TextField(max_length = 50)
    material = models.TextField(max_length = 50)

    payment_status = models.BooleanField(default=False)
    registered = models.BooleanField(default=False)
    comment = models.TextField(max_length = 100)

    def __str__(self):
        return str(self.bknumber)
