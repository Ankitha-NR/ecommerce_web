from rest_framework.views import APIView
from django.http import JsonResponse
from src.libraries import UserLib

class UserView(APIView):

    def get(self, requests):
        print requests.GET
        response = {"success": True,"message":"GET API is working successfully"}
        return JsonResponse(response)

    def post(self, requests):
        response_text, success_status = UserLib().CreateUser(user_info = requests.data)
        Response = {"success": success_status, "message": response_text}
        return JsonResponse(Response)
