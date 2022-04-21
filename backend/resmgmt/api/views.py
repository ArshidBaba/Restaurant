import json
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from menu.models import Menu
from rest_framework.decorators import api_view

from menu.serializers import MenuSerializer

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    instance = Menu.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(model_data, fields=['id', 'title', 'price' 'sale_price'])
        data = MenuSerializer(instance).data
    return Response(data)
    # model_data = Menu.objects.all().order_by("?").first()
    # data = {}
    # if model_data:
    #     data['id'] = model_data.id
    #     data['title'] = model_data.title
    #     data['content'] = model_data.content
    #     data['price'] = model_data.price
    # return JsonResponse(data)
    