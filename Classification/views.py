from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import base64
import json
from django.core.files.base import ContentFile
from rest_framework.decorators import api_view
from django.core.files.storage import default_storage
from . import ColorDetect
from . import Model
@api_view(["POST","GET"])
def index(request):

    if request.method=="GET":
        return JsonResponse({"content":"Hello worls"})

    if request.method=="POST":
        image_data = json.loads(request.body)['content']
        # format, imgstr = image_data.split(';base64,')
        # ext = format.split('/')[-1]
        print(image_data)
        data = ContentFile(base64.b64decode(image_data))  
        file_name = "myphoto.jpg"
        path = default_storage.save(file_name, data)
        outputColors=ColorDetect.colorDetection(path)
        Class1,Class2=Model.predict(path)
        if Class2=="":
            Content={
                "pattern":Class1,
                "secondry_pattern":False,
                "colors":outputColors["Maincolors"]
            }
            return JsonResponse(Content)
        else:
            Content={
                "pattern":Class1,
                "secondry_pattern":Class2,
                "colors":outputColors["Maincolors"]
            }
            return JsonResponse(Content)
    
