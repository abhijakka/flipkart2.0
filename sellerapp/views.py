from ast import Global
from glob import glob
from itertools import product
from django.shortcuts import get_object_or_404, redirect, render
from sellerapp.models import *
from mainapp.models import *
from django.contrib import messages
import statistics
# Create your views here.
def seller_dashboard(request):
     seller_id = request.session['seller_id']
     product = ProductModel.objects.filter(seller_id=seller_id).count()
     orders =OrdersModels.objects.filter(order_product_seller=seller_id).count()
     feedback=FeedbackModel.objects.filter(feedback_seller=seller_id).count()
     return render(request,'seller/seller-dashboard.html',{'product_count':product,'order_count':orders,'feedback_count':feedback})

def seller_add_products(request):
          seller_id = request.session['seller_id']
          data = SellerDetailsModel.objects.get(seller_id=seller_id)
          print(data)
          seller_name=data.own_name
          if request.method == 'POST' and  'image' in request.FILES :
               catagory = request.POST.get('category')
               pro_name = request.POST.get('product_name')
               model_no = request.POST.get('model_no')
               pro_prize = request.POST.get('pro_prize')
               pro_discount = request.POST.get('pro_discount')
               pro_image = request.FILES['image']
             
               description = request.POST.get('description')
               a=int(pro_discount)/int(pro_prize)*100
               # c=(float(a))
               b=(round(a)-100)
               # print(b,'abhi')
               data2=ProductModel.objects.create(seller_id=data,catagory=catagory,pro_name=pro_name,
                                           model_no=model_no,pro_prize=pro_prize,pro_image=pro_image,description=description,
                                           seller_name=seller_name,pro_discount=pro_discount,discount_percentage=b)
               if data2:
                    messages.success(request,"Your products is Uploaded")
               messages.success(request,"please upload images is mandatory else your product is not Uploaded")  
               return redirect('seller-view-products')
               
          return render(request,'seller/seller-add-products.html')
             
def seller_edit_products(request,id):
          edit_pro = ProductModel.objects.filter(pro_id=id)
          obj = get_object_or_404(ProductModel,pro_id=id)
          if request.method == 'POST':
               product_name = request.POST.get('pro_name')
               model_no = request.POST.get('model_no')
               pro_prize = request.POST.get('pro_prize')
               description = request.POST.get('description')
                
               obj.pro_name = product_name
               obj.model_no = model_no
               obj.pro_prize = pro_prize
               obj.description = description
               obj.save()
               messages.success(request,"Your product is sucessfully updated") 
               return redirect('seller-view-products')
               
          return render(request,'seller/seller-edit-product.html',{'edit_pro':edit_pro})

