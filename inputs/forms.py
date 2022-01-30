from django import forms
from .models import *

class filterform(forms.Form):
    country = forms.CharField(label=False, widget=forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Country', 'autocomplete': "off"}))

class uploadform(forms.Form):
    file = forms.FileField(label=False)

class soindex(forms.Form):
    cpt = forms.CharField(label=False, widget=forms.TextInput(attrs={'class': 'cpt', 'id': 'search', 'placeholder': 'Cust. Payment Terms', 'autocomplete': "off"}))
    client = forms.CharField(label=False, widget=forms.TextInput(attrs={'class':'client','id': 'search1', 'placeholder': 'Client','autocomplete':"off"}))
    destination = forms.CharField(label=False, widget=forms.TextInput(attrs={'class':'destination','id': 'search2', 'placeholder': 'Destination', 'autocomplete': "off"}))
    date = forms.CharField(label=False, widget = forms.TextInput(attrs={'type':"date",'class': 'date','placeholder': 'Select a date'}))
    number = forms.CharField(label=False, widget=forms.TextInput(attrs={'class':'number','placeholder': 'Number', 'autocomplete': "off"}))
    material = forms.CharField(label=False, widget=forms.TextInput(attrs={'class':'material','id': 'search3','placeholder': 'Material','autocomplete': "off"}))
    cntr = forms.IntegerField(label=False, widget=forms.TextInput(attrs={'class':'cntr','placeholder': 'Cntr', 'autocomplete': "off"}))
    Tons = forms.DecimalField(label=False, widget=forms.TextInput(attrs={'class':'Tons','placeholder': 'Tons', 'autocomplete': "off"}))
    min = forms.DecimalField(label=False, widget=forms.TextInput(attrs={'class':'min','placeholder': 'Min Payload', 'autocomplete': "off"}))
    cost = forms.CharField(label=False, widget=forms.TextInput(attrs={'class':'cost','placeholder': 'Price', 'autocomplete': "off"}))
    currency = forms.CharField(label=False, widget=forms.Select(attrs={'class': 'currency', 'id': 'currency'},choices=(('USD', 'USD'), ('EUR', 'EUR'),)))
    comment = forms.CharField(label=False, widget=forms.TextInput(attrs={'class':'comment','placeholder': 'Comment', 'autocomplete': "off"}))

class bfr(forms.ModelForm):
    class Meta:
        model = Buffer
        fields = ['number','Origin','carrier', 'cntr','bknumber', 'ETD','ETA','comment','proveedor']

        labels = {
            'number': False,
            'Origin': False,
            'carrier': False,
            'cntr': False,
            'bknumber': False,
            'ETD': False,
            'ETA': False,
            'comment': False,
            'proveedor':False
        }
        widgets = {
            'number': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Number', 'autocomplete': "off"}),
            'Origin': forms.TextInput(attrs={'class': 'one', 'id': 'price', 'placeholder': 'Origin', 'autocomplete': "off"}),
            'carrier': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Carrier', 'autocomplete': "off"}),
            'cntr': forms.TextInput(attrs={'class': 'one', 'id': 'min', 'placeholder': 'cntr', 'autocomplete': "off"}),
            'bknumber': forms.TextInput(attrs={'class': 'one', 'id': 'price', 'placeholder': 'BK', 'autocomplete': "off"}),
            'ETD': forms.TextInput(attrs={'class': 'one', 'id': 'price', 'placeholder': 'ETD', 'autocomplete': "off"}),
            'ETA': forms.TextInput(attrs={'class': 'one', 'id': 'price', 'placeholder': 'ETA', 'autocomplete': "off"}),
            'comment': forms.TextInput(attrs={'class': 'one', 'id': 'comment', 'placeholder': 'Comment', 'autocomplete': "off"}),
            'proveedor': forms.TextInput(attrs={'class': 'one', 'id': 'comment', 'placeholder': 'Supplier', 'autocomplete': "off"}),
        }

class followupform(forms.ModelForm):
    class Meta:
        model = track
        fields = ['payment_status','registered','comment']

        labels = {
            'payment_status':'Payment status',
            'registered': 'Registered'
        }
        widgets = {
            'payment_status': forms.CheckboxInput(),
            'registered': forms.CheckboxInput(),
            'comment': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Comment', 'autocomplete': "off"}),
        }

class soform(forms.ModelForm):
    class Meta:
        model = SO
        fields = ['date','cntr','Tons', 'min','cost', 'currency','comment']

        labels = {
            'date': 'Date:',
            'cntr': 'Cntrs:',
            'currency': False,
            'Tons': 'Tons:',
            'min': 'Min:',
            'cost': 'Price:',
            'comment': 'Comment:'
        }
        widgets = {
            'date': forms.TextInput(attrs={'class': 'one', 'id': 'search1', 'placeholder': 'Date', 'autocomplete': "off"}),
            'cntr': forms.NumberInput(attrs={'class': 'one', 'id': 'cntr', 'placeholder': 'Cntr', 'autocomplete': "off"}),
            'Tons': forms.TextInput(attrs={'class': 'one', 'id': 'search1', 'placeholder': 'Tons', 'autocomplete': "off"}),
            'min': forms.TextInput(attrs={'class': 'one', 'id': 'min', 'placeholder': 'Min', 'autocomplete': "off"}),
            'cost': forms.TextInput(attrs={'class': 'one', 'id': 'price', 'placeholder': 'Cost', 'autocomplete': "off"}),
            'currency': forms.Select(attrs={'class': 'one', 'id': 'currency'}, choices=(('USD', 'USD'), ('EUR', 'EUR'),)),
            'comment': forms.TextInput(attrs={'class': 'one', 'id': 'comment', 'placeholder': 'Comment', 'autocomplete': "off"}),
        }


class poform (forms.ModelForm):
    class Meta:
        model = PO
        fields = ['date','number','cntr','Tons', 'price','currency',]
        labels = {
            'date': "Date:",
            'number': "Number:",
            'cntr': "Cntrs:",
            'Tons': "Tons:",
            'price': "Price:",
            'currency': False
        }
        widgets = {
            'date': forms.TextInput(attrs={'class':'one','id': 'date', 'placeholder': 'Date','autocomplete':"off"}),
            'number': forms.TextInput(attrs={'class': 'one', 'id': 'number', 'placeholder': 'Number', 'autocomplete': "off"}),
            'cntr': forms.TextInput(attrs={'class': 'one', 'id': 'cntr', 'placeholder': 'Cntr', 'autocomplete': "off"}),
            'Tons': forms.TextInput(attrs={'class': 'one', 'id': 'tons', 'placeholder': 'Tons', 'autocomplete': "off"}),
            'price': forms.TextInput(attrs={'class': 'one', 'id': 'price', 'placeholder': 'Price', 'autocomplete': "off"}),
            'currency': forms.Select(attrs={'class': 'currency', 'id': 'e'}, choices=(('USD', 'USD'), ('EUR', 'EUR'),)),
        }

class claimform(forms.ModelForm):
    class Meta:
        model = Claims
        fields = ['date','bl','reason','comment','currency', 'amount','photos','picCust','picVipa','Sent',\
                  'settlement','cn','cn_currency','cn_amount','dn', 'dn_currency','dn_amount','settlement_date',\
                  'rate','cntrs','tons']

        labels = {
            'date': False,
            'bl': False,
            'reason': False,
            'comment': False,
            'currency': False,
            'amount': False,
            'photos': False,
            # 'picCust': False,
            # 'picVipa': False,
            # 'Sent': False,
            # 'settlement': False,
            'cn': 'CN',
            'cn_currency': False,
            'cn_amount': False,
            'dn': 'DN',
            'dn_currency': False,
            'dn_amount': False,
            'settlement_date': False,
            'rate': False,
            'cntrs':False,
            'tons':False
        }

        widgets = {
            'date': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Date', 'autocomplete': "off"}),
            'bl': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'BL', 'autocomplete': "off"}),
            'reason': forms.Select(attrs={'class': 'one', 'id': 'reason'},choices=(('Low Quality', 'Low Quality'), ('Wrong Grade', 'Wrong Grade'),\
                    ('Underweight', 'Underweight'),('Humidity', 'Humidity'),('Doc delay', 'Doc delay'),('Humidity + diff weight', 'Humidity + diff weight'),('Diff weigth', 'Diff weigth'),\
                    ('Diff material', 'Diff material'),('TMP Material', 'TMP Material'),('Extra Costs', 'Extra Costs'),('Proh. Material', 'Proh. Material'),('Logistics Costs', 'Logistics Costs'),)),
            'comment': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Comment', 'autocomplete': "off"}),
            'currency':  forms.Select(attrs={'class': 'one', 'id': 'search'},choices=(('USD', 'USD'), ('EUR', 'EUR'),)),
            'amount': forms.TextInput(attrs={'class': 'amount', 'id': 'search', 'placeholder': 'Amount', 'autocomplete': "off"}),
            'photos': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Photos', 'autocomplete': "off"}),
            'picCust': forms.CheckboxInput(),
            'picVipa': forms.CheckboxInput(),
            'Sent': forms.CheckboxInput(),
            'settlement': forms.CheckboxInput(),
            'cn': forms.CheckboxInput(),
            'cn_currency': forms.Select(attrs={'class': 'one', 'id': 'search'},choices=(('USD', 'USD'), ('EUR', 'EUR'),)),
            'cn_amount': forms.TextInput(attrs={'class': 'amount', 'id': 'search', 'placeholder': 'CN Amount', 'autocomplete': "off"}),
            'dn': forms.CheckboxInput(),
            'dn_currency':  forms.Select(attrs={'class': 'one', 'id': 'search'},choices=(('USD', 'USD'), ('EUR', 'EUR'),)),
            'dn_amount': forms.TextInput(attrs={'class': 'amount', 'id': 'search', 'placeholder': 'DN Amount', 'autocomplete': "off"}),
            'settlement_date': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Settlement Date', 'autocomplete': "off"}),
            'rate': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Rate', 'autocomplete': "off"}),
            'cntrs': forms.TextInput(attrs={'class': 'one', 'id': 'cntrs', 'placeholder': 'Cntrs', 'autocomplete': "off"}),
            'tons': forms.TextInput(attrs={'class': 'one', 'id': 'tons', 'placeholder': 'Tons', 'autocomplete': "off"})
        }

