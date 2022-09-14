from audioop import avg
from email import message
from random import random
from re import A

from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.db.models import Q,F
from sellerapp.models import *
from mainapp.models import *
from django.contrib import messages
from django.core.paginator import Paginator
import requests
import random
from textblob import TextBlob
from django.db.models import Sum,Avg
from filpkartproject.RazorpayApi import RazorpayClient
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

import statistics

# Create your views here.
def customer_dashboard(request):
        customer_id=request.session['user_id']
        wishlist=ProductUploadModel.objects.filter(product_watchlist=customer_id).count()
        cart_count=CartModel.objects.filter(cart_owner=customer_id).count()
        cart=CartModel.objects.filter(cart_owner=customer_id)
        data2=CartModel.objects.filter(cart_owner=customer_id).aggregate((Sum('cart_product_price')))
        total=data2['cart_product_price__sum']
        print(total)
        Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').all()
        listing2=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(purchasedcount__gte = 5)
        if request .method=="POST" and 'searchbtn' in request.POST:
            print('search')
            search=request.POST.get("search")
            Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(Q(pro_name__icontains=search) | Q(catagory__icontains=search) | Q(pro_prize__icontains=search)|Q(pro_discount__icontains=search))
       
        elif request.method=="POST" and 'filterbtn' in request.POST:
            print('filter')
            pro_name = request.POST.get("product_name")
            print(pro_name)
            catagory = request.POST.get("category")
            print(catagory)
            pro_prize=request.POST.get("pro_prize  ")
            print(pro_prize)
            pro_discount=request.POST.get("pro_discount")
            print(pro_discount)
            
                    
            Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(Q(pro_name__iexact=pro_name) | Q(catagory__iexact=catagory) | Q(pro_prize__iexact=pro_prize)|Q(pro_discount__iexact=pro_discount))
            print(Listing)
        return render(request,'main/customer-index.html',{'List':Listing,"cart":cart,'listing2':listing2,'cart_count':cart_count,'total':total,'wishlist':wishlist})

def laptops_customer_dashboard(request):
        customer_id=request.session['user_id']
        wishlist=ProductUploadModel.objects.filter(product_watchlist=customer_id).count()
        cart_count=CartModel.objects.filter(cart_owner=customer_id).count()
        cart=CartModel.objects.filter(cart_owner=customer_id)
        data2=CartModel.objects.filter(cart_owner=customer_id).aggregate((Sum('cart_product_price')))
        total=data2['cart_product_price__sum']
        print(total)
        Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(catagory='Laptops')
        listing2=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(purchasedcount__gte = 5)
        if request .method=="POST" and 'searchbtn' in request.POST:
            print('search')
            search=request.POST.get("search")
            Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(Q(pro_name__icontains=search) | Q(catagory__icontains=search) | Q(pro_prize__icontains=search)|Q(pro_discount__icontains=search))
        elif request.method=="POST" and 'filterbtn' in request.POST:
            print('filter')
            pro_name = request.POST.get("product_name")
            print(pro_name)
            catagory = request.POST.get("category")
            print(catagory)
            pro_prize=request.POST.get("pro_prize  ")
            print(pro_prize)
            pro_discount=request.POST.get("pro_discount")
            print(pro_discount)
            
                    
            Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(Q(pro_name__iexact=pro_name) | Q(catagory__iexact=catagory) | Q(pro_prize__iexact=pro_prize)|Q(pro_discount__iexact=pro_discount))
            print(Listing)
        return render(request,'main/customer-index.html',{'List':Listing,"cart":cart,'listing2':listing2,'cart_count':cart_count,'total':total,'wishlist':wishlist})
def customer_dashboard_smartphone(request):
        customer_id=request.session['user_id']
        wishlist=ProductUploadModel.objects.filter(product_watchlist=customer_id).count()
        cart_count=CartModel.objects.filter(cart_owner=customer_id).count()
        cart=CartModel.objects.filter(cart_owner=customer_id)
        data2=CartModel.objects.filter(cart_owner=customer_id).aggregate((Sum('cart_product_price')))
        total=data2['cart_product_price__sum']
        print(total)
        Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(catagory='Smartphones')
        listing2=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(purchasedcount__gte = 5)
        if request .method=="POST" and 'searchbtn' in request.POST:
            print('search')
            search=request.POST.get("search")
            Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(Q(pro_name__icontains=search) | Q(catagory__icontains=search) | Q(pro_prize__icontains=search)|Q(pro_discount__icontains=search))
        elif request.method=="POST" and 'filterbtn' in request.POST:
            print('filter')
            pro_name = request.POST.get("product_name")
            print(pro_name)
            catagory = request.POST.get("category")
            print(catagory)
            pro_prize=request.POST.get("pro_prize  ")
            print(pro_prize)
            pro_discount=request.POST.get("pro_discount")
            print(pro_discount)
            
                    
            Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(Q(pro_name__iexact=pro_name) | Q(catagory__iexact=catagory) | Q(pro_prize__iexact=pro_prize)|Q(pro_discount__iexact=pro_discount))
            print(Listing)
        return render(request,'main/customer-index.html',{'List':Listing,"cart":cart,'listing2':listing2,'cart_count':cart_count,'total':total,'wishlist':wishlist})


