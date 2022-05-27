from datetime import datetime
from django.shortcuts import render,redirect
from nursery.models import ContactUs, UserDetails,ProductDetail,AddToCart,Order,Blogs
from nursery.forms import ContactForm ,RegistrationForm, UserDetailsForm, AdminProfileForm,WriteBlogForm
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm ,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate ,login ,logout ,update_session_auth_hash

from django.core.mail import EmailMessage
from django.template.loader import get_template
# Create your views here.

"""
For Sending Html Email It Needed Argument 
Subject
Sender Email
Recevier Email In List 
Replay Email
Html Template Path
Context Is A Dictionary That Use In Html Template

"""
def html_email_Sanding(subject,html_template_path,reciver_emails,context_dict,attech_d=False,sender_email=settings.EMAIL_HOST_USER,replay_email=settings.EMAIL_HOST_USER):
    email_html_template = get_template(html_template_path).render(context_dict)
    email_message = EmailMessage(
        subject,
        email_html_template,
        sender_email,
        reciver_emails,
        reply_to=[sender_email]
    )
    email_message.content_subtype = 'html'
    if attech_d:
        email_message.attach(attech_d.name,attech_d.read(),attech_d.content_type)
    yes = email_message.send(fail_silently=True)
    return yes

'''
Home Page Carry Resent Added Four Blogs And Products
'''

def home(request):
    blog = Blogs.objects.all().order_by('-pk')[:4]
    product = ProductDetail.objects.all().order_by('-pk')[:4]
    return render(request,'nursery/home.html',{'allpr':product,'allbl':blog})

"""
It's Only Show About Our Project.
"""

def about(request):
    return render(request,'nursery/about.html')

"""
Contact Page Get FeedBack For Both Unknown Or Known User They Can Send Mail Through Fill This Form.

By Mistake User Enter Wrong Email That's Why We Ask Mobile Number For Backup.  
"""

# contact form page
def contact(request):
    if request.method == 'POST':      
        confm = ContactForm(request.POST)
        if confm.is_valid():
            name = confm.cleaned_data['Full_Name']
            email = confm.cleaned_data['Email']
            mobile = confm.cleaned_data['Mobile']
            message = confm.cleaned_data['Message']
            contacts = ContactUs(Full_Name=name,Email=email,Mobile=mobile,Message=message)
            subject= "Contact with me "+name
            html_template_path = 'email/contact_email.html'
            content_html={
                'today':datetime.now(),
                'mobile':mobile,
                'email':email,
                'name':name
            }
            html_email_Sanding(subject=subject,html_template_path=html_template_path,reciver_emails=[email],context_dict=content_html)
            messages.success(request,'Your Message Sended To Uniqe Nursery.')
            contacts.save()
        else:
            messages.error(request,'Please Fill Again')
            confm = ContactForm()
        return render(request,'nursery/contact.html',{'confm':confm})
    else:
        confm = ContactForm()
        return render(request,'nursery/contact.html',{'confm':confm})

"""
Here We Fetch Data Form The DataBase (Blogs,ProductDetail) And Filter By There Plant Type For Showing Differnet Type Of Blogs And Products Respectivly On blog.html and product.html .
"""

def product(request):
    allProds = []
    catProds = ProductDetail.objects.values('Plant_Type','id')
    cats = {item['Plant_Type'] for item in catProds}
    for cat in cats:
        prod = ProductDetail.objects.filter(Plant_Type=cat)
        allProds.append(prod)

    parms = {'products': allProds}
    return render(request,'nursery/product.html',parms)

def blog(request):
    allProds = []
    catProds = Blogs.objects.values('Plant_Type','id')
    cats = {item['Plant_Type'] for item in catProds}
    for cat in cats:
        prod = Blogs.objects.filter(Plant_Type=cat)
        allProds.append(prod)

    parms = {'products': allProds}
    return render(request,'nursery/blog.html',parms)


"""
Here We Fetch That Data From The DataBase That Requested By User To All details Inside In.

That Two Functions Give Us Only Single Row From Their Respective Models Class.

If "productdetails" Function Get POST Request Form The Frontend It Will Collect All Data From That Page And Save To AddToCart Model Through Requested User This POST Request Work Only For Register User Unknown User Can't Be Add Item In The AddToCart Model .
"""

def productdetails(request,myid,type):
    prod = []
    product = ProductDetail.objects.filter(id=myid)
    catProds = ProductDetail.objects.filter(Plant_Type=type)
    prod.append(catProds)
    print(product[0].Product_Name)
    if request.method == 'POST':
        if product[0].Discount_Price == "":
            item_price = product[0].Real_Price
        else:
            item_price = product[0].Discount_Price
        quantity = request.POST['quantity']
        item_price = int(item_price) * int(quantity)
        atc = AddToCart(
            Buyer=request.user.userdetails,
            Product=product[0],
            Product_Amount=item_price,
            Product_Quantity=quantity
        )
        atc.save()
        messages.success(request,f"{product[0].Product_Name} Is Added In Your Cart.")
        return redirect('/addtocart/')
    return render(request,'nursery/productdetail.html',{'product':product[0],'prod':prod})

