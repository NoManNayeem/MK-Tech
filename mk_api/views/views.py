from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..models import Profile

# class HelloView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         profile = Profile.objects.get(user=request.user)
#         if profile.userType==1:
#             content = {'message': 'Hello, Admin!'}
#         else:
#             content = {"message":"You Are Not Admin"}
#         return Response(content)
