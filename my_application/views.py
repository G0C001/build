from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import get_mens,get_women,get_kids
from .models import create_user
from .forms import form1,form2,form3,register_user,login_user
import psycopg2

def admin(request):
    return render(request,"admin.html")
    
user_phone = {'phone': '0','name':'name'}

def user(request):
    register = register_user()
    login = login_user()

    data = create_user.objects.all()

    if request.method == 'POST':
        if 'register_user' in request.POST:
            form = register_user(request.POST)
            phone = request.POST['phone']
            user_phone['phone'] = phone

            if data.filter(phone=phone).exists():
                messages.error(request, 'User phone already exists')
            elif form.is_valid():
                form.save()
                connection = psycopg2.connect(
                    host = "ep-patient-glade-73852248-pooler.us-east-1.postgres.vercel-storage.com",
                    database = "verceldb",
                    user = "default",
                    password = "2MAihOc3IRZD"
                )
                mycursor = connection.cursor()
                x = "CREATE TABLE user{} (id SERIAL PRIMARY KEY, product_img VARCHAR(100), product_Name VARCHAR(100), product_price VARCHAR(100), product_details VARCHAR(100))".format(phone)
                mycursor.execute(x)
                connection.commit()
                messages.success(request, 'Registered successfully')
                return redirect("user")

        elif 'login_user' in request.POST:
            loginphone = request.POST.get('phone')
            loginpassword = request.POST.get('password')
            user_phone['phone'] = loginphone
            data = create_user.objects.all()
            valid_user = False

            for i in data:
                if i.phone == loginphone and i.password == loginpassword:
                    valid_user = True
                    user_phone['name'] = i.name
                    view_name = user_phone['name']
                    break

            if valid_user:
                return render(request, 'home.html',{'view_name':view_name})
            else:
                messages.error(request, 'Wrong phone or password')

    return render(request, 'user.html', {'register': register,'login': login})



view_cart = {'product_img':'0','product_Name':'0','product_price':'0','product_details':'0'}


def addme(request):
    view_name = user_phone['name']
    x = user_phone['phone']
    phone = int(x)
    a = view_cart['product_img']
    b = view_cart['product_Name']
    c = view_cart['product_price']
    d = view_cart['product_details']
    connection = psycopg2.connect(
                    host = "ep-patient-glade-73852248-pooler.us-east-1.postgres.vercel-storage.com",
                    database = "verceldb",
                    user = "default",
                    password = "2MAihOc3IRZD"
                )
    mycursor = connection.cursor()
    # x = ("insert into user{} values(id,%s,%s,%s,%s)").format(phone)
    x = "INSERT INTO user{} (product_img, product_Name, product_price, product_details) VALUES (%s, %s, %s, %s)".format(phone)
    val = a,b,c,d
    mycursor.execute(x,val)
    connection.commit()
    return render(request, 'home.html',{'view_name':view_name})

def addtocart(request):
    x = user_phone['phone']
    phone = int(x)
    connection = psycopg2.connect(
                    host = "ep-patient-glade-73852248-pooler.us-east-1.postgres.vercel-storage.com",
                    database = "verceldb",
                    user = "default",
                    password = "2MAihOc3IRZD"
                )
    mycursor = connection.cursor()
    x = ("select * from user{}").format(phone)
    mycursor.execute(x)
    cart_val = mycursor.fetchall()
    return render(request, 'addtocart.html', {'cart_val': cart_val})

def mens_cart(request,id):
    cart_data = get_mens.objects.get( id = id )
    view_cart['product_img'] = cart_data.product_img
    view_cart['product_Name'] = cart_data.product_Name
    view_cart['product_price'] = cart_data.product_price
    view_cart['product_details'] = cart_data.product_details
    return render(request, 'cart.html', {'cart_data': cart_data})

def womens_cart(request,id):
    cart_data = get_women.objects.get( id = id )
    view_cart['product_img'] = cart_data.product_img
    view_cart['product_Name'] = cart_data.product_Name
    view_cart['product_price'] = cart_data.product_price
    view_cart['product_details'] = cart_data.product_details
    return render(request, 'cart.html', {'cart_data': cart_data})

def kids_cart(request,id):
    cart_data = get_kids.objects.get( id = id )
    view_cart['product_img'] = cart_data.product_img
    view_cart['product_Name'] = cart_data.product_Name
    view_cart['product_price'] = cart_data.product_price
    view_cart['product_details'] = cart_data.product_details
    return render(request, 'cart.html', {'cart_data': cart_data})

def home(request):
    view_name = user_phone['name']
    return render(request, 'home.html',{'view_name':view_name})

def update_mens(request):
    if request.method == 'POST':
        form = form1(request.POST)
        if form.is_valid():   
            form.save()
            messages.success(request, ' details update Successfully')
            return redirect("admin")
    else:
        form = form1()
        check = ""
    return render(request, 'admin_mens.html', {'form': form})

def update_womens(request):
    if request.method == 'POST':
        form = form2(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' details update Successfully')
            return redirect("admin")
    else:
        form = form2()
        check = ""
    return render(request, 'admin_womens.html', {'form': form})

def update_kides(request):
    if request.method == 'POST':
        form = form3(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' details update Successfully')
            return redirect("admin")
    else:
        form = form3()
        check = ""
    return render(request, 'admin_kides.html', {'form': form})

def mens(request):
    data = get_mens.objects.all()
    return render(request, 'mens.html', {'data':data})

def womens(request):
    data = get_women.objects.all()
    return render(request, 'womens.html', {'data':data})

def kids(request):
    data = get_kids.objects.all()
    return render(request, 'kids.html', {'data':data})