class ukrclaim(forms.ModelForm):
    class Meta:
        model = ClaimsUkr
        fields = ['humidper','humidton','impur', 'docs','claimsupp', 'set']

        labels = {
            'humidper': "Humidity %:",
            'humidton': "Humidity Tons:",
            'impur': "Impurities:",
            'docs': "Docs sent:",
            'claimsupp': "Claim to supplier:",
            'set': "Date of settlement:"
        }
        widgets = {
            'humidper': forms.NumberInput(attrs={'class': 'one', 'id': 'humidper', 'placeholder': 'Humidity %:', 'autocomplete': "off"}),
            'humidton': forms.NumberInput(attrs={'class': 'one', 'id': 'humidton', 'placeholder': 'Humidity Tons', 'autocomplete': "off"}),
            'impur': forms.NumberInput(attrs={'class': 'one', 'id': 'impur', 'placeholder': 'Impurities', 'autocomplete': "off"}),
            'docs': forms.CheckboxInput(),
            'claimsupp': forms.TextInput(attrs={'class': 'one', 'id': 'Claim to supplier', 'placeholder': 'Claim to supplier', 'autocomplete': "off"}),
            'set': forms.TextInput(attrs={'class': 'one', 'id': 'set', 'placeholder': 'Date of settlement', 'autocomplete': "off"}),
        }


