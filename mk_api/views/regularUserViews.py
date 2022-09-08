from .adminViews import *




#### View Product ####
@api_view(['GET'])
@permission_classes((AllowAny,))
def view_products(request,format=None):
    if request.method=="GET":
        orders = Product.objects.all()
        serializer = ProductSerializer(orders, many=True)
        content = serializer.data
    else:
        content = {"message":"Products Not Found"}
    return Response(content)




#### View One Product ####
@api_view(['GET'])
@permission_classes((AllowAny,))
def view_one_product(request,id,format=None):
    if request.method=="GET":
        orders = Product.objects.filter(id=id)
        serializer = ProductSerializer(orders, many=True)
        content = serializer.data
    else:
        content = {"message":"Product Not Found"}
    return Response(content)




#### Create Order ####
@api_view(['POST'])
@permission_classes((AllowAny,))
def create_order(request,format=None):
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