def customer_dashboard_cameras(request):
        customer_id=request.session['user_id']
        wishlist=ProductUploadModel.objects.filter(product_watchlist=customer_id).count()
        cart_count=CartModel.objects.filter(cart_owner=customer_id).count()
        cart=CartModel.objects.filter(cart_owner=customer_id)
        data2=CartModel.objects.filter(cart_owner=customer_id).aggregate((Sum('cart_product_price')))
        total=data2['cart_product_price__sum']
        print(total)
        Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(catagory='Cameras')
        listing2=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(purchasedcount__gte = 5)
        if request .method=="POST" and 'searchbtn' in request.POST:
            print('search')
            search=request.POST.get("search")
            Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(Q(pro_name__icontains=search) | Q(catagory__icontains=search) | Q(pro_prize__icontains=search)|Q(pro_discount__icontains=search))
        elif request.method=="POST" and 'filterbtn' in request.POST:
            print('filter')
            pro_name = request.POST.get("product_name")
            print(pro_name)
            catagory = request.POST.get("category")
            print(catagory)
            pro_prize=request.POST.get("pro_prize  ")
            print(pro_prize)
            pro_discount=request.POST.get("pro_discount")
            print(pro_discount)
            
                    
            Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(Q(pro_name__iexact=pro_name) | Q(catagory__iexact=catagory) | Q(pro_prize__iexact=pro_prize)|Q(pro_discount__iexact=pro_discount))
            print(Listing)
        return render(request,'main/customer-index.html',{'List':Listing,"cart":cart,'listing2':listing2,'cart_count':cart_count,'total':total,'wishlist':wishlist})
               
def public_dashboard_laptops(request):
        
        Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(catagory='Laptops')
        listing2=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(purchasedcount__gte = 5)
        if request .method=="POST" and 'searchbtn' in request.POST:
            print('search')
            search=request.POST.get("search")
            Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(Q(pro_name__icontains=search) | Q(catagory__icontains=search) | Q(pro_prize__icontains=search)|Q(pro_discount__icontains=search))
        elif request.method=="POST" and 'filterbtn' in request.POST:
            print('filter')
            pro_name = request.POST.get("product_name")
            print(pro_name)
            catagory = request.POST.get("category")
            print(catagory)
            pro_prize=request.POST.get("pro_prize  ")
            print(pro_prize)
            pro_discount=request.POST.get("pro_discount")
            print(pro_discount)
            
                    
            Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(Q(pro_name__iexact=pro_name) | Q(catagory__iexact=catagory) | Q(pro_prize__iexact=pro_prize)|Q(pro_discount__iexact=pro_discount))
            print(Listing)
        return render(request,'main/index.html',{'List':Listing,'listing2':listing2})


def public_dashboard_cameras(request):
        
        Listing=ProductModel.objects.filter(catagory='Cameras')
        listing2=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(purchasedcount__gte = 5)
        if request .method=="POST" and 'searchbtn' in request.POST:
            print('search')
            search=request.POST.get("search")
            Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(Q(pro_name__icontains=search) | Q(catagory__icontains=search) | Q(pro_prize__icontains=search)|Q(pro_discount__icontains=search))
        elif request.method=="POST" and 'filterbtn' in request.POST:
            print('filter')
            pro_name = request.POST.get("product_name")
            print(pro_name)
            catagory = request.POST.get("category")
            print(catagory)
            pro_prize=request.POST.get("pro_prize  ")
            print(pro_prize)
            pro_discount=request.POST.get("pro_discount")
            print(pro_discount)
            
                    
            Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(Q(pro_name__iexact=pro_name) | Q(catagory__iexact=catagory) | Q(pro_prize__iexact=pro_prize)|Q(pro_discount__iexact=pro_discount))
            print(Listing)
        return render(request,'main/index.html',{'List':Listing,'listing2':listing2})


def public_dashboard_smartphones(request):
        
        Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(catagory='Smartphones')
        listing2=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(purchasedcount__gte = 5)
        if request .method=="POST" and 'searchbtn' in request.POST:
            print('search')
            search=request.POST.get("search")
            Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(Q(pro_name__icontains=search) | Q(catagory__icontains=search) | Q(pro_prize__icontains=search)|Q(pro_discount__icontains=search))
        elif request.method=="POST" and 'filterbtn' in request.POST:
            print('filter')
            pro_name = request.POST.get("product_name")
            print(pro_name)
            catagory = request.POST.get("category")
            print(catagory)
            pro_prize=request.POST.get("pro_prize  ")
            print(pro_prize)
            pro_discount=request.POST.get("pro_discount")
            print(pro_discount)
            
                    
            Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(Q(pro_name__iexact=pro_name) | Q(catagory__iexact=catagory) | Q(pro_prize__iexact=pro_prize)|Q(pro_discount__iexact=pro_discount))
            print(Listing)
    
        return render(request,'main/index.html',{'List':Listing,'listing2':listing2})

    
