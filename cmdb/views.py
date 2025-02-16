from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import BSIC_INFO
# Create your views here.
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User

from .serializers import *
from cmdb import remote_server_info

import re
import pdb
# 认证登录跳转
class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):

        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            # 登录成功，可以返回一些信息或者token
            return Response({'detail': 'Login successful'})
        else:
            return Response(serializer.errors, status=400)

class BSICINFOListView(generics.ListAPIView):
    queryset = BSIC_INFO.objects.all()
    serializer_class = BSICINFOSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.5
    """
    queryset = Group.objects.all()
    serializer_class = BSICINFOSerializer
    permission_classes = [permissions.IsAuthenticated]

class BSICINFOViewSet(viewsets.ModelViewSet):
    queryset = BSIC_INFO.objects.all()
    serializer_class = BSICINFOSerializer
    permission_classes = [permissions.IsAuthenticated]  

class GetSysInfoView(viewsets.ViewSet):
    def list (self, request, *args, **kwargs):
        reponse_data = {
            "cpu_cores":"1", 
            "ip":"1.1.1.1"
        }
        return Response(reponse_data)
    def post(self, request, *args, **kwargs):  
        ip = request.data.get('ip',None)
        username = request.data.get('sys_user',"root")
        password = request.data.get('sys_password',"root")
        ip_regex = re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
        cpu_cores = remote_server_info.get_cpu_info(ip, username, password)
        
        if not ip:
            raise ValidationError({"ip": ["This field is required."]})
        if not ip_regex.match(ip):
            raise ValidationError({"ip": ["Invalid IP address."]})
        
        try:
            cpu_cores =  remote_server_info.get_cpu_info(ip, username, password)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
        reponse_data = {
            "cpu_cores":cpu_cores, 
            "ip":ip
        }
        return Response(reponse_data)
          

# @api_view(['GET'])
# def get_sys_resource(request):
#     hostname = "10.10.10.152"
#     username = "root"
#     password = "root"
#     cpu_cores = remote_server_info.get_cpu_info(hostname, username, password)
#     return JsonResponse({"cpu_cores":cpu_cores})

    


    def get_cmdb(request):
        cmdb_obj = BSIC_INFO.objects.all().values()
        cmdb = list(cmdb_obj)
        return JsonResponse({"data":cmdb})


