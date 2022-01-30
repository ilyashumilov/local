def z(request):
    user = request.user
    df_sales = pd.read_excel('/Users/a111/Desktop/Script.xlsx',sheet_name='Shipments')
    df_sales = pd.DataFrame(df_sales)
    count = -1
    print(df_sales)
    for i in df_sales:
        count += 1
        try:
            print(df_sales.loc[count, 'Buyer'])

            client = Empresa.objects.filter(name=df_sales.loc[count, 'Buyer'])[0]
            destination = Ports.objects.filter(port=df_sales.loc[count, 'Destination / City'])[0]
            material = Materials.objects.filter(name=df_sales.loc[count, 'Product / EN643'])[0].name

            proveedor = Empresa.objects.filter(name=df_sales.loc[count, 'Supplier'])[0]
            origin = Ports.objects.filter(port=df_sales.loc[count, 'Origin / City'])[0]
            material = Materials.objects.filter(name=df_sales.loc[count, 'Product / EN643'])[0].name

            min = 0
            try:
                min = float(df_sales.loc[count, 'MT/cntr'].replace(',', '.'))
            except:
                min = float(df_sales.loc[count, 'MT/cntr'])
            cost = 0

            try:
                cost = float(df_sales.loc[count, 'Purchase cost'].replace(',', '.'))
            except:
                cost = float(df_sales.loc[count, 'Purchase cost'])

            sale = SO(user=user, number=df_sales.loc[count, 'SO'], client=client, destination=destination,
                      date=df_sales.loc[count, 'SO date'], material=material, cntr=int(df_sales.loc[count, 'Cntrs']),\
                      Tons=float(str(df_sales.loc[count, 'Tons']).replace(',', '.')), min=min, cost=cost, currency='USD',
                      comment=str(df_sales.loc[count, 'Add. Info']) + str(df_sales.loc[count, 'Order Conditions / Remarks']),\
                      cpt=str(df_sales.loc[count, 'Customers Payment Terms']), stat=True)
            sale.save()

            purchaise = PO(so=sale,number=df_sales.loc[count, 'PO'][:10], Proveedor=proveedor,Origin=origin,
                      date=df_sales.loc[count, 'PO date'], material=material, cntr=int(df_sales.loc[count, 'Cntrs']),\
                      Tons=float(str(df_sales.loc[count, 'Tons']).replace(',', '.')), price=cost, currency='USD',\
                      spt=str(df_sales.loc[count, 'Suppliers Payment Terms']))
            purchaise.save()

            ship = Shipment(po=purchaise,number=df_sales.loc[count, 'PO'],forwarder=df_sales.loc[count, 'Freight Provider'],carrier=df_sales.loc[count, 'Shipping Line'],\
                            cntr=int(df_sales.loc[count, 'Cntrs']),bknumber=str(df_sales.loc[count, 'Forwarder Booking Number']),ETD=df_sales.loc[count, 'ETD'], \
                            ETA=df_sales.loc[count, 'ETA'], BK = True, Si = False, Magic = False,margin=0,marginEUR=0,Truck=True,equip='Truck',\
                            shipinstr=df_sales.loc[count, 'VGM/Si'])

            ship.save()

            cntr=Container(us=request.user,number='',seal='',bales=0,gross=float(str(df_sales.loc[count, 'Tons']).replace(',', '.')),tara=0,vgm=0)
            cntr.save()

            cost2 = Costs(shipment=ship, name='Sale', volume=ship.po.so.cost, currency=ship.po.so.currency)
            cost2.save()
            cost3 = Costs(shipment=ship, name='Purchaise', volume=-ship.po.price, currency=ship.po.currency)
            cost3.save()
            cost = Costs(shipment=ship, name='Freight', volume=-float(df_sales.loc[count, 'Freight']), currency='EUR')
            cost.save()
            actualizeShip(ship.id)

        except:
            pass