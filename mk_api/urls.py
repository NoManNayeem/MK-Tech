from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import obtain_auth_token
from .views import adminViews,customerViews,regularUserViews

urlpatterns = [
    #''' Admin URLs '''#
    path('admin/product/id=<int:id>', adminViews.product, name='product'),
    path('admin/view_customers/', adminViews.view_customers, name='view_customers'),
    path('admin/view_orders/', adminViews.view_orders, name='view_orders'),
    path('admin/change_order_status/id=<int:id>', adminViews.change_order_status, name='change_order_status'),


    path('admin/newProducts/', adminViews.newProducts, name='newProducts'),

    # Regular User Views #
    path('create_order/', regularUserViews.create_order, name='create_order'),
    path('order_details/id=<int:id>', customerViews.order_details, name='order_status'),
    path('view_products/', regularUserViews.view_products, name='view_products'),
    path('view_one_product/id=<int:id>', regularUserViews.view_one_product, name='view_one_product'),


    # Customer URLs
    path('customer/all_order_details/', customerViews.all_order_details, name='all_order_details'),
    # path('admin/viewCustomer/customerName=<str:name>&id=<int:id>/', adminViews.view_customers, name='view_customers'),
    
    ### Auth Token ###
    path('login/api-token-auth/', obtain_auth_token, name='api_token_auth'),
    
]