def home(request):
    Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').all()
    listing2=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(purchasedcount__gte = 5)
    if request .method=="POST" and 'searchbtn' in request.POST:
        print('search')
        search=request.POST.get("search")
        Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(Q(pro_name__icontains=search) | Q(catagory__icontains=search) | Q(pro_prize__icontains=search)|Q(pro_discount__icontains=search))
    elif request.method=="POST" and 'filterbtn' in request.POST:
        print('filter')
        pro_name = request.POST.get("product_name")
        print(pro_name)
        catagory = request.POST.get("category")
        print(catagory)
        pro_prize=request.POST.get("pro_prize  ")
        print(pro_prize)
        pro_discount=request.POST.get("pro_discount")
        print(pro_discount)
          
                
        Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(Q(pro_name__iexact=pro_name) | Q(catagory__iexact=catagory) | Q(pro_prize__iexact=pro_prize)|Q(pro_discount__iexact=pro_discount))
        print(Listing)
    return render(request,'main/index.html',{'List':Listing,'listing2':listing2})

def cart_details(request):
    customer_id=request.session['user_id']
    if request .method=="POST" and 'searchbtn' in request.POST:
            print('search')
            search=request.POST.get("search")
            Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(Q(pro_name__icontains=search) | Q(catagory__icontains=search) | Q(pro_prize__icontains=search)|Q(pro_discount__icontains=search))
       
    wishlist=ProductUploadModel.objects.filter(product_watchlist=customer_id).count()
    cart_count=CartModel.objects.filter(cart_owner=customer_id).count()
    cart=CartModel.objects.filter(cart_owner=customer_id)
    data2=CartModel.objects.filter(cart_owner=customer_id).aggregate((Sum('cart_product_price')))
    total=data2['cart_product_price__sum']
    print(total)
    data=CartModel.objects.filter(cart_owner=customer_id)
  
    data2=CartModel.objects.filter(cart_owner=customer_id).aggregate(price=(Sum('cart_product_price')))
    print(data2)
    
    # if not data:
    #     return redirect(request.META['HTTP_REFERER'])
    
    return render(request,'main/cart-details.html',{'data':data,'data2':data2,'cart_count':cart_count,'wishlist':wishlist,'total':total,'cart':cart})


def laptops(request):
    
    listing2=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(purchasedcount__gte = 5)[0:4]
    Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(catagory='Laptops')
    if request .method=="POST" and 'searchbtn' in request.POST:
            print('search')
            search=request.POST.get("search")
            Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(Q(pro_name__icontains=search) | Q(catagory__icontains=search) | Q(pro_prize__icontains=search)|Q(pro_discount__icontains=search))
            print(Listing,'abhi')
    return render (request,'main/laptops.html',{'listing':Listing,'listing2':listing2})
def cameras(request):
   
    listing2=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(purchasedcount__gte = 5)[0:4]
    Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(catagory='Cameras')
    if request .method=="POST" and 'searchbtn' in request.POST:
            print('search')
            search=request.POST.get("search")
            Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(Q(pro_name__icontains=search) | Q(catagory__icontains=search) | Q(pro_prize__icontains=search)|Q(pro_discount__icontains=search))
            print(Listing,'abhi')
    return render (request,'main/laptops.html',{'listing':Listing,'listing2':listing2})

def smartphones(request):
  
    listing2=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(purchasedcount__gte = 5)[0:4]
    Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(catagory='Smartphones').all()
    if request .method=="POST" and 'searchbtn' in request.POST:
            print('search')
            search=request.POST.get("search")
            Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(Q(pro_name__icontains=search) | Q(catagory__icontains=search) | Q(pro_prize__icontains=search)|Q(pro_discount__icontains=search))
            print(Listing,'abhi')
    return render (request,'main/laptops.html',{'listing':Listing,'listing2':listing2})
      
def customer_laptops(request):
    user_id=request.session['user_id']
    wishlist=ProductUploadModel.objects.filter(product_watchlist=user_id).count()
    cart_count=CartModel.objects.filter(cart_owner=user_id).count()
    cart=CartModel.objects.filter(cart_owner=user_id)
    data2=CartModel.objects.filter(cart_owner=user_id).aggregate((Sum('cart_product_price')))
    total=data2['cart_product_price__sum']
    print(total)
    listing2=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(purchasedcount__gte = 5)[0:4]
    Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(catagory='Laptops')
    data=ProductUploadModel.objects.filter(product_watchlist=user_id)
    if request .method=="POST" and 'searchbtn' in request.POST:
            print('search')
            search=request.POST.get("search")
            Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(Q(pro_name__icontains=search) | Q(catagory__icontains=search) | Q(pro_prize__icontains=search)|Q(pro_discount__icontains=search))
            print(Listing,'abhi')
    return render (request,'main/customer-laptops.html',{'listing':Listing,'data':data,"cart":cart,'total':total, 'cart_count':cart_count,'wishlist':wishlist,'listing2':listing2})  

def customer_cameras(request):
    customer_id=request.session['user_id']
    wishlist=ProductUploadModel.objects.filter(product_watchlist=customer_id).count()
    cart_count=CartModel.objects.filter(cart_owner=customer_id).count()
    cart=CartModel.objects.filter(cart_owner=customer_id)
    Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(catagory='Cameras')
    data2=CartModel.objects.filter(cart_owner=customer_id).aggregate((Sum('cart_product_price')))
    total=data2['cart_product_price__sum']
    print(total)
    listing2=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(purchasedcount__gte = 5)[0:4]
    if request .method=="POST" and 'searchbtn' in request.POST:
            print('search')
            search=request.POST.get("search")
            Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(Q(pro_name__icontains=search) | Q(catagory__icontains=search) | Q(pro_prize__icontains=search)|Q(pro_discount__icontains=search))
            
    return render (request,'main/customer-laptops.html',{'listing':Listing,"cart":cart,'total':total, 'cart_count':cart_count,'wishlist':wishlist,'listing2':listing2})

