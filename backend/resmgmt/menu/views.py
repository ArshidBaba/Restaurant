from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from api.mixins import StaffEditorPermissionMixin
# from api.authentication import TokenAuthentication
from .models import Menu
from .serializers import MenuSerializer
# from api.permissions import IsStaffEditorPermission

class MenuListCreateAPIView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    def perform_create(self, serializer):
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content=content)
        # return super().perform_create(serializer)

class MenuDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


class MenuUpdateAPIView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
        
            
class MenuDestroyAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        

# class MenuListAPIView(generics.ListAPIView):
#     """
#     Not gonna use this method
#     """



@api_view(['GET', 'POST'])
def menu_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            obj = get_object_or_404(Menu, pk=pk)
            data = MenuSerializer(obj, many=False).data
            return Response(data)
        queryset = Menu.objects.all()
        data = MenuSerializer(queryset, many=True).data
        return Response(data)
            
    if method == "POST":
        serializer = MenuSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content=content)
        return Response(serializer.data)


