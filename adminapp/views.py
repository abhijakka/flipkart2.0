from email import message
import django
from django.shortcuts import redirect, render,get_object_or_404
from django.core.mail import EmailMultiAlternatives
from filpkartproject.settings import DEFAULT_FROM_EMAIL
from sellerapp.models import *
from django.http import HttpResponse
from userapp.models import *
from mainapp.models import *
from django.contrib import messages
from django.db.models import Sum,Avg

# Create your views here.
def admin_login(request):
          if request.method == "POST":
                    name = request.POST.get('uname')
                    password = request.POST.get('psw')
                    if name =='admin' and password == 'admin':
                         messages.success(request,'login success')     
                         return redirect('admin-index')  
                    else:
                       messages.error(request,'invalid login')         
          return render(request,'admin/admin-login.html')

def admin_index(request):
          seller_count = SellerDetailsModel.objects.count()
          user_count = UserDetailsModel.objects.count()
          product_count = ProductModel.objects.count()
          orders =OrdersModels.objects.count()
          ordertotal=OrdersModels.objects.aggregate(total=Sum('order_product_amount'))
          quantity=OrdersModels.objects.aggregate(quantity=Sum('order_product_qty'))

          return render(request,'admin/admin-index.html',{'seller_count':seller_count,'user_count':user_count,'pro_count':product_count,'order_count':orders,"total":ordertotal,'quantity':quantity})

def admin_feedback(request):
     data=FeedbackModel.objects.all()
     return render(request,'admin/admin-feedback.html',{'data':data})

def admin_seller_edit(request):
          return render(request,'admin/admin-seller-edit.html')

def admin_view_seller_profile(request,id):
          obj =get_object_or_404(SellerDetailsModel,seller_id=id)
          return render(request,'admin/admin-seller-profile-view.html',{'profile':obj})
def accept_seller(request,id):
        accept = get_object_or_404(SellerDetailsModel,seller_id=id)
        accept.status = 'Accepted'
        accept.save(update_fields=['status']) 
        accept.save()   
        html_content = "<br/><p>FILPKART Want to inform you that Your Online seller card is <b>accepted</b> by team of Filpkart as it is issued by a Filpkart-2.0.\
           <br>Thanks for your Resgistration</p>"
        from_mail = DEFAULT_FROM_EMAIL
        to_mail = [accept.email ]
        # if send_mail(subject,message,from_mail,to_mail):
        msg = EmailMultiAlternatives("Your Filpkart seller Registration Status ", html_content, from_mail, to_mail)
        msg.attach_alternative(html_content, "text/html")
        try:
          if msg.send():
               print("Sent")
               return redirect('admin-view-main-seller')
        except: 
             return redirect('admin-view-main-seller')      
        return redirect('admin-view-main-seller')
    
def reject_seller(request,id):
        reject = get_object_or_404(SellerDetailsModel,seller_id=id)
        reject.status = 'Rejected'
        reject.save(update_fields=['status']) 
        reject.save()
          #email meassage
        html_content = "<br/><p>FILPKART Want to inform you that Your Online seller card is <b>Rejected</b> by team of Filpkart as it is issued by a Filpkart-2.0.\
           So better luck next time.<br>Thanks for your Resgistration</p>"
        from_mail = DEFAULT_FROM_EMAIL
        to_mail = [reject.email ]
        # if send_mail(subject,message,from_mail,to_mail):
        msg = EmailMultiAlternatives("Your Filpkart seller Registration Status ", html_content, from_mail, to_mail)
        msg.attach_alternative(html_content, "text/html")
        try:
          if msg.send():
               print("Sent")
               return redirect('admin-view-main-seller')
        except: 
             return redirect('admin-view-main-seller')
        return redirect('admin-view-main-seller')    

def admin_View_buyers(request):
          buyers = ProductModel.objects.all()
          return render(request,'admin/admin-view-buyer.html',{'buyer':buyers})

def admin_view_main_seller(request):
          seller_details = SellerDetailsModel.objects.all()
          return render(request,'admin/admin-view-main-seller.html',{'seller_details':seller_details})

def admin_view_products(request):
          product = ProductModel.objects.all()
          return render(request,'admin/admin-view-products.html',{'product':product})

def admin_logout(request):
          return render(request,'admin/admin-logout.html')