def customer_smartphones(request):
    customer_id=request.session['user_id']
    listing2=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(purchasedcount__gte = 5)[0:4]
    wishlist=ProductUploadModel.objects.filter(product_watchlist=customer_id).count()
    cart_count=CartModel.objects.filter(cart_owner=customer_id).count()
    cart=CartModel.objects.filter(cart_owner=customer_id)
    data2=CartModel.objects.filter(cart_owner=customer_id).aggregate((Sum('cart_product_price')))
    total=data2['cart_product_price__sum']
    print(total)
    Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(catagory='Smartphones')
    if request .method=="POST" and 'searchbtn' in request.POST:
            print('search')
            search=request.POST.get("search")
            Listing=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(Q(pro_name__icontains=search) | Q(catagory__icontains=search) | Q(pro_prize__icontains=search)|Q(pro_discount__icontains=search))
            
    return render (request,'main/customer-laptops.html',{'listing':Listing,"cart":cart,'total':total, 'cart_count':cart_count,'wishlist':wishlist,'listing2':listing2})    


def billing(request):
    customer_id=request.session['user_id']
    wishlist=ProductUploadModel.objects.filter(product_watchlist=customer_id).count()
    cart_count=CartModel.objects.filter(cart_owner=customer_id).count()
    cart=CartModel.objects.filter(cart_owner=customer_id)
    data2=CartModel.objects.filter(cart_owner=customer_id).aggregate((Sum('cart_product_price')))
    total=data2['cart_product_price__sum']
    print(total)
    data5=UserDetailsModel.objects.filter(user_id=customer_id)
    data77=UserDetailsModel.objects.get(user_id=customer_id)
    data=CartModel.objects.filter(cart_owner=customer_id)
    data2=CartModel.objects.filter(cart_owner=customer_id).aggregate((Sum('cart_product_price')))
    total=data2['cart_product_price__sum']
    print(total)
    data3=CustomerAddress.objects.filter(customer=customer_id).exists()
    if not data:
        return redirect(request.META['HTTP_REFERER'])
    if data3:
        return redirect('customer_address')
    else:
         if request.method=='POST' and 'searchbtn' in request.POST:
            print('abhi')    
            flat_no = request.POST.get("flatno")
            address = request.POST.get("address")
            city1 = request.POST.get("city")
            print(city1)
            zipcode = request.POST.get("zipcode")
            landmark = request.POST.get("landmark")
            mobile = request.POST.get("tel")
            Typeplace = request.POST.get("place")
            data7=CustomerAddress.objects.create(city=city1,zip_code=zipcode,flat_no=flat_no,address_type=address,contact_no=mobile,landmark=landmark,address_name=Typeplace,customer=data77)
            
            return redirect('customer_address')
    return render (request,'main/billing.html',{ 'exist':data3,'data':data,
                                               'profile':data5,"cart":cart,'total':total, 'cart_count':cart_count,'wishlist':wishlist})
@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            print(payment_id)
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
            # print(payment_id,razorpay_order_id,signature,)
            api=RazorpayClient()
            print(api)
            # verify the payment signature.
            result = api.client.utility.verify_payment_signature(params_dict)
            # print(result)
            if result:
                customer_id=request.session['user_id']
                customer=UserDetailsModel.objects.get(user_id=customer_id)
                
                total2=CartModel.objects.filter(cart_owner=customer).aggregate(Sum('cart_product_price'))
                total=total2["cart_product_price__sum"]
                print(total)

                amount=int(total*100) #(1Rs*100=100paisa)
                print('pay',payment_id)
                print('amot',(type(amount)))
                # amount=2000
                try:
 
                    # capture the payemt
                    print('tryyyyyyyyyyyyyyyy')
                    a=api.client.payment.capture(payment_id, amount)
                    print(a,'gjghgh')
                    print(payment_id)
                    print(amount)
                    return redirect('make_order', order_id=razorpay_order_id,payment_id=payment_id)
                except:
                    
                    # if there is an error while capturing payment.
                    print('abhi')
                    messages.error(request,'Payment Failed!! Please Try Again')
                    return redirect('billing')
                
                    
            else:
 
                # if signature verification fails.
                print('abhi55')
                messages.error(request,'Signature verification Failed!! Please Try Again')
                return redirect('billing')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()
