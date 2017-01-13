import json
from django.shortcuts import render
import os, dill
from djangoMiniProject import settings


def post_list(request):
    json_path = os.path.join(settings.STATIC_ROOT, 'data_20170113.json')
    with open(json_path, 'r') as fp:
        data = json.load(fp)

    return render(request, 'mini/post_list.html', {'data': data})