from asyncio.windows_events import NULL
from logging import exception
from xmlrpc.client import Boolean
from django.shortcuts import render,redirect
from accounts.models import useraccounts, vendors

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
    mydata={
        'value':2 ,
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
    TIME_ZONE = 'UTC'
    USE_TZ = True
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

