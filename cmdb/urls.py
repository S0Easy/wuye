# from django.urls import path,  include
# from django.contrib.auth.models  import User   
# from rest_framework import routers, serializers, viewsets

# # Serializers define the API representation
# class UserSeralizer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups', 'is_staff')

# # ViewSets define the view behavior
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSeralizer

# # Router provides an easy way of automatically determining  the URL  conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
# ]