def seller_upload(request,id,id1):
          seller_id = request.session['seller_id']
          seller_details=SellerDetailsModel.objects.get(seller_id=seller_id)
          pro_details = ProductModel.objects.get(pro_id=id)
          a=pro_details.pro_id
            
          seller_pro = ProductModel.objects.filter(pro_id=id).filter(seller_id=id1)
          pro_details = ProductModel.objects.get(pro_id=id)
          if   request.method == 'POST' or request.FILES.get('multi_images') or request.FILES.get('image2') or request.FILES.get('image3') or request.FILES.get('image4') or request.FILES.get('image5'): 
                    product_name = request.POST.get('product_name')
                    product_images1 = request.FILES.get('multi_images')
                    product_images2 = request.FILES.get('image2')  
                    product_images3 = request.FILES.get('image3') 
                    product_images4 = request.FILES.get('image4')
                    product_images5 = request.FILES.get('image5')
                    if ProductUploadModel.objects.filter(product_name=product_name).exists():
                         i = get_object_or_404(ProductUploadModel,pro_details_id=id)
                         # i.product_name=product_name
                         # i.product_images1=product_images1 
                         # i.product_images2=product_images2
                         # i.product_images3=product_images3
                         # i.product_images4=product_images4
                         # i.product_images5=product_images5
                        
                         # i.save(update_fields=['product_name','product_images1','product_images2','product_images3','product_images4','product_images5'])            
                         if not request.FILES.get('multi_images'):
                                   i.product_name=product_name
                                   i.save(update_fields=['product_name'])
                                   print('abhi1')
                                   
                                   if i:
                                             messages.success(request,"Your images is Updated")       
                                   else:
                                        pass
                              
                              
                         if request.FILES.get('multi_images'):
                                   product_images1=request.FILES.get('multi_images')
                                   i.product_images1=product_images1
                                   i.save(update_fields=['product_images1'])
                                   i.save()
                                   print('ffff')
                                   if i:
                                             messages.success(request,"Your images is Updated")       
                                   else:
                                        pass
                         elif request.FILES.get('image2'):
                                   
                                   product_images2=request.FILES.get('image2')
                                   
                                   i.product_images2=product_images2
                                   i.save(update_fields=['product_images2'])
                                   i.save()
                                   print('abhi2')
                                   if i:
                                             messages.success(request,"Your images is Updated")       
                                   else:
                                        pass 
                         elif   request.FILES.get('image3'):
                                   
                                   product_images3 = request.FILES.get('image3')
                                   
                                   i.product_images3=product_images3
                                   i.save(update_fields=['product_images3'])
                                   i.save()
                                   print('abhi3')
                                   if i:
                                             messages.success(request,"Your images is Updated")       
                                   else:
                                        pass  
                         elif request.FILES.get('image4'):
                                   
                                   
                                   product_images4 = request.FILES.get('image4')
                                   
                                   i.product_images4=product_images4
                                   i.save(update_fields=['product_images4'])
                                   i.save()
                                   print('abhi4')
                                   if i:
                                             messages.success(request,"Your images is Updated")       
                                   else:
                                        pass
                         elif  request.FILES.get('image5'):
                                   
                                   product_images5 = request.FILES.get('image5')
                                   
                                   i.product_images5=product_images5
                                   i.save(update_fields=['product_images5'])
                                   i.save()
                                   print('abhi5')
                                   if i:
                                             messages.success(request,"Your images is Updated")       
                                   else:
                                        pass  
                         elif  request.FILES.get('image2') and request.FILES.get('multi_images'):
                                   
                                   product_images2 = request.FILES.get('image2')
                                   product_images1 = request.FILES.get('multi_images')
                                   i.product_images1=product_images1
                                   i.product_images2=product_images2
                                   i.save(update_fields=['product_images1','product_images2'])
                                   i.save()
                                   print('abhi5')
                                   if i:
                                             messages.success(request,"Your images is Updated")       
                                   else:
                                        pass 
                         elif  request.FILES.get('image2') and request.FILES.get('multi_images') and request.FILES.get('image3'):
                                   
                                   product_images2 = request.FILES.get('image2')
                                   product_images3 = request.FILES.get('image3')
                                   product_images1 = request.FILES.get('multi_images')
                                   i.product_images1=product_images1
                                   i.product_images2=product_images2
                                   i.product_images3=product_images3
                                   i.save(update_fields=['product_images1','product_images2','product_images3'])
                                   i.save()
                                   print('abhi5')
                                   if i:
                                             messages.success(request,"Your images is Updated")       
                                   else:
                                        pass 
                         elif  request.FILES.get('image2') and request.FILES.get('multi_images') and request.FILES.get('image3') and request.FILES.get('image4'):
                                   product_images1 = request.FILES.get('multi_images')
                                   product_images2 = request.FILES.get('image2')
                                   product_images3 = request.FILES.get('image3')
                                   product_images4 = request.FILES.get('image4')
                                   
                                   i.product_images1=product_images1
                                   i.product_images2=product_images2
                                   i.product_images3=product_images3
                                   i.product_images4=product_images4
                                   i.save(update_fields=['product_images1','product_images2','product_images3','product_images4'])
                                   i.save()
                                   print('abhi5')
                                   if i:
                                             messages.success(request,"Your images is Updated")       
                                   else:
                                        pass  
                         elif  request.FILES.get('image2') and request.FILES.get('multi_images') and request.FILES.get('image3') and request.FILES.get('image4') and request.FILES.get('image5'):
                                   
                                   product_images2 = request.FILES.get('image2')
                                   product_images3 = request.FILES.get('image3')
                                   product_images4 = request.FILES.get('image4')
                                   product_images5 = request.FILES.get('image5')
                                   product_images1 = request.FILES.get('multi_images')
                                   i.product_images1=product_images1
                                   i.product_images2=product_images2
                                   i.product_images3=product_images3
                                   i.product_images4=product_images4
                                   i.product_images5=product_images5
                                   i.save(update_fields=['product_images1','product_images2','product_images3','product_images4','product_images5'])
                                   i.save()
                                   print('abhi5')
                                   if i:
                                        messages.success(request,"Your images is Updated")       
                                   else:
                                        pass                                                                                   
                    else:
             
                          ProductUploadModel.objects.create(product_name=product_name,
                                                       product_images1=product_images1,
                                                       product_images2=product_images2,pro_details=pro_details
                                                       ,product_images3=product_images3,product_images4=product_images4,product_images5=product_images5,seller_id=seller_details) 
                          data55=get_object_or_404(ProductModel,pro_id=id)
                          data55.product_uploaded_status='uploaded'
                          data55.save(update_fields=['product_uploaded_status'])
                          messages.success(request,"Your images is Updated")  

          
                      
 
             
   
    
                
          
          return render(request,'seller/seller-upload.html', {'seller_pro':seller_pro})


