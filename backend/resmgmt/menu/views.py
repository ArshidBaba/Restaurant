from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from .models import Menu
from .serializers import MenuSerializer

class MenuListCreateAPIView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def perform_create(self, serializer):
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content=content)
        # return super().perform_create(serializer)

class MenuDetailAPIView(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuUpdateAPIView(generics.UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
        
            
class MenuDestroyAPIView(generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = 'pk'

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