class readiness(forms.ModelForm):
    class Meta:
        model = Readiness
        fields = ['number','cntr','Tons', 'comment']

        labels = {
            'number': "Number",
            'cntr': "Cntrs",
            'Tons': "Tons",
            'comment': "Comment"
        }
        widgets = {
            'number': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Cntr', 'autocomplete': "off"}),
            'cntr': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Cntr', 'autocomplete': "off"}),
            'Tons': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Tons', 'autocomplete': "off"}),
            'comment': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Comment', 'autocomplete': "off"}),
        }

class splitform(forms.Form):
    current = forms.DecimalField(label=False, widget=forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Current', 'autocomplete': "off"}))
    cntr = forms.DecimalField(label=False, widget=forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Cntr', 'autocomplete': "off"}))

class moveform(forms.Form):
    newso = forms.CharField(label=False, widget=forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'New SO number', 'autocomplete': "off"}))

class index(forms.Form):
    Proveedor = forms.CharField(label=False, widget=forms.TextInput(attrs={'class':'proveedor','id': 'search1', 'placeholder': 'Supplier', 'autocomplete': "off"}))
    Origin = forms.CharField(label=False, widget=forms.TextInput(attrs={'class':'origin', 'id': 'search2','placeholder': 'Origin', 'autocomplete': "off"}))
    material = forms.CharField(label=False, widget=forms.TextInput(attrs={'class':'material','id': 'search3','placeholder': 'Material', 'autocomplete': "off"}))
    status = forms.CharField(label=False, widget=forms.TextInput(attrs={'class':'status','placeholder': 'Status', 'autocomplete': "off"}))
    date = forms.CharField(label=False, widget = forms.TextInput(attrs={'type':"date",'class': 'date','placeholder': 'Select a date'}))
    cntr = forms.IntegerField(label=False, widget=forms.TextInput(attrs={'class':'cntr','placeholder': 'Containers', 'autocomplete': "off"}))
    Tons = forms.DecimalField(label=False, widget=forms.TextInput(attrs={'class':'tons','placeholder': 'Tons', 'autocomplete': "off"}))
    price = forms.DecimalField(label=False, widget=forms.TextInput(attrs={'class':'price','placeholder': 'Price', 'autocomplete': "off"}))
    currency = forms.CharField(label=False, widget=forms.Select(attrs={'class': 'currency', 'id': 'currency'},choices=(('USD', 'USD'), ('EUR', 'EUR'),)))
    spt = forms.CharField(label=False, widget = forms.TextInput(attrs={'class': 'spt','placeholder': 'Sup. paym. terms', 'autocomplete': "off"}))

