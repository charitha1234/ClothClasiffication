from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import base64
import json
from django.core.files.base import ContentFile
from rest_framework.decorators import api_view
from django.core.files.storage import default_storage
from . import ColorDetect
@api_view(["POST","GET"])
def index(request):

    if request.method=="GET":
        return HttpResponse("Hello world")

    if request.method=="POST":
        image_data = json.loads(request.body)['content']
        format, imgstr = image_data.split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr))  
        file_name = "myphoto." + ext
        path = default_storage.save(file_name, data)
        print(file_name)
        ColorDetect.colorDetection(path)
        Content={
            "pattern":0,
            "polka":False,
            "floral":False,
            "colors":[
                {
                    "color":"green",
                    "percentage":50,
                    "shades":"dark green",

                },
                {
                    "color":"red",
                    "percentage":20,
                    "shades":"carrot"
                }
            ]
        }
        return JsonResponse(Content)
    
