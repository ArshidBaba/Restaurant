import json
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from menu.models import Menu
from rest_framework.decorators import api_view

from menu.serializers import MenuSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = MenuSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # print(instance)
        print(serializer.data)
        return Response(serializer.data)
    return Response({"Invalid": "This is not valid data"}, status=400)
    