def make_order(request,order_id,payment_id):
    print(order_id)
    customer_id=request.session['user_id']
    customer=UserDetailsModel.objects.get(user_id=customer_id)
    items=CartModel.objects.filter(cart_owner=customer)
    address=CustomerAddress.objects.get(address_id=customer.customer_cart_address)
    landmark=address.landmark
    city=address.city
    zip_code=address.zip_code
    flat_no=address.flat_no
    contact_no=address.contact_no
    address_name=address.address_name
   
    for i in items:
        order_unique_id=order_id
        order_product=i.cart_product
        order_product2=i.cart_product.pro_details
        a=i.cart_product.pro_details.pro_id
        print(a,'abhi155')
        order_product_price=i.cart_product.pro_details.pro_discount
        order_product_qty=i.cart_product_qty
        order_product_amount=i.cart_product_price
        order_product_seller=i.cart_product.seller_id
        order_payment_status='Succesful'
        order_status='Order confirmed'
    
        order_payment_id=payment_id
        
        obj=OrdersModels(order_unique_id=order_unique_id,order_product=order_product,
                        order_product_price=order_product_price,order_product_qty=order_product_qty,
                        order_product_amount=order_product_amount,order_product_seller=order_product_seller,
                        order_payment_status=order_payment_status,order_status=order_status,order_product2=order_product2,
                        order_customer=customer,order_address=address,order_payment_id=order_payment_id,landmark=landmark,city=city,
                        zip_code=zip_code,flat_no=flat_no,contact_no=contact_no,address_name=address_name
                        )
        data=get_object_or_404(ProductModel,pro_id=a)
        a=data.purchasedcount+1
        data.purchasedcount=a
        print(data,'abhi')
        data.save(update_fields=['purchasedcount'])
        obj.save()
        
    for i in items:
        i.delete()
    messages.success(request,'Payment Succesful')
    return redirect('customer_order_placed')    

def customer_address(request):
    user_id=request.session['user_id']
    wishlist=ProductUploadModel.objects.filter(product_watchlist=user_id).count()
    cart_count=CartModel.objects.filter(cart_owner=user_id).count()
    cart=CartModel.objects.filter(cart_owner=user_id)
    data2=CartModel.objects.filter(cart_owner=user_id).aggregate((Sum('cart_product_price')))
    total=data2['cart_product_price__sum']
    print(total)
    Listing=CustomerAddress.objects.filter(customer=user_id)
    count=CustomerAddress.objects.filter(customer=user_id).count()
    user_address=UserDetailsModel.objects.filter(user_id=user_id).values('customer_cart_address').exists()
    data=get_object_or_404(UserDetailsModel,user_id=user_id)
    print(user_address)
    if not  Listing: 
        return redirect('cart') 
    if request.method == 'POST' and  'searchbtn' in request.POST:
        print('abhi55666556')
        user_address=request.POST.get('address')
        data.customer_cart_address=user_address
        if not  user_address:
            messages.success(request,'Please select Address')
            return redirect(request.META['HTTP_REFERER'])
        
        data.save(update_fields=['customer_cart_address'])
        if data:
            return redirect('customer_final_billing')
        else:
            return redirect('customer_address')
         
    
    return render(request,'main/customer-address.html',{'Listing':Listing,'count':count
    ,'cart_count':cart_count,'total':total,'wishlist':wishlist, "cart":cart   })
    
def public_product_details(request,id):
   
    
    Listing=ProductUploadModel.objects.filter(pro_details=id)
    data=ProductModel.objects.filter(product_uploaded_status='uploaded').order_by('-pro_id')[0:4]
  
    data3=FeedbackModel.objects.filter(feedback_product2=id)
    paginator = Paginator(data3, 8)

    page_number =request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    pages = page_obj.paginator.num_pages

    # for i in page_obj:
    #     if id in i.feedback_product2.all():
    #         i.is_watched = True
    #     else:
    #         i.is_watched = False
    
    
    return render (request,'main/product-details-public.html',{'data':Listing,'data1':data,'data3':data3,'products':page_obj,'pages':pages,})
   

def product_details(request,id):
    user_id=request.session['user_id']
    wishlist=ProductUploadModel.objects.filter(product_watchlist=user_id).count()
    cart_count=CartModel.objects.filter(cart_owner=user_id).count()
    cart=CartModel.objects.filter(cart_owner=user_id)
    data2=CartModel.objects.filter(cart_owner=user_id).aggregate((Sum('cart_product_price')))
    total=data2['cart_product_price__sum']
    print(total)
    data2=UserDetailsModel.objects.get(user_id=user_id)
    Listing=ProductUploadModel.objects.filter(pro_details=id)
    data=ProductModel.objects.filter(product_uploaded_status='uploaded').order_by('-pro_id')[0:4]
    feedback_access=OrdersModels.objects.filter(order_customer=user_id).filter(order_product2=id).filter(order_status='Delivered')
    print(feedback_access)
    data3=FeedbackModel.objects.filter(feedback_product2=id)
    paginator = Paginator(data3, 8)

    page_number =request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    pages = page_obj.paginator.num_pages
    if request .method=="POST" and 'searchbtn' in request.POST:
            print('search')
            search=request.POST.get("search")
            data=ProductModel.objects.filter(product_uploaded_status='uploaded').filter(Q(pro_name__icontains=search) | Q(catagory__icontains=search) | Q(pro_prize__icontains=search)|Q(pro_discount__icontains=search))
            

    # for i in page_obj:
    #     if id in i.feedback_product2.all():
    #         i.is_watched = True
    #     else:
    #         i.is_watched = False
    
    
    return render (request,'main/product-details.html',{'data':Listing,'data1':data,'feedback':feedback_access,'data2':data2,'data3':data3,'products':page_obj,'pages':pages,'cart_count':cart_count,'total':total,'wishlist':wishlist, "cart":cart })


      