def readblog(request,myid,type):
    blog = Blogs.objects.filter(id=myid,Plant_Type=type)
    return render(request,'nursery/readblog.html',{'blog':blog[0]})

"""
Order or Add to cart process writen here
"""
@login_required(login_url='/login/')
def addtocart(request):
    cart = AddToCart.objects.filter(Buyer=request.user.userdetails)
    if request.method == "POST":
        if 'Order' in request.POST:
            buyer = request.user.userdetails
            product_id = request.POST['prid']
            quantity = request.POST['quantity']
            price = request.POST['price']
            product = ProductDetail.objects.filter(id=product_id)
            print(product[0])
            if request.user.userdetails.Address == " ":
               messages.error(request,"First Fill Your Personal Details In Your Profile.")
            else: 
                od = Order(
                    Buyer = buyer,
                    Product = product[0],
                    Product_Quantity = quantity[10:],
                    Product_Amount = price[2:],
                )
                od.save()

                # Html Template Email Sending Process
                to = request.user.userdetails.Email
                address = request.user.userdetails.Address
                pincode = request.user.userdetails.Pincode
                mobile = request.user.userdetails.Mobile
                name = product[0].Product_Name
                img = product[0].Product_Img
                subject = f'{name} - Order Placed'
                html_template_path = 'email/order_email.html'
                content_html = {
                    'product_name':name,
                    'address':f"{address}<br><br>{pincode}",
                    'quantity':quantity,
                    'price':price,
                    'mobile':mobile
                }
                yes = html_email_Sanding(subject=subject,html_template_path=html_template_path,reciver_emails=[to],attech_d=img,context_dict=content_html)
                
                # Html Template Email Send
                if yes:
                    messages.success(request,"Your Order Placed.\n Pay After Delivery.\n Prepaid Not Available.\n Your Mail Adderss Is Incorrect.")
                else:
                    messages.success(request,"Your Order Placed.\n Pay After Delivery.\n Prepaid Not Available.\n Check Mail For Confirmation.")
                return redirect('/')
        elif 'Remove' in request.POST:
            product_id = request.POST['prid']
            addcart = AddToCart.objects.get(id=product_id)
            addcart.delete()        
    return render(request,'nursery/addtocart.html',{'added':cart})

@login_required(login_url='/login/')
def orders(request):
    orders = Order.objects.filter(Buyer = request.user.userdetails)
    if request.method =="POST":
        product_id = request.POST['prid']
        ord = Order.objects.get(id=product_id)
        ord.update(Order_Cancel_Position=True)
    return render(request,'nursery/order.html',{'orders':orders})

"""
Adding New Content Form Frontend To DataBase Like : Blogs ,Products .

Login Required For Both Function Only Register User Can Have Authority To Add New Blog & Product For Sell.
"""


@login_required(login_url='/login/')
def addproduct(request):
    if request.method == 'POST':
        prodimg = request.FILES['prodimg']
        prodname = request.POST['prodname']
        planttype = request.POST['prodtype']
        real = request.POST['real']
        discount = request.POST['discount']
        description = request.POST['description']
        light = request.POST['light']
        watering = request.POST['watering']
        wheretogrow = request.POST['wheretogrow']
        maintenace = request.POST['maintenace']
        specialfeature = request.POST['specialfeature']
        secondtimg = request.FILES['secondtimg']
        
        addnew = ProductDetail(
            Product_Img=prodimg,
            Product_Name = prodname,
            Plant_Type = planttype,
            Real_Price = real,
            Discount_Price = discount,
            Description = description,
            Light =light,
            Watering = watering,
            Where_To_Grow = wheretogrow,
            Maintenance = maintenace,
            Special_Feature = specialfeature,
            Second_Img = secondtimg
        )
        addnew.save()
        messages.success(request,f'Item - {prodname} added.')
    return render(request,'nursery/addproduct.html')

