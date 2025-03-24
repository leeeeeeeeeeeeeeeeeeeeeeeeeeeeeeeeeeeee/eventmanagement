import datetime
from pyexpat.errors import messages
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from event.forms import Signupform,SigninForm
from event.models import *  # Import the eventteam model
from django.views.generic import View
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth import logout

from django.contrib.auth.models import User
from eventmanagement import settings

# Create your views here.




def strt(request):
    
    if request.user.is_staff:
        return render(request,'eventteam/eventhome.html')
    else:
        return redirect("/event/clienthome/")

def home(request):
    return render(request,"clienthome.html")

def packages(request):
    packages = packagemodel.objects.all()
    return render(request,"client/packages.html",{"a":packages})

def signpage(request):
    return render(request,"signpage.html")

def loginpage(request):
    return render(request,"auth-apps/login.html")




   

                       # event team

def chome(request):
    b = packagemodel.objects.filter(PLOG__id=request.user.id)
    return render(request, "eventteam/eventhome.html", {"a": b})


def addpkg(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        det=request.POST.get('det')
        photo1=request.FILES.get('photo-1')
        photo2=request.FILES.get('photo-2')
        photo3=request.FILES.get('photo-3')
        photo4=request.FILES.get('photo-4')

        print(title)
        fs=FileSystemStorage()

        photo_name1=datetime.datetime.now().strftime("%Y%m%d%H%M%S")+"_1.jpeg"
        fs.save(photo_name1,photo1)
        photo_path_1=fs.url(photo_name1)

        photo_name2=datetime.datetime.now().strftime("%Y%m%d%H%M%S")+"_2.jpeg"
        fs.save(photo_name2,photo2)
        photo_path_2=fs.url(photo_name2)

        photo_name3=datetime.datetime.now().strftime("%Y%m%d%H%M%S")+"_3.jpeg"
        fs.save(photo_name3,photo3)
        photo_path_3=fs.url(photo_name3)

        photo_name4=datetime.datetime.now().strftime("%Y%m%d%H%M%S")+"_4.jpeg"
        fs.save(photo_name4,photo4)
        photo_path_4=fs.url(photo_name4)

        package=packagemodel(
            title=title,
            discription=det,
            photo1=photo_path_1,
            photo2=photo_path_2,
            photo3=photo_path_3,
            photo4=photo_path_4,
            PLOG=request.user
        )
        package.save()
        return redirect('/event/chome/')
    
    return render(request,"eventteam/addpackages.html")


def edelete(request,cid):
    packagemodel.objects.filter(id=cid).delete()
    return redirect('/event/chome/')



def e_editpage(request, cid):
    a=packagemodel.objects.get(id=cid)
    return render(request,"eventteam/edit.html",{"a":a})

def e_edit(request):
    a=request.POST['title']
    b=request.POST['dis']

    d=request.POST['id']

    obj=packagemodel.objects.get(id=d)
    obj.title=a
    obj.discription=b

    if 'img' in request.FILES:
        c = request.FILES['img']
        if c !="":
            date = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".jpeg"
            fs = FileSystemStorage()
            fs.save(date, c)
            path = fs.url(date)
            obj.photo=path
    obj.save()
    return redirect('/event/chome/')

def accept_appointment(request):
    id=request.POST['id']
    amount=request.POST['amount']
    a=appointments.objects.filter(id=id).update(status="accepted",estimate="requested",amount=amount)
    email = appointments.objects.get(id=id).USER.email
    send_mail(
        "your appointment has been accepted",
        "we are ready for your event.we shared our estiamte details ,u can check it on ouer webpage",
        "accoutfortrail@gmail.com",
        [email],
        fail_silently=False,
    )
    return redirect('/event/chome')

def reject_appointment(request,cid):
    a=appointments.objects.filter(id=cid).update(status="rejected")
    email = appointments.objects.get(id=cid).USER.email
    send_mail(
        "your appointment has been rejected",
        "due your scheduled time is already booked",
        "accoutfortrail@gmail.com",
        [email],
        fail_silently=False,
    )
    return redirect('/event/chome')





        # LOGIN



                            #client


def clienthome(request):
    return render(request, "clienthome.html", )

def showmore(request,cid):
    C=packagemodel.objects.get(id=cid)
    # b=eventteam.objects.get(id=C)
    return render(request,"client/more.html",{"a":C,})




def ajxbooking(request):
    date=request.GET.get('date')
    time=request.GET.get('time')
    id=request.GET.get('id')
    # time=request.POST['time']
    print(date,time,id)

    obj=appointments.objects.filter(date=date,time=time,ALOG_id=id,USER__LOGIN_id=request.session['logid']).exists()

    return JsonResponse({"status":obj})




def cprofile(request):
    v1=signuptable.objects.get(LOGIN_id=request.session['logid'])
    v6 = appointments.objects.filter(USER__LOGIN__id=request.session['logid'])
    return render(request,"client/profile.html",{"a":v1,"b":v6})
def editcprfle(request):
    v1 = signuptable.objects.get(LOGIN_id=request.session['logid'])
    return render(request, "client/editp.html", {"a": v1})

def cpedited(request):
    name=request.POST["name"]
    email =request.POST["email"]
    number =request.POST["number"]
    place =request.POST["place"]
    v1 = signuptable.objects.filter(LOGIN_id=request.session['logid'])
    v1.update(name=name,email=email,place=place,number=number)
    v2=logintable.objects.filter(id=request.session['logid']).update(user=email)
    return HttpResponse(''''<script>window.location="/event/cprofile/"</script>''')

def cpass(request):
    v1=logintable.objects.filter(id=request.session['logid'])
    return render(request,"client/clientpass.html",{"a":v1})

def cpasscahnge(request):
    a=request.POST['pass']
    v1=logintable.objects.filter(id=request.session['logid']).update(password=a)
    return HttpResponse(''''<script>window.location="/event/strt/"</script>''')

def feed(request):
    return render(request,"client/feedback.html")

def feedbacks(request):
    a=request.POST['a']


    v = feedback()
    v.a=a
    v.FDLOG_id=request.session['logid']
    v.save()
    return HttpResponse(''''<script>window.location="/event/clienthome/"</script>''')

def comp(request):
    return render(request,"complints.html")

def shwrequsts(request,cid):
    a=appointments.objects.filter(USER__LOGIN__id=request.session['logid'])
    return render(request,"client/requests.html",{"b":a})

def raz_pay(request,amount,id):
    import razorpay
    razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
    razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"

    razorpay_client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

    # amount = 200
    amount= float(amount)*100

    # Create a Razorpay order (you need to implement this based on your logic)
    order_data = {
        'amount': amount,
        'currency': 'INR',
        'receipt': 'order_rcptid_11',
        'payment_capture': '1',  # Auto-capture payment
    }

    # Create an order
    order = razorpay_client.order.create(data=order_data)

    context = {
        'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],
    }

    obj = payments()
    obj.REQ_MAIN_id = id
    obj.p_date = datetime.datetime.now().strftime('%Y%m%d')
    obj.amnt = float(amount)
    obj.p_status = 'paid'
    obj.save()

    appointments.objects.filter(id=id).update(estimate="accepted")

    return render(request, 'payment.html',{ 'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],"id":id})



def estiamteaccept(request,cid):
    appointments.objects.filter(id=cid).update(estimate="accepted")
    return redirect("/event/clienthome/")

def estimatereject(request,cid):
    a=appointments.objects.filter(id=cid).update(estimate="rejected")
    email=appointments.objects.get(id=cid).ALOG.PLOG.email

    return redirect("/event/clienthome/")



def request(request):
    v = eventteam.objects.filter(status="pending")
    v4 = eventteam.objects.filter(status="approved")
    v5 = cmplnt.objects.filter(re="pending")
    v6 = feedback.objects.all()
    v7 = appointments.objects.all()
    return render(request,"admin/requests.html",{"a":v,"b":v4,"c":v5,"d":v6,"e":v7})



def v_accept(request,cid):
    v = eventteam.objects.get(id=cid)
    v.status="approved"
    v.save()
    return redirect("/event/request/")
def v_reject(request,cid):
    v = eventteam.objects.get(id=cid)
    v.status = "rejected"
    v.save()
    return redirect("/event/request/")

def complntpage(request):
    return render(request,"client/complaint.html")
def sendcomplaint(request):
    a=request.POST['complaint']
    obj=cmplnt()
    obj.time=datetime.datetime.now()
    obj.c=a
    obj.re="pending"
    obj.CLOG_id=request.session['logid']
    obj.save()
    return redirect("/event/clienthome")



                #admin
def adminhm(request):
    v3 = signuptable.objects.all()
    v4 = eventteam.objects.filter(status="approved")
    v5 = cmplnt.objects.filter(re="pending")
    v6 = feedback.objects.all()
    v7 = appointments.objects.all()
    return render(request, "admin/adminhome.html", {"a": v3, "b": v4, "c": v5, "d": v6, "e": v7})


def admincomplaint(request):
    a=cmplnt.objects.filter(re='pending')
    v4 = eventteam.objects.filter(status="approved")
    v5 = cmplnt.objects.filter(re="pending")
    v6 = feedback.objects.all()
    v7 = appointments.objects.all()
    return render(request,"admin/complaints.html",{"a":a,"b":v4,"c":v5,"d":v6,"e":v7})
def adminreply(request,):
    a=request.POST['aa']
    id=request.POST['id']
    ob=cmplnt.objects.filter(id=id).update(re=a)
    return redirect("/event/admincomplaint")
def adminfeedback(request):
    ob=feedback.objects.all()
    v4 = eventteam.objects.filter(status="approved")
    v5 = cmplnt.objects.filter(re="pending")
    v6 = feedback.objects.all()
    v7 = appointments.objects.all()
    return render(request,"admin/feedback.html",{"a":ob,"b":v4,"c":v5,"d":v6,"e":v7})




def openevent(request,id):
    a=packagemodel.objects.filter(PLOG_id=id)
    return render(request,"admin/openevnet.html",{"a":a})

def logoutview(request):
    logout(request)
    request.session['logid']=""
    return redirect("/event/home")

def SigninView(request):
    # Track page history
    history = request.session.get('page_history', [])
    if request.META.get('HTTP_REFERER') and request.META.get('HTTP_REFERER') not in history[-2:]:
        history.append(request.META.get('HTTP_REFERER'))
    request.session['page_history'] = history[-2:]  # Keep last 2 pages

    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pass')
        print(user, "helloooo")
        user_object = authenticate(request, username=user, password=pwd)
        if user_object:
            print('valid')
            print(type(user_object), user_object)
            login(request, user_object)
            request.session['logid'] = user_object.id
            return redirect(history[0] if len(history) >= 2 else '/')
        else:
            print('invalid')
            return render(request, "auth-apps/login.html")
    return render(request, "auth-apps/login.html")
    




class SignupView(View):
    def get(self, request, *args, **kwargs):
        form_instance = Signupform()  # Ensure Signupform is imported
        return render(request, "auth-apps/signpage.html", {"form": form_instance})

    def post(self, request, *args, **kwargs):
        # Track page history
        history = request.session.get('page_history', [])
        if request.META.get('HTTP_REFERER') and request.META.get('HTTP_REFERER') not in history[-2:]:
            history.append(request.META.get('HTTP_REFERER'))
        request.session['page_history'] = history[-2:]  # Keep last 2 pages

        form_data = request.POST
        form_instance = Signupform(form_data)
        if form_instance.is_valid():
            data = form_instance.cleaned_data
            user = User.objects.create_user(
                email=data['email'],
                username=data['username'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                password=data['password']
            )
            user.save()
            print("account created")
            return redirect(history[0] if len(history) >= 2 else '/')
        print("nooo")
        return render(request, "auth-apps/signpage.html", {"form": form_instance})
            



def signup_manager(request):
    if request.method == 'POST':
        # Extract form data
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        #
        if not username or not password or not email:
            messages.error(request, "All fields are required.")
            return render(request, 'auth-apps/manager-signup.html')

      
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, 'auth-apps/manager-signup.html')

       
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                is_staff=True  
            )
            user.save()

            login(request, user)
            request.session['logid']=user.id
            messages.success(request, "Signup successful! You are now a staff member.")
            return redirect("/event/chome")  # Replace 'home' with your desired redirect URL

        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'auth-apps/manager-signup.html')


    return render(request, 'auth-apps/manager-signup.html')



def signin_manager(request):
    if request.method == 'POST':
        user= request.POST.get('username')
        password= request.POST.get('password')

        if not user or not password:
            messages.error(request,"username and password are required")
            return render(request,'auth-apps/manager_signin.html')
        
        user_object=authenticate(request,username=user,password=password)
        if user_object is not None:

            if user_object.is_staff:
                login(request,user_object)
                request.session['logid']=user_object.id
                messages.success(request,"login successful! welcome, event manager")
                return redirect("/event/chome")
            else:
                messages.error(request,"you must be a staff member to login here")
                return render(request,'auth-apps/manager_signin.html')
        else:
            messages.error(request,"Invalid username or password")
            return render(request,'auth-apps/manager_signin.html')

    return render(request,'auth-apps/manager_signin.html')

def make_enquery(request, cid):

    if request.method != 'POST':
        request.session['package_id'] = cid
        return render(request, 'client/client_enquery.html')

    if request.method == 'POST':
        location = request.POST.get('location')
        date = request.POST.get('date')
        description = request.POST.get('description')

        print(location,date,description)

        if not all([location, date, description]):
            messages.error(request, "All fields are required")
            return render(request, 'client/client_enquery.html')

        try:
            appointment = appointments(
                date=date,
                location=location,
                details=description,
                status="pending",
                amount="",
                estimate="",
                USER=User.objects.get(id=request.user.id),
                ALOG=packagemodel.objects.get(id=request.session['package_id'])
            )
            appointment.save()
            return redirect('/event/packages')

        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'client/client_enquery.html')
        
def equiriespage(request):
    enquiry=appointments.objects.filter(ALOG__PLOG__id=request.user.id)
    return render(request,"eventteam/enquiry.html",{"a":enquiry})