def new_address_form(request):
    customer_id=request.session['user_id']
    wishlist=ProductUploadModel.objects.filter(product_watchlist=customer_id).count()
    cart_count=CartModel.objects.filter(cart_owner=customer_id).count()
    cart=CartModel.objects.filter(cart_owner=customer_id)
    data2=CartModel.objects.filter(cart_owner=customer_id).aggregate((Sum('cart_product_price')))
    total=data2['cart_product_price__sum']
    print(total)
    data5=UserDetailsModel.objects.filter(user_id=customer_id)
    data77=UserDetailsModel.objects.get(user_id=customer_id)

    if request.method=='POST' and 'searchbtn' in request.POST:
        print('abhi')    
        flat_no = request.POST.get("flatno")
        address = request.POST.get("address")
        city1 = request.POST.get("city")
        print(city1)
        zipcode = request.POST.get("zipcode")
        landmark = request.POST.get("landmark")
        mobile = request.POST.get("tel")
        Typeplace = request.POST.get("place")
        data7=CustomerAddress.objects.create(city=city1,zip_code=zipcode,flat_no=flat_no,address_type=address,contact_no=mobile,landmark=landmark,address_name=Typeplace,customer=data77)
        messages.success(request,'Sucessfully Uploaded Address')
        return redirect('customer_address')
    
    return render (request,'main/address-new-add-form.html',{'profile':data5,'cart_count':cart_count,'total':total,'wishlist':wishlist, "cart":cart })   

def addtocart(request,id,method_redirect):
    customer_id=request.session['user_id']
    customer=UserDetailsModel.objects.get(user_id=customer_id)
    data=ProductUploadModel.objects.get(pro_details=id)
    b=data.product_id

    
    a=data.pro_details.pro_discount
    data2=CartModel.objects.filter(cart_owner=customer_id).filter(cart_product=b).exists()
    data3=CartModel.objects.filter(cart_owner=customer_id).filter(cart_product=b)
    for j in data3:
        print(j.cart_product_qty)
    
    if data2 and j.cart_product_qty == 4 :
        messages.info(request,'Maximum No Of product 4 Is limit')
    elif data2 and j.cart_product_qty <= 4 : 
        # data3=CartModel.objects.filter(cart_owner=customer_id).filter(cart_product=b).update(cart_product_qty=F('cart_product_qty')+1)
        data4=get_object_or_404(CartModel,cart_owner=customer_id,cart_product=b)
        b=data4.cart_product_qty+1
        c=b*a
        print(c)
        
        data4.cart_product_qty=b
        
        data4.cart_product_price=c
        
        data4.save(update_fields=['cart_product_qty','cart_product_price'])
        messages.success(request,'Succesfully added to cart')

   
    else:    
         data1=CartModel.objects.create(cart_owner=customer,cart_product=data,cart_product_price=a)
         messages.success(request,'Succesfully added to cart')
    if method_redirect=='index':   
       return redirect('index')
    elif method_redirect == 'view':
            return redirect('product-details',id=id)
       
    elif method_redirect=='wishlist':
        return redirect('wishlist')
    else:
        return redirect('customer_smartphones')


def buynow(request,id):
    customer_id=request.session['user_id']
    customer=UserDetailsModel.objects.get(user_id=customer_id)
    data=ProductUploadModel.objects.get(pro_details=id)
    b=data.product_id

    
    a=data.pro_details.pro_discount
    data2=CartModel.objects.filter(cart_owner=customer_id).filter(cart_product=b).exists()
    data3=CartModel.objects.filter(cart_owner=customer_id).filter(cart_product=b)
    
    for j in data3:
        print(j.cart_product_qty)
    
    if data2 and j.cart_product_qty == 4 :
        messages.info(request,'Maximum No Of product 4 Is limit')
    elif data2 and j.cart_product_qty <= 4 :
        product_details=get_object_or_404(CartModel,cart_owner=customer_id,cart_product=b) 
        # data3=CartModel.objects.filter(cart_owner=customer_id).filter(cart_product=b).update(cart_product_qty=F('cart_product_qty')+1)
        product_details.cart_product_qty=product_details.cart_product_qty+1
        b=int(a)*product_details.cart_product_qty
        print(b,'abhibuy')
        product_details.cart_product_price=b
        product_details.save(update_fields=['cart_product_price','cart_product_qty'])
   
    else:    
        data1=CartModel.objects.create(cart_owner=customer,cart_product=data,cart_product_price=a)
       
    return redirect('billing')







def wishlist(request):
    customer_id=request.session['user_id']
    wishlist=ProductUploadModel.objects.filter(product_watchlist=customer_id).count()
    cart_count=CartModel.objects.filter(cart_owner=customer_id).count()
    cart=CartModel.objects.filter(cart_owner=customer_id)
    data2=CartModel.objects.filter(cart_owner=customer_id).aggregate((Sum('cart_product_price')))
    total=data2['cart_product_price__sum']
    print(total)
    # customer=UserDetailsModel.objects.get(user_id=customer_id)
    product_object = ProductUploadModel.objects.filter(product_watchlist=customer_id)
    print(product_object)
    if not product_object:
        messages.success(request,'please select your favourite products')
        
    if request .method=="POST" and 'searchbtn' in request.POST:
            print('search')
            search=request.POST.get("search")
            product_object=ProductUploadModel.objects.filter(product_watchlist=customer_id).filter(Q(pro_details__pro_name__icontains=search) | Q(pro_details__catagory__icontains=search) | Q(pro_details__pro_prize__icontains=search)|Q(pro_details__pro_discount__icontains=search))
                
    
    return render(request,'main/wishlist.html',{'product_object':product_object,'cart_count':cart_count,'total':total,'wishlist':wishlist, "cart":cart }) 

