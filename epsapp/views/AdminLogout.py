from django.contrib.auth import logout
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from epsapp.models.AuthTrails import AuthTrails as AuthTrail
from epsapp.serializers.AuthTrails import AuthTrails


class AdminLogout(APIView):
    permission_classes = ([IsAuthenticated])

    def get(self, request):
        print(request.session)
        if 'auth_trails' in request.session:
            current_dateTime = datetime.now()
            auth_id = request.session["auth_trail"]
            data = AuthTrail.objects.get(key=auth_id)
            detail = {
                "user_logout": "Ended " + str(current_dateTime),
            }
            serial = AuthTrails(data, data=detail, partial=True)
            if serial.is_valid(raise_exception=True):
                serial.save()
            logout(request)
            return Response('Logged Successfully')
        else:
            return Response("Invalid Token Login Again.")
