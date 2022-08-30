from asyncio.windows_events import NULL
from logging import exception
from xmlrpc.client import Boolean
from django.shortcuts import render,redirect
from accounts.models import devices, useraccounts, vendors , devicetypes
from django.db import connection

# home page code=========================================================
def index(request):
    return render(request,'index.html')

# authentication code=======================================================
def auth(request):
    user_name = request.GET.get('username')
    jpassword = request.GET.get('password')

    # checking if password is write
    if useraccounts.objects.filter(email= user_name, password = jpassword , isactive = True).exists() is True :
        request.session['email'] = user_name
        return redirect('../dashboard/', )
    
    # if wring it is sent too index ppage
    else:
        myflags={
            'modal_indicator' :  7,
        }
        return render(request,'index.html', myflags)

# DataEntry Page code starts from here-==============================================
def dashboard(request):
    request.session['email']
    all_vendors= vendors.objects.all().values()
    all_types= devicetypes.objects.all().values()
    mydata={
        'value':2 ,
        'vendors': all_vendors,
        'types':all_types,
    }

    return render(request,'dashboard.html',mydata)

#showing records star here==========================================================
def DataDashboard(request):
    objs = (vendors.objects.all().values())
    members = {
        'member' : objs
    }
    print(objs)
    return render(request,'dataDashboard.html', members)

# vendor actions start from here======================================
def addVendor(request):
    vname = str (request.GET.get('vname'))
    vloaction = str (request.GET.get('vloction'))
    vmail = str (request.GET.get('vmail'))
    vnum = str (request.GET.get('vnum'))
    isActive = True
    id= 'nowtime1231'
    try:
        vendordb = vendors(vendorId = id, vendorName = vname, vendorLoaction = vloaction, vendorPhone = vnum, vendorEmail = vmail)
        vendordb.save()
    except:
        print('Something went wrong')
    return redirect('../dashboard/', )


def Delete_Vendors(request):
    vendor_id = request.GET.get('vid')
    member = vendors.objects.get(id=vendor_id)
    member.isactive = False
    member.save()
    return redirect('/records/')


def venderEdit(request):
    vname = str (request.GET.get('vname'))
    vloaction = str (request.GET.get('vloction'))
    vmail = str (request.GET.get('vmail'))
    vnum = str (request.GET.get('vnum'))
    vid = str (request.GET.get('vid'))
    print(vid)
    member = vendors.objects.get(id=vid)
    member.vendorName = vname
    member.vendorLoaction = vloaction
    member.vendorPhone = vnum
    member.vendorEmail = vmail
    member.save()
    return redirect('/records/')

# Vendor acions ends here========================================================

#-=============decive type
def devicetypeSubmit(request):
    vname = str (request.GET.get('device_type'))
    try:
        typesdb = devicetypes(typename = vname)
        typesdb.save()
    except Exception as e: # work on python 3.x
        print('Failed to upload to ftp: '+ str(e))
    return redirect('../dashboard/', )
#========================================================


#Devices actions starts here =================================================

def deviceSubmit(request):
    serialnum = str (request.GET.get('ser_num'))
    hostname = str (request.GET.get('host_name'))
    devicemodel = str (request.GET.get('device_mdel'))
    purchasedate = str (request.GET.get('purchase_date'))
    warrentyperiod = str (request.GET.get('warrenty'))
    vendor_id = str (request.GET.get('vendorid'))
    type_id = str (request.GET.get('type_id'))
    isactive = True
    try:
        all_devices = devices(serialnum = serialnum , hostname = hostname , devicemodel =devicemodel, purchasedate = purchasedate, warrentyperiod = warrentyperiod, vendorid_id = vendor_id, devicetypeid_id=type_id,isactive = isactive)
        all_devices.save()
    except:
        print('Something went wrong')
    return redirect('../dashboard/', )

def deviceShow(request):
    objs = devices.objects.raw('SELECT * FROM accounts_devices, accounts_vendors, accounts_devicetypes WHERE accounts_devices.vendorid_id = accounts_vendors.id AND accounts_devices.devicetypeid_id = accounts_devicetypes.id')
    all_types= devicetypes.objects.all().values()
    all_vendors= vendors.objects.all().values()
    members = {
        'member' : objs,
        'types' : all_types,
        'vendors' : all_vendors
    }
    # for r in devices.objects.raw('SELECT * FROM accounts_devices, accounts_vendors, accounts_devicetypes WHERE accounts_devices.vendorid_id = accounts_vendors.id AND accounts_devices.devicetypeid_id = accounts_devicetypes.id'):
    #     print(r.__dict__)

    # tables = connection.introspection.table_names()
    # seen_models = connection.introspection.installed_models(tables)
    # print(seen_models)
    return render(request,'devicedatadash.html', members)

def deldevices(request):
    serialnum = str (request.GET.get('did'))
    member = devices.objects.get(id=serialnum)
    member.isactive = False
    member.save()
    return redirect('/deviceShow/')