def wishlist_action(request,id,redirect_method):
    print(redirect_method,'sdfghj')
    customer_id=request.session['user_id']
    customer=UserDetailsModel.objects.get(user_id=customer_id)
    product_object = ProductUploadModel.objects.get(pro_details=id)
    if customer in product_object.product_watchlist.all():
        product_object.product_watchlist.remove(customer)
        messages.info(request,'Product removed from watchlist')
    else:
        product_object.product_watchlist.add(customer)
        messages.success(request,'Product Added to watchlist')
    
        # if redirect_method == "wishlist" :
        #     return redirect('wishlist', id=id)
    if redirect_method == 'wishlist':
        return redirect('wishlist')
    elif redirect_method == 'product-details':
        return redirect('product-details',id=id)
    else:
        return redirect('index')
    
def cart_product_delete(request,id,redirect_method):
    customer_id=request.session['user_id']
    CartModel.objects.filter(cart_owner=customer_id).filter(cart_id=id).delete()
    data=CartModel.objects.filter(cart_owner=customer_id).filter(cart_id=id)
    
    
    if redirect_method == None:
        messages.success(request,'Succesfully deleted From cart')
        return redirect('index') 
    
    elif  redirect_method == 'cart':
          messages.success(request,'Succesfully deleted From cart')

          return redirect('cart')
        
    elif redirect_method =='index':
        messages.success(request,'Succesfully deleted From cart')   
        return redirect('index')
   
       
    elif redirect_method =='wishlist':
        messages.success(request,'Succesfully deleted From cart') 
        return redirect('wishlist')
    
    elif redirect_method =='products':
        messages.success(request,'Succesfully deleted From cart') 
        return redirect('customer_smartphones')
    else:
        messages.success(request,'Succesfully deleted From cart')
        return redirect('index')    
          
    # elif redirect_method == 'cart':    
    #   return redirect('cart')
    
    
def cart_product_update(request,id):
    if request.method == 'POST':
       print('affff')
       customer_id=request.session['user_id']
       data2=get_object_or_404(CartModel,cart_owner=customer_id,cart_id=id)
       data=CartModel.objects.filter(cart_owner=customer_id).filter(cart_id=id)
       for i in data:
           a=(i.cart_product.pro_details.pro_discount)
       update_qnty=request.POST.get('update_quantity') 
       b=a*int(update_qnty)
       print(b)
       data2.cart_product_qty=update_qnty
       data2.cart_product_price=b
       data2.save(update_fields=['cart_product_qty','cart_product_price'])
       messages.success(request,'Succesfully Updated ')
     
    return redirect('cart') 
    
def address_delete(request,id,id2):
    CustomerAddress.objects.filter(address_id=id).filter(customer=id2).delete()
   
    
    return redirect('customer_address')  

   
def customer_order_placed(request):
    customer_id=request.session['user_id']
    wishlist=ProductUploadModel.objects.filter(product_watchlist=customer_id).count()
    cart_count=CartModel.objects.filter(cart_owner=customer_id).count()
    cart=CartModel.objects.filter(cart_owner=customer_id)
    data2=CartModel.objects.filter(cart_owner=customer_id).aggregate((Sum('cart_product_price')))
    total=data2['cart_product_price__sum']
    print(total)
    data=OrdersModels.objects.filter(order_customer=customer_id)
    if request .method=="POST" and 'searchbtn' in request.POST:
            print('search')
            search=request.POST.get("search")
            data=OrdersModels.objects.filter(Q(order_product2__pro_name__icontains=search) | Q(order_product2__catagory__icontains=search) | Q(order_product2__pro_prize__icontains=search)|Q(order_product2__pro_discount__icontains=search))
            
   
    return render(request,'main/customer-order-placed.html',{'data':data,'cart_count':cart_count,'total':total,'wishlist':wishlist, "cart":cart })

def customer_order_placed_details(request,id):
    print(id,'abhi')
    customer_id=request.session['user_id']
    wishlist=ProductUploadModel.objects.filter(product_watchlist=customer_id).count()
    cart_count=CartModel.objects.filter(cart_owner=customer_id).count()
    cart=CartModel.objects.filter(cart_owner=customer_id)
    data2=CartModel.objects.filter(cart_owner=customer_id).aggregate((Sum('cart_product_price')))
    total=data2['cart_product_price__sum']
    print(total)
    customer=UserDetailsModel.objects.get(user_id=customer_id)
    order=OrdersModels.objects.filter(order_id=id)

   
    return render(request,'main/customer-order-placed-details.html',{'order':order,'cart_count':cart_count,'total':total,'wishlist':wishlist, "cart":cart })
                                      
                                            
                                            
                                            
                                            
                                            
