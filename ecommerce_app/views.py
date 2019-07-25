from __future__ import unicode_literals
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from models import storetable


@csrf_exempt
def store(requests):
    if requests.method == "GET":
        response_obj =storetable.objects.all()
        response = {"data":[]}
        for item in response_obj:
            response["data"].append(
                {
                "store_name":item.store_name,"store_location":item.store_location, "store_owner_name":item.store_owner_name}
            )

        #print a
        #response = {"message": "GET method is Working Successfully"}
    elif requests.method == "POST":
        request_body = json.loads(requests.body)
        storetable.objects.create(**request_body)
        response = {"message":"POST method is working successfully"}
    elif requests.method == "PUT":
        response = {"message":"PUT method is working successfully"}
    else:
        response = {"message":"DELETE method is working successfully"}
    return JsonResponse(response)


