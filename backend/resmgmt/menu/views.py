from rest_framework import generics

from .models import Menu
from .serializers import MenuSerializer

class MenuDetailAPIView(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