def customer_feedback(request,id):
    print(id)
    user_id=request.session['user_id']
    
    data=FeedbackModel.objects.filter(feedback_product2=id).filter(feedback_customer_id=user_id).exists()
    
    if data:
        return redirect(request.META['HTTP_REFERER'])
    else:
        data55=get_object_or_404(ProductModel,pro_id=id) 
        data66=FeedbackModel.objects.filter(feedback_product2=id).aggregate(a=Avg('feedback_rating'))
        avg=data66['a']
        avgtotal=avg
   
        a=data55.product_review
        print(avgtotal)
        if request.method=='POST' and 'searchbtn' in request.POST:
            print('abhi','post')
            feedback_message=request.POST['feedback']
            feedback_rating=request.POST['rating']
            
            #classifier to decide sentimet of user from text data
            analysis = TextBlob(feedback_message)
            
            sentiment=''
            if analysis.polarity>0.2:
                sentiment='Positive'
            elif analysis.polarity<-0.2: 
                sentiment='Negative'
            else:
                sentiment='Neutral'

            
            customer_id=request.session['user_id']
            customer=UserDetailsModel.objects.get(user_id=customer_id)
            product=ProductUploadModel.objects.get(pro_details=id)
            feedback_product2=ProductModel.objects.get(pro_id=id)
            print(feedback_message,sentiment)
            # data55.product_review=avgtotal
         
               
               
            obj=FeedbackModel(feedback_message=feedback_message,feedback_sentiment=sentiment,feedback_customer=customer,
                                feedback_product=product,feedback_seller=product.seller_id,feedback_rating=feedback_rating,feedback_product2=feedback_product2)
         
            obj.save()
            if avg== None:
                data55.product_review=feedback_rating
            else:
                 data55.product_review=avgtotal  
            data55.save(update_fields=['product_review'])
            data56=ProductModel.objects.filter(pro_id=id).update(F('user_review_count')+1)

            messages.success(request,'Review Submitted Successfully')
            return redirect('product-details',id=id)                                            
        
def customer_final_billing(request):
    
    customer_id=request.session['user_id']
    wishlist=ProductUploadModel.objects.filter(product_watchlist=customer_id).count()
    cart_count=CartModel.objects.filter(cart_owner=customer_id).count()
    cart=CartModel.objects.filter(cart_owner=customer_id)
    data2=CartModel.objects.filter(cart_owner=customer_id).aggregate((Sum('cart_product_price')))
    total=data2['cart_product_price__sum']
    print(total)
    data5=UserDetailsModel.objects.filter(user_id=customer_id)
    data6=UserDetailsModel.objects.filter(user_id=customer_id).count()
    data77=UserDetailsModel.objects.get(user_id=customer_id)
    data=CartModel.objects.filter(cart_owner=customer_id)
    data2=CartModel.objects.filter(cart_owner=customer_id).aggregate((Sum('cart_product_price')))
    total=data2['cart_product_price__sum']
    print(total)
    amount=int(total)*100 #20Rs(20*100paisa)
    print(amount)
    currency='INR'
    api = RazorpayClient()
    # Create a Razorpay Order
    razorpay_order = api.create_order(amount)

    razorpay_order_id = razorpay_order['id']
    
    callback_url = 'paymenthandler/'
    return render(request,'main/customer-billing-final.html',{ 'data5':data5,'total':total,
        'razorpay_order_id':razorpay_order_id,
        'razorpay_merchant_key':settings.RAZOR_KEY_ID,
        'amount':amount,
        'currency':currency,
        'callback_url':callback_url,'data':data,'count':data6,'cart_count':cart_count,'wishlist':wishlist, "cart":cart })    





     
 
        
def logout(request):
    del request.session['user_id'] 
    return redirect('home')   

def user_login(request):
          if request.method == "POST":
           email = request.POST.get("email")  
           password  = request.POST.get("psw") 
           try:
             check = UserDetailsModel.objects.get(email=email,password=password) 
             request.session['user_id'] = check.user_id 
             messages.success(request,'login succesful') 
             return redirect('index')  
           except: 
            messages.error(request,'login succesful')
          return render(request,'user/user-login.html')

def user_signup(request):
          if request.method == 'POST' and 'photo' in request.FILES:
           name=request.POST.get('uname') 
           email=request.POST.get('Email') 
           phno=request.POST.get('Phonenumber') 
           profile_photo=request.FILES['photo'] 
           password=request.POST.get('psw') 
           data=UserDetailsModel.objects.create(name=name,email=email,phno=phno,profile_photo=profile_photo,password=password)
           if data:
               messages.success(request,' succesfully Registered')         
          return render(request,'user/user-signup.html') 
    
def customer_profile(request):
    profile=request.session['user_id']
    data=UserDetailsModel.objects.filter(user_id=profile)
    data2=get_object_or_404(UserDetailsModel,user_id=profile)
    if request.method=='POST':
        password=request.POST.get('password')
        data2.password=password
        data2.save(update_fields=['password'])
        if data2:
            messages.success(request,' succesfully Updated')         
  
    return render(request,'main/customer-profile.html',{'data':data})    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
       






         