@login_required(login_url='/login/')
def writeblog(request):
    if request.method == 'POST':
        tegfm = WriteBlogForm(request.POST)
        if tegfm.is_valid():
            plantessentials=tegfm.cleaned_data['Plant_Essentials']
            commonproblems=tegfm.cleaned_data['Common_Problems']
            styleanddécor=tegfm.cleaned_data['Style_and_Décor']
        prodimg = request.FILES['prodimg']
        blogname = request.POST['prodname']
        author = request.POST['author']
        planttype = request.POST['prodtype']
        description = request.POST['description']
        light = request.POST['light']
        watering = request.POST['watering']
        wheretogrow = request.POST['wheretogrow']
        maintenace = request.POST['maintenace']
        specialfeature = request.POST['specialfeature']
        secondtimg = request.FILES['secondtimg']
        
        addnew = Blogs(
            Main_Img=prodimg,
            Blog_Name = blogname,
            Author=author,
            Plant_Type = planttype,
            Small_Info = description,
            Light =light,
            Watering = watering,
            Where_To_Grow = wheretogrow,
            Maintenance = maintenace,
            Special_Feature = specialfeature,
            Second_Img = secondtimg,
            Plant_Essentials=plantessentials,
            Common_Problems=commonproblems,
            Style_and_Décor=styleanddécor
        )
        addnew.save()
        messages.success(request,f'Blog - {blogname} added.')
    elif request.method == 'get':
        messages.error(request,f'Blog can not be add.')
    tegfm = WriteBlogForm()
    return render(request,'nursery/writeblog.html',{'form':tegfm})

"""Authentication Function Starts From Here"""

# registration page 
def registration(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            regfm = RegistrationForm(request.POST)
            if regfm.is_valid():
                user = regfm.save()
                UserDetails.objects.create(
                    User = user,
                    Email = user.email,
                )
                messages.success(request,'Registrations Successfully Done.')
                return redirect('/login/')
            else:
                messages.error(request,'Password Could Not Be Same As Email Or Username')
        else:
            regfm = RegistrationForm()
        return render(request,'nursery/registration.html',{'regfm':regfm})
    else:
        return redirect('/profile/')

# login page 
def loginUser(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            logfm = AuthenticationForm(request=request, data=request.POST)
            if logfm.is_valid():
                uname = logfm.cleaned_data['username']
                upass = logfm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Login Successfully Done.')
                    return redirect('/profile/')
                else:
                    messages.error(request,'Password Or Username Not Match')
            else:
                messages.error(request,'Password Or Username Not Match')
                
        else:
            logfm = AuthenticationForm()
        return render(request,'nursery/login.html',{'logfm':logfm})
    else:
        return redirect('/profile/')

# logout page 
def logoutUser(request):
    logout(request)
    messages.success(request,'Logout Successfully.')
    return redirect('/login/')

# profile page
@login_required(login_url='/login/')
def profile(request):
    # if request.user.is_superuser == True:
    #     if request.method == "POST":
    #         fm = AdminProfileForm(request.POST,request.FILES,instance=request.user)
    #         if fm.is_valid():
    #             fm.save()
    #             messages.success(request,f'{request.user} Profile Successfully Update')
    #     else:
    #         fm = AdminProfileForm(instance=request.user)
    # else:
    #     if request.method == "POST":
    #         fm = UserDetailsForm(request.POST,request.FILES,instance=request.user.userdetails)
    #         if fm.is_valid():
    #             fm.save()
    #             messages.success(request,f'{request.user} Profile Successfully Update')
    #     else:
    #         fm = UserDetailsForm(instance=request.user.userdetails)
    try:
        if request.method == "POST":
            fm = UserDetailsForm(request.POST,request.FILES,instance=request.user.userdetails)
            if fm.is_valid():
                fm.save()
                messages.success(request,f'{request.user} Profile Successfully Update')
        else:
            fm = UserDetailsForm(instance=request.user.userdetails)
    except Exception as e:
        UserDetails.objects.create(
            User = request.user,
            Email = request.user.email,
        )
        fm = UserDetailsForm(instance=request.user.userdetails)
    return render(request,'nursery/profile.html',{'fm':fm})

# changepassword page 
@login_required(login_url='/login/')
def changepassword(request):
    if request.method == "POST":
        chpass = PasswordChangeForm(user=request.user,data=request.POST)
        if chpass.is_valid():
            chpass.save()
            messages.success(request,'Password Has Been Changed')
            update_session_auth_hash(request,chpass.user)
            return redirect('/profile/')
        else:
            messages.error(request,'Password Not Change')
    else:
        chpass = PasswordChangeForm(user=request.user)
    return render(request,'nursery/changepassword.html',{'chpass':chpass})

# forgotpassword page 
def forgotpassword(request):
    if request.method == "POST":
        fgpass = SetPasswordForm(user=request.user,data=request.POST)
        if fgpass.is_valid():
            fgpass.save()
            messages.success(request,'Password Has Been Changed')
            update_session_auth_hash(request,fgpass.user)
            return redirect('/profile/')
        else:
            messages.error(request,'Password Not Change')
    else:
        fgpass = SetPasswordForm(user=request.user)
    return render(request,'nursery/forgotpassword.html',{'fgpass':fgpass}) 

