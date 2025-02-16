"""
URL configuration for wuye project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from cmdb import views

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from  cmdb.views import *



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups',  GroupViewSet)  
router.register(r'cmdb',  BSICINFOViewSet)
router.register(r'sysinfo',  GetSysInfoView,basename='cpu_cores')



urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # LoginView路由
    path('api/login/', LoginView.as_view(), name='login'),
    # path('cmdb/get-sys-info/', GetSysInfoView.as_view(), name='sys_info'),
    path("admin/", admin.site.urls),
]

urlpatterns += router.urls
# urlpatterns = [
#     path("cmdb/", views.get_cmdb),
#     path('api-auth/', include('rest_framework.urls')),
#     path("admin/", admin.site.urls),
# ]