class shipmentforma(forms.ModelForm):
    class Meta:
        choises = (
            ('NOR', 'NOR'),
            ("40'HC", "40'HC"),
            ("40'DC", "40'DC"),
            ("Truck", "Truck"),
            ("Rail", "Rail"),
            ("45'", "45'"),
        )
        model = Shipment
        fields = ['number','bknumber','ETD','ETA','BK','SI','Magic','equip']
        labels = {
            'number': "Number",
            'bknumber': "BK",
            'ETD': "ETD",
            'ETA': "ETA",
            'equip': 'Equipment'
        }
        widgets = {
            'number': forms.TextInput(attrs={'class':'one','id': 'search', 'placeholder': 'Number','autocomplete':"off"}),
            'bknumber': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'BK', 'autocomplete': "off"}),

            'ETA': forms.TextInput(attrs={'type': "date", 'class': 'date', 'id': 'ETA', 'placeholder': 'ETA','autocomplete': "off"}),
            'ETD': forms.TextInput(attrs={'type': "date", 'class': 'date', 'id': 'ETD', 'placeholder': 'ETD','autocomplete': "off"}),

            'BK': forms.CheckboxInput(),
            'SI': forms.CheckboxInput(),
            'Magic': forms.CheckboxInput(),
            'equip': forms.Select(attrs={'class': 'currency', 'id': 'currency'}, choices=choises)
        }

class shipmentform(forms.ModelForm):
    class Meta:
        choises = (
            ('NOR', 'NOR'),
            ("40'HC", "40'HC"),
            ("40'DC", "40'DC"),
            ("Truck", "Truck"),
            ("Rail", "Rail"),
            ("45'", "45'"),
        )
        model = Shipment
        fields = ['number','bknumber','ETD','ETA','BK','SI','Magic','carrier','forwarder','shipinstr','equip','link','comment']
        labels = {
            'number': "Number",
            'bknumber': "BK",
            'ETD': "ETD",
            'ETA': "ETA",
            'carrier':'carrier',
            'SI': 'SI/CST',
            'forwarder': 'forwarder',
            'shipinstr':'SI number',
            'equip':'Equipment',
            'link':'Photo',
            'comment':'Comment'
        }
        widgets = {
            'number': forms.TextInput(attrs={'class':'one','id': 'search', 'placeholder': 'Number','autocomplete':"off"}),
            'bknumber': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'BK', 'autocomplete': "off"}),

            'ETA': forms.TextInput(attrs={'type': "date", 'class': 'date', 'id': 'ETA', 'placeholder': 'ETA','autocomplete': "off"}),
            'ETD': forms.TextInput(attrs={'type': "date", 'class': 'date', 'id': 'ETD', 'placeholder': 'ETD','autocomplete': "off"}),

            'BK': forms.CheckboxInput(),
            'SI': forms.CheckboxInput(),
            'Magic': forms.CheckboxInput(),
            'carrier': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Carrier', 'autocomplete': "off"}),
            'link': forms.TextInput(attrs={'class': 'one', 'id': 'link', 'placeholder': 'Link', 'autocomplete': "off"}),
            'shipinstr': forms.TextInput(attrs={'class': 'one', 'id': 'shipinstr', 'placeholder': 'SI number', 'autocomplete': "off"}),
            'forwarder': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Forwarder', 'autocomplete': "off"}),
            'equip': forms.Select(attrs={'class': 'currency', 'id': 'currency'},choices=choises),
            'comment': forms.TextInput(attrs={'class': 'one', 'id': 'comment', 'placeholder': 'Comment', 'autocomplete': "off"})

        }