def seller_upload1(request,id,id1):
     pro_details = ProductModel.objects.get(pro_id=id)
     a=pro_details.pro_id
          
     seller_pro = ProductModel.objects.filter(pro_id=id).filter(seller_id=id1)
     pro_details = ProductModel.objects.get(pro_id=id)
     
     return render(request,'seller/seller-upload-modify.html',{'seller_pro':seller_pro})
     
def seller_view_feedback(request):
     seller = request.session['seller_id']
     data=FeedbackModel.objects.filter(feedback_seller=seller)
     for i in data:
         print(i.feedback_customer.name, )
     
     return render(request,'seller/seller-view-feedback.html',{'data':data})

def seller_view_main_products(request,id):
          
     Listing=ProductUploadModel.objects.filter(pro_details=id)
     
    
     data=ProductModel.objects.order_by('-pro_id')[0:4]
     data3=FeedbackModel.objects.filter(feedback_product2=id)    
          
     return render(request,'seller/seller-view-main-products.html',{'data':Listing,'data1':data,'data3':data3})

def seller_view_orders(request):
     seller = request.session['seller_id']
     data=OrdersModels.objects.filter(order_product_seller=seller)
    
   
     return render(request,'seller/seller-view-orders.html',{'data':data})
def seller_product_update_delivery(request,id):
     data=get_object_or_404(OrdersModels,order_id=id)
     if request.method=='POST':
          update_order=request.POST.get('update')
          data.order_status=update_order
          data.save(update_fields=['order_status'])
         
     return redirect('seller-view-orders')

def seller_view_products(request):
          seller = request.session['seller_id']
          
          products = ProductModel.objects.filter(seller_id=seller)
          for i in products:
               a=(i.pro_id)
               print(a)
               
          
          
          check=ProductUploadModel.objects.all()
          for i in check:
               a=i.pro_details
               print(a)
          
          print(check)
    
          if products.count() == 0:  
              messages.info(request,'No Products added')
          else:
               pass     
          return render(request,'seller/seller-view-products.html',{'products':products,'check':check})

def seller_login(request):
          if request.method == 'POST':
                email = request.POST.get('email')
                password = request.POST.get('psw')
                try:
                     check = SellerDetailsModel.objects.get(email=email,password=password)  
                     request.session['seller_id']=check.seller_id 
                      
                     status = check.status
                     if status =='Accepted':
                         message=messages.success(request,'login success')
                         return redirect('seller-dashboard') 
                     elif status =='Rejected' : 
                         message=messages.error(request,'Your request is Rejected so you cannot login')  
                     elif status == 'pending':
                         message=messages.info(request,'Your request is Pending so cannot login')      
                except:
                     messages.warning(request,'invalid login')              
          return render(request,'seller/seller-login.html')

def seller_signup(request):
          if request.method == "POST" and request.FILES['pancard'] and request.FILES['logo'] and  request.FILES['addressproof']:
                    com_name = request.POST.get('company_name')
                    own_name = request.POST.get('own_name')
                    phno = request.POST.get('phone')
                    email = request.POST.get('email')
                    pancard = request.FILES['pancard']   
                    com_logo = request.FILES['logo']
                    address_proof = request.FILES['addressproof']
                    address = request.POST.get('address')
                    password = request.POST.get('password')
                    SellerDetailsModel.objects.create(com_name=com_name,own_name=own_name,phno=phno,email=email,pancard=pancard,
                    com_logo=com_logo,address_proof=address_proof,address=address,password=password)
          return render(request,'seller/seller-signup.html')
     
     
def delete_pro(request,id):
       d=ProductModel.objects.filter(pro_id = id)
       d.delete()   
       return redirect('seller-view-products')  
              
               

