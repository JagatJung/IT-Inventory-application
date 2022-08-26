from asyncio.windows_events import NULL
from logging import exception
from xmlrpc.client import Boolean
from django.shortcuts import render,redirect
from accounts.models import useraccounts

# home page code
def index(request):
    return render(request,'index.html')

# authentication code
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

def dashboard(request):
    print(request.session['email']) 
    mydata={
        'value':2 ,
    }
    return render(request,'dashboard.html',mydata)