class shipmentform1(forms.ModelForm):
    class Meta:
        choises = (
                      ('NOR', 'NOR'),
                      ("40'HC", "40'HC"),
                      ("40'DC", "40'DC"),
                      ("Truck", "Truck"),
                      ("Rail", "Rail"),
                      ("45'", "45'"),

        )

        model = Shipment
        fields = ['number','bknumber','ETD','ETA','BK','SI','Magic','carrier','forwarder','shipinstr','equip','link','comment']
        labels = {
            'number': "Number",
            'bknumber': "BK",
            'ETD': "ETD",
            'ETA': "ETA",
            'carrier':'carrier',
            'SI':'SI/CST',
            'forwarder': 'forwarder',
            'shipinstr':'SI number',
            'equip': 'Equipment',
            'link': 'Photo',
            'comment': 'Comment'
        }
        widgets = {
            'number': forms.TextInput(attrs={'class':'one','id': 'search', 'placeholder': 'Number','autocomplete':"off"}),
            'bknumber': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'BK', 'autocomplete': "off"}),
            'ETA': forms.TextInput(attrs={'class': 'one', 'id': 'ETA', 'placeholder': 'ETA', 'autocomplete': "off"}),
            'ETD': forms.TextInput(attrs={'class': 'one', 'id': 'ETD', 'placeholder': 'ETD', 'autocomplete': "off"}),
            'BK': forms.CheckboxInput(),
            'SI': forms.CheckboxInput(),
            'Magic': forms.CheckboxInput(),
            'carrier': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Carrier', 'autocomplete': "off"}),
            'shipinstr': forms.TextInput(attrs={'class': 'one', 'id': 'shipinstr', 'placeholder': 'SI number', 'autocomplete': "off"}),
            'forwarder': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Forwarder', 'autocomplete': "off"}),
            'link': forms.TextInput(attrs={'class': 'one', 'id': 'link', 'placeholder': 'Link', 'autocomplete': "off"}),
            'equip': forms.Select(attrs={'class': 'currency', 'id': 'currency'},choices=choises),
            'comment': forms.TextInput(attrs={'class': 'one', 'id': 'comment', 'placeholder': 'Comment', 'autocomplete': "off"})
        }

class freightform(forms.ModelForm):
    class Meta:
        model = Freight
        fields = ['forwarder','Line','POL','POD','terms','rate','currencyrate','period','contract','additional','currencyadd']
        labels = {
            'Line': False,
            'POL': False,
            'POD': False,
            'terms': False,
            'rate': False,
            'currencyrate': False,
            'period': False,
            'contract': False,
            'additional': False,
            'currencyadd':False,
            'forwarder':False
        }

        widgets = {
            'Line': forms.TextInput(attrs={'class':'one','id': 'search', 'placeholder': 'Line', 'autocomplete':"off"}),
            'POL': forms.TextInput(attrs={'class': 'one', 'id': 'POL', 'placeholder': 'POL', 'autocomplete': "off"}),
            'POD': forms.TextInput(attrs={'class': 'one', 'id': 'POD', 'placeholder': 'POD', 'autocomplete': "off"}),
            'terms': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Terms', 'autocomplete': "off"}),
            'rate': forms.TextInput(attrs={'class': 'one', 'id': 'rate', 'placeholder': 'Rate', 'autocomplete': "off"}),
            'currencyrate': forms.Select(attrs={'class': 'one', 'id': 'currencyrate'},choices=(('USD', 'USD'), ('EUR', 'EUR'),)),
            'period' : forms.TextInput(attrs={'type': "date", 'class': 'date', 'id': 'period', 'placeholder': 'Period', 'autocomplete': "off"}),
            'contract': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Contract', 'autocomplete': "off"}),
            'additional': forms.TextInput(attrs={'class': 'one', 'id': 'additional', 'placeholder': 'Additional costs', 'autocomplete': "off"}),
            'currencyadd': forms.Select(attrs={'class': 'one', 'id': 'add'},choices=(('USD', 'USD'), ('EUR', 'EUR'),)),
            'forwarder': forms.TextInput(attrs={'class': 'one', 'id': 'forwarder', 'placeholder': 'Forwarder', 'autocomplete': "off"})
        }


