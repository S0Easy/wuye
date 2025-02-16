from django.contrib.auth.models import Group, User
from .models import BSIC_INFO
from rest_framework import serializers
from cmdb import remote_server_info
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        return data


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']




class BSICINFOSerializer(serializers.HyperlinkedModelSerializer):
    hostname = serializers.CharField(allow_blank=True)
    assset_desc = serializers.CharField(allow_blank=True)
    cpu_cores = serializers.CharField(allow_blank=True)
    sys_user = serializers.CharField(allow_blank=True)
    sys_password = serializers.CharField(allow_blank=True)
    class Meta:
        model = BSIC_INFO
        fields = '__all__'
