from django.contrib.auth import logout
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from epsapp.models.Trails import AuthTrails


class AdminLogout(APIView):
    permission_classes = ([IsAuthenticated])

    def get(self, request):
        print(request.session["user_id"])
        # print(requests.header["authorization"])
        # request.user.auth_token.delete()
        # logout(request)
        return Response('User Logged out successfully')

    # def get(self, request):
    #     user_id = request.session["user_id"]
    #     data = AuthTrails.objects.get(user=user_id)
    #     current_dateTime = datetime.now()
    #     detail = {
    #         "user_logout": "Ended "+str(current_dateTime),
    #     }
    #     print(detail)
    #     return Response('User Logged out successfully')