class freightform1(forms.ModelForm):
    class Meta:
        model = Freight
        fields = ['forwarder','Line','POL','POD','terms','rate','currencyrate','period','contract','additional','currencyadd']
        labels = {
            'Line': False,
            'POL': False,
            'POD': False,
            'terms': False,
            'rate': False,
            'currencyrate': False,
            'period': False,
            'contract': False,
            'additional': False,
            'currencyadd':False,
            'forwarder':False
        }

        widgets = {
            'Line': forms.TextInput(attrs={'class':'one','id': 'search', 'placeholder': 'Line', 'autocomplete':"off"}),
            'POL': forms.TextInput(attrs={'class': 'one', 'id': 'POL', 'placeholder': 'POL', 'autocomplete': "off"}),
            'POD': forms.TextInput(attrs={'class': 'one', 'id': 'POD', 'placeholder': 'POD', 'autocomplete': "off"}),
            'terms': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Terms', 'autocomplete': "off"}),
            'rate': forms.TextInput(attrs={'class': 'one', 'id': 'rate', 'placeholder': 'Rate', 'autocomplete': "off"}),
            'currencyrate': forms.Select(attrs={'class': 'one', 'id': 'currencyrate'},choices=(('USD', 'USD'), ('EUR', 'EUR'),)),
            'period': forms.TextInput(attrs={'class': 'one', 'id': 'period', 'placeholder': 'period', 'autocomplete': "off"}),
            'contract': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Contract', 'autocomplete': "off"}),
            'additional': forms.TextInput(attrs={'class': 'one', 'id': 'additional', 'placeholder': 'Additional costs', 'autocomplete': "off"}),
            'currencyadd': forms.Select(attrs={'class': 'one', 'id': 'add'},choices=(('USD', 'USD'), ('EUR', 'EUR'),)),
            'forwarder': forms.TextInput(attrs={'class': 'one', 'id': 'forwarder', 'placeholder': 'Forwarder', 'autocomplete': "off"})
        }

