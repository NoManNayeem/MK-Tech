
from functools import partial
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from django.views.decorators.csrf import ensure_csrf_cookie


from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.views.decorators.csrf import csrf_exempt

from ..serializers.productSerializer import ProductSerializer
from ..serializers.profileSerializer import ProfileSerializer
from ..serializers.orderSerializer import OrderSerializer

from ..models import *


#### View All Customers As Admin ####
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def view_customers(request, format=None):
    if request.method=="GET":
            profile = Profile.objects.get(user=request.user)
            if profile.userType==1:
                customers = Profile.objects.filter(userType = 2)
                serializer = ProfileSerializer(customers, many=True)
                content = serializer.data
                return Response(content)
            else:
                content = {"message":"You Are Not An Admin"}
            return Response(content)


#### View All Orders As Admin ####
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def view_orders(request, format=None):
    if request.method=="GET":
            profile = Profile.objects.get(user=request.user)


            if profile.userType==1:
                orders = Order.objects.all()
                serializer = OrderSerializer(orders, many=True)
                content = serializer.data
                return Response(content)
            else:
                content = {"message":"You Are Not An Admin"}
            return Response(content)



#### Change Order_Status As Admin ####
@api_view(['PATCH'])
@permission_classes((IsAuthenticated,))
def change_order_status(request,id,format=None):
    if request.method=="PATCH":
        profile = Profile.objects.get(user=request.user)
        if profile.userType==1:
            order = Order.objects.get(id = id)
            serializer = OrderSerializer(order, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data=serializer.data)
                


## View & Create Product #####

@api_view(['GET', 'POST'])
@ensure_csrf_cookie
@renderer_classes((JSONRenderer,))
@csrf_exempt
@permission_classes((IsAuthenticated,))
def newProducts(request):
    profile = Profile.objects.get(user=request.user)
    if profile.userType==1:
        if request.method == 'GET':
            product = Product.objects.all()
            serializer = ProductSerializer(product, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



### UPDATE, DELETE PRODUCT ###
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def product(request, id):
    profile = Profile.objects.get(user=request.user)
    if profile.userType==1:
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = ProductSerializer(product)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        content = {"message":"You Are Not An Admin"}
        return Response(content)


