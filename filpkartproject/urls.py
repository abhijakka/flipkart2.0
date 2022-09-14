"""filpkartproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name   
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from mainapp import views as main_views
from sellerapp import views as seller_views
from adminapp import views as admin_views
from userapp import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main_views.home,name='home'),
    path('index',main_views.customer_dashboard,name='index'),
    path('logout',main_views.logout,name='logout'),
    path('cart',main_views.cart_details,name='cart'),
    path('cart-details/<int:id>/<str:method_redirect>',main_views.addtocart,name='cart-details'),
    path('billing',main_views.billing,name='billing'),
    path('product-details/<int:id>',main_views.product_details,name='product-details'),
    path('public-product-details/<int:id>',main_views.public_product_details,name='public-product-details'),
    path('customer-laptops',main_views.customer_laptops,name='customer_laptops'),
    path('customer-smartphones',main_views.customer_smartphones,name='customer_smartphones'),
    path('customer-cameras',main_views.customer_cameras,name='customer_cameras'),
    path('laptops',main_views.laptops,name='laptops'),
    path('cameras',main_views.cameras,name='cameras'),
    path('smartphones',main_views.smartphones,name='smartphones'),
    path('public_dashboard_laptops',main_views.public_dashboard_laptops,name='public_dashboard_laptops'),
    path('public_dashboard_cameras',main_views.public_dashboard_cameras,name='public_dashboard_cameras'),
    path('public_dashboard_smartphones',main_views.public_dashboard_smartphones,name='public_dashboard_smartphones'),
    path('laptops_customer_dashboard',main_views.laptops_customer_dashboard,name='laptops_customer_dashboard'),
    path('customer_dashboard_smartphone',main_views.customer_dashboard_smartphone,name='customer_dashboard_smartphone'),
    path('customer_dashboard_cameras',main_views.customer_dashboard_cameras,name='customer_dashboard_cameras'),
    path('wishlist',main_views.wishlist,name='wishlist'),
    path('customer_profile',main_views.customer_profile,name='customer_profile'),
    path('wishlist-action/<int:id>/<str:redirect_method>',main_views.wishlist_action,name='wishlist_action'),
    path('cart-product-delete/<int:id>/<str:redirect_method>',main_views.cart_product_delete,name='cart_product_delete'),
  

    path('cart_product_update/<int:id>',main_views.cart_product_update,name='cart_product_update'),
    path('address-delete/<int:id>/<int:id2>',main_views.address_delete,name='address_delete'),
    path('paymenthandler/', main_views.paymenthandler, name='paymenthandler'),
    path('customer-address', main_views.customer_address, name='customer_address'),
    path('new-address', main_views.new_address_form, name='new_address_form'),
    path('customer-order-placed', main_views.customer_order_placed, name='customer_order_placed'),
    path('customer-order-placed-details/<int:id>', main_views.customer_order_placed_details, name='customer_order_placed_details'),
    path('customer-final-billing', main_views.customer_final_billing, name='customer_final_billing'),
    path('make-order/<str:order_id>/<str:payment_id>',main_views.make_order,name='make_order'),
    path('customer-feedback/<int:id>', main_views.customer_feedback, name='customer_feedback'),
    path('buy-now/<int:id>', main_views.buynow, name='buynow'),
    # path('details',main_views.details,name='details'),
    # path('blank',main_views.blank,name='blank'),
    # seller paths
    path('seller-dashboard',seller_views.seller_dashboard,name='seller-dashboard'),
    path('seller-add-products',seller_views.seller_add_products,name='seller-add-products'),
    path('seller-edit-products/<int:id>/',seller_views.seller_edit_products,name='seller-edit-products'),
    path('seller-upload/<int:id>/<int:id1>/',seller_views.seller_upload,name='seller-upload'),
    path('seller-upload1/<int:id>/<int:id1>/',seller_views.seller_upload1,name='seller-upload1'),

    path('seller-view-feedback',seller_views.seller_view_feedback,name='seller-view-feedback'),
    path('seller-view-main-products/<int:id>/',seller_views.seller_view_main_products,name='seller-view-main-products'),
    path('seller-view-orders',seller_views.seller_view_orders,name='seller-view-orders'),
    path('seller-added-products',seller_views.seller_view_products,name='seller-view-products'),
    path('seller-login',seller_views.seller_login,name='seller-login'),
    path('seller-signup',seller_views.seller_signup,name='seller-signup'),
    path('del-product/<int:id>/',seller_views.delete_pro,name='del-product'),
    path('seller_product_update_deliveryt/<int:id>/',seller_views.seller_product_update_delivery,name='seller_product_update_delivery'),
    # admin paths
    path('admin-login',admin_views.admin_login,name='admin-login'),
    path('admin-index',admin_views.admin_index,name='admin-index'),
    path('admin-feedback',admin_views.admin_feedback,name='admin-feedback'),
    path('admin-seller-edit',admin_views.admin_seller_edit,name='admin-seller-edit'),
    path('admin-view-seller-profile',admin_views.admin_view_seller_profile,name='admin'),

    path('admin-view-seller-profile/<int:id>/',admin_views.admin_view_seller_profile,name='admin-view-seller-profile'),
    path('admin-View-buyers',admin_views.admin_View_buyers,name='admin-View-buyers'),
    path('admin-view-main-seller',admin_views.admin_view_main_seller,name='admin-view-main-seller'),
    path('admin-view-products',admin_views.admin_view_products,name='admin-view-products'),
    path('admin-logout',admin_views.admin_logout,name='admin-logout'), 
    path('accept_seller/<int:id>/',admin_views.accept_seller,name='accept_seller'), 
    path('reject_seller/<int:id>/',admin_views.reject_seller,name='reject_seller'), 


    # user paths
    path('user-login',main_views.user_login,name='user-login'), 
    path('user-signup',main_views.user_signup,name='user-signup'), 



]


urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  