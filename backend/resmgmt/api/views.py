import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    print(request.GET)
    print(request.POST)
    body = request.body # byte string of the JSON data
    data = {}
    try:
        data = json.loads(body) # string of JSON data -> Python Dict
    except:
        pass
    print(data)
    # print(body)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)