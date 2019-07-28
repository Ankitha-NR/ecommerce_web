from rest_framework.views import APIView
from django.http import JsonResponse

class store(APIView):

    def get(self, requests):
        print requests.GET
        response = {"success": True,"message":"GET API is working successfully"}
        return JsonResponse(response)

    def post(self, requests):
        print requests.data
        response = {"success": True, "message": "POST API is working successfully"}
        return JsonResponse(response)
