from .adminViews import *

#### Get order_details ####
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def order_details(request,id, format=None):
    if request.method=="GET":
        order = Order.objects.filter(id=id)
        serializer = OrderSerializer(order, many=True)
        content = serializer.data
        return Response(content)
    else:
        content = {"message":"Order Not Found"}
        return Response(content)


#### all_order_details ####
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def all_order_details(request,format=None):
    if request.method=="GET":
        profile = Profile.objects.get(user= request.user)
        orders = Order.objects.filter(customer = profile)
        serializer = OrderSerializer(orders, many=True)
        content = serializer.data
    else:
        content = {"message":"Order Not Found"}
    return Response(content)