class containerindex(forms.Form):
    number = forms.CharField(label=False, widget=forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Number', 'autocomplete': "off"}))
    seal = forms.CharField(label=False, widget=forms.TextInput(attrs={'class': 'one', 'id': 'search1', 'placeholder': 'Seal', 'autocomplete': "off"}))
    bales = forms.CharField(label=False, widget=forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Bales', 'autocomplete': "off"}))
    gross = forms.CharField(label=False, widget=forms.TextInput(attrs={'class': 'one', 'id': 'search1', 'placeholder': 'Gross', 'autocomplete': "off"}))
    tara = forms.CharField(label=False, widget=forms.TextInput(attrs={'class': 'one', 'id': 'search1', 'placeholder': 'Tara', 'autocomplete': "off"}))


class containerform(forms.ModelForm):
    class Meta:
        model = Containers
        fields = ['number','seal','bales','gross','tara']

        labels = {
            'number': False,
            'seal': False,
            'bales': False,
            'gross': False,
            'tara': False,
        }

        widgets = {
            'number': forms.TextInput(attrs={'class':'one','id': 'search', 'placeholder': 'Number','autocomplete':"off"}),
            'seal': forms.TextInput(attrs={'class':'one','id': 'search', 'placeholder': 'Seal','autocomplete':"off"}),
            'bales': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Bales', 'autocomplete': "off"}),
            'gross': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Gross', 'autocomplete': "off"}),
            'tara': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Tara', 'autocomplete': "off"}),
        }

class containerform1(forms.ModelForm):
    class Meta:
        model = Containers
        fields = ['number','seal','bales','gross','tara']

        labels = {
            'number': False,
            'seal': False,
            'bales': False,
            'gross': False,
            'tara': False,
        }

        widgets = {
            'number': forms.TextInput(attrs={'class':'one','id': 'search', 'placeholder': 'Number','autocomplete':"off"}),
            'seal': forms.TextInput(attrs={'class':'one','id': 'search', 'placeholder': 'Transaction','autocomplete':"off"}),
            'bales': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Bales', 'autocomplete': "off"}),
            'gross': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Inv. Weight', 'autocomplete': "off"}),
            'tara': forms.TextInput(attrs={'class': 'one', 'id': 'search', 'placeholder': 'Act. Weight', 'autocomplete': "off"}),
        }

class searchform(forms.Form):
    number = forms.CharField(label=False, widget=forms.TextInput(attrs={'class':'one','id': 'search', 'placeholder': 'Number', 'autocomplete': "off"}))

class opsform(forms.Form):
    number = forms.CharField(label=False, widget=forms.TextInput(attrs={'class':'one','id': 'search1', 'placeholder': '', 'autocomplete': "off"}))
    number1 = forms.CharField(label=False, widget=forms.TextInput(attrs={'class':'one','id': 'search2', 'placeholder': '', 'autocomplete': "off"}))


class destform(forms.Form):
    number = forms.CharField(label='POD:', widget=forms.TextInput(attrs={'class':'one','id': 'search', 'placeholder': 'POD', 'autocomplete': "off"}))

class destform1(forms.Form):
    number1 = forms.CharField(label='POD:', widget=forms.TextInput(attrs={'class':'one','id': 'search', 'placeholder': 'POD', 'autocomplete': "off"}))


class freightsearchform(forms.Form):
    POL = forms.CharField(label=False, widget=forms.TextInput(attrs={'class': 'one', 'id': 'POL', 'placeholder': 'POL', 'autocomplete': "off"}))
    POD = forms.CharField(label=False, widget=forms.TextInput(attrs={'class': 'one', 'id': 'POD', 'placeholder': 'POD', 'autocomplete': "off"}))

class indexcost(forms.Form):
    variants = (
        ('Documents', 'Documents'),
        ('BAF', 'BAF'),
        ('CAF', 'CAF'),
        ('Change of Destination', 'Change of Destination'),
        ('Cleaning container', 'Cleaning container'),
        ('Congestion surcharge', 'Congestion surcharge'),
        ('Detention/Demurrage', 'Detention/Demurrage'),
        ('Doc cut off', 'Doc cut off'),
        ('Documents', 'Documents'),
        ('Eurotransport', 'Eurotransport'),
        ('Export Clearance', 'Export Clearance'),
        ('Fuel surcharge', 'Fuel surcharge'),
        ('Goods test', 'Goods test'),
        ('ISPS export', 'ISPS export'),
        ('ISPS import', 'ISPS import'),
        ('Import Clearance', 'Import Clearance'),
        ('Inland Export', 'Inland Export'),
        ('Inland Import', 'Inland Import'),
        ('Inspection', 'Inspection'),
        ('Li/Lo', 'Li/Lo'),
        ('Seafreight', 'Seafreight'),
        ('Seal charge', 'Seal charge'),
        ('THC export', 'THC export'),
        ('THC import', 'THC import'),
        ('Terrestrial Documents', 'Terrestrial Documents'),
        ('Waiting Hours', 'Waiting Hours'),
        ('Warehouses fee', 'Warehouses fee'),
        ('Wasted journey', 'Wasted journey'),
        ('Weighing fee', 'Weighing fee'),
        ('Bank cost', 'Bank cost'),
        ('Handling Fee', 'Handling Fee'),
        ('Сomission', 'Сomission'),
    )

    name = forms.CharField(label=False,widget=forms.Select(attrs={'class': 'one', 'id': 'search'}, choices=variants))
    volume = forms.CharField(label=False, widget=forms.TextInput(attrs={'class': 'one', 'id': 'search1', 'placeholder': 'Volume', 'autocomplete': "off"}))
    currency = forms.CharField(label=False, widget=forms.Select(attrs={'class': 'one', 'id': 'search'}, choices=(('USD', 'USD'), ('EUR', 'EUR'),)))

class bufferf(forms.ModelForm):
    class Meta:
        model = Buffer
        fields = ['comment']

        labels = {
            'comment': False,
        }

        widgets = {
            'comment': forms.TextInput(attrs={'class':'one','id': 'search', 'placeholder': 'Comment','autocomplete':"off"}),
        }

class bufferform(forms.Form):
    Comment = forms.CharField(label=False, widget=forms.TextInput(attrs={'class': 'one', 'id': 'search1', 'placeholder': 'Comment', 'autocomplete': "off"}))

class countryform(forms.ModelForm):
    class Meta:
        model = Ports
        fields = '__all__'

class Monthlyform(forms.ModelForm):
    class Meta:
        choises = (
            ('NOR', 'NOR'),
            ("40'HC", "40'HC"),
            ("40'DC", "40'DC"),
            ("Truck", "Truck"),
            ("Rail", "Rail"),
            ("45'", "45'"),
        )
        model = Monthly
        fields = ['sodate','podate','Supplier','client','origincity','origincountry','destinationcity','destinationcountry','number',\
                  'material','cntr','Tons','min','ETD','ETA','bknumber','shipinstr','equip','link']

        labels = {
            'sodate': "SO date:",
            'podate': "PO date:",
            'Supplier': "Supplier:",
            'client': "Client:",
            'origincity': "Or. City:",
            'origincountry': "Or. Country:",
            'destinationcity': "Dest. City:",
            'destinationcountry': "Dest. Country:",
            'number': "Shipment:",
            'material': "Material:",
            'cntr': "Cntrs:",
            'Tons': "Tons:",
            'min': "Min:",
            'ETD': "ETD:",
            'ETA': "ETA:",
            'bknumber': "BK:",
            'shipinstr':'SI:',
            'equip' : 'Equip:',
            'link' : 'Photos:'
        }
        widgets = {
            'sodate': forms.TextInput(attrs={'class':'one','id': 'sodate', 'placeholder': 'SO date','autocomplete':"off"}),
            'podate': forms.TextInput(attrs={'class':'one','id': 'podate', 'placeholder': 'PO date','autocomplete':"off"}),
            'Supplier': forms.TextInput(attrs={'class': 'one', 'id': 'Supplier', 'placeholder': 'Supplier', 'autocomplete': "off"}),
            'client': forms.TextInput(attrs={'class': 'one', 'id': 'client', 'placeholder': 'Client', 'autocomplete': "off"}),
            'origincity': forms.TextInput(attrs={'class': 'one', 'id': 'origincity', 'placeholder': 'Origin city', 'autocomplete': "off"}),
            'origincountry': forms.TextInput(attrs={'class': 'one', 'id': 'origincountry', 'placeholder': 'Origin country', 'autocomplete': "off"}),
            'destinationcity': forms.TextInput(attrs={'class': 'one', 'id': 'destinationcity', 'placeholder': 'Destination city', 'autocomplete': "off"}),
            'destinationcountry': forms.TextInput(attrs={'class': 'one', 'id': 'destinationcountry', 'placeholder': 'Destination country', 'autocomplete': "off"}),
            'number': forms.TextInput(attrs={'class': 'one', 'id': 'number', 'placeholder': 'Number', 'autocomplete': "off"}),
            'material': forms.TextInput(attrs={'class': 'one', 'id': 'material', 'placeholder': 'Material', 'autocomplete': "off"}),
            'cntr': forms.TextInput(attrs={'class': 'one', 'id': 'cntr', 'placeholder': 'Cntr', 'autocomplete': "off"}),
            'Tons': forms.TextInput(attrs={'class': 'one', 'id': 'tons', 'placeholder': 'Tons', 'autocomplete': "off"}),
            'min': forms.TextInput(attrs={'class': 'one', 'id': 'min', 'placeholder': 'Min payload', 'autocomplete': "off"}),
            'ETD': forms.TextInput(attrs={'class': 'one', 'id': 'ETD', 'placeholder': 'ETD', 'autocomplete': "off"}),
            'ETA': forms.TextInput(attrs={'class': 'one', 'id': 'ETA', 'placeholder': 'ETA', 'autocomplete': "off"}),
            'link': forms.TextInput(attrs={'class': 'one', 'id': 'link', 'placeholder': 'Link', 'autocomplete': "off"}),
            'bknumber': forms.TextInput(attrs={'class': 'one', 'id': 'bknumber', 'placeholder': 'BK', 'autocomplete': "off"}),
            'shipinstr': forms.TextInput(attrs={'class': 'one', 'id': 'shipinstr', 'placeholder': 'SI number', 'autocomplete': "off"}),
            'equip': forms.Select(attrs={'class': 'currency', 'id': 'currency'}, choices=choises)
        }