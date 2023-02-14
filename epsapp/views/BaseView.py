from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from epsapp.views.BaseRequestClass import get_data, post_data
# post_data, delete_data, patch_data, put_position, \
# post_group, patch_group, post_user, get_app_data, get_web_domain

# from wijungleapp.src.views.FileUploadViewSet import FileUploadViewSet


class BaseView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if 'org_id' not in request.session or 'user_id' not in request.session or 'auth_trail' not in request.session:
            return Response("Invalid Token Login Again")
        else:
            if request.query_params.get('page') and request.query_params.get('rows'):  # Pagination
                model = request.query_params.get('model')
                page = int(request.query_params.get('page'))
                rows = int(request.query_params.get('rows'))
                column = request.data.get('column')  # COLUMN SEARCH COLUMN IN BODY
                val = request.data.get('value')  # # COLUMN SEARCH VALUE IN BODY
                field = request.query_params.get('field', default="key")  # Field to order the data accordingly
                order = request.query_params.get('order', default="1")  # Type of order the data accordingly
                types = request.query_params.get('types', default=None)
                org_id = request.session["org_id"]
                user_id = request.session["user_id"]
                auth_trail = request.session["auth_trail"]
                data = get_data(model, page, rows, org_id, user_id, auth_trail, field, order, column, val, types)
                return Response(data, status=status.HTTP_200_OK)

        # if request.data.get('model') == "app-data" and request.data.get("app-class"):  # API for getting app_class_data [on EDIT]
        #     model = request.data.get('model')
        #     app_class = request.data.get("app-class")
        #     data = get_app_data(model, app_class)
        #     return Response(data, status=status.HTTP_200_OK)
        #
        # if request.data.get("model") == "domain" and request.data.get("web-class"):  # API for getting domain [on EDIT]
        #     model = request.data.get('model')
        #     web_class = request.data.get("web-class")
        #     data = get_web_domain(model, web_class)
        #     return Response(data)

    # # Code for the Export in File (Type)
    # if request.query_params.get('file'):
    #     if request.query_params.get('file') == 'all':
    #         model = request.query_params.get('model')
    #         data = get_all_data(model)
    #         return Response(data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        if 'org_id' not in request.session or 'user_id' not in request.session or 'auth_trail' not in request.session:
            return Response("INVALID TOKEN, LOGIN AGAIN!!!")
        model = request.query_params.get('model')
        data = request.data
        action = request.query_params.get('action', default="null")
        print(model)
        print(data)
        print(action)
        org_id = request.session["org_id"]
        user_id = request.session["user_id"]
        auth_trail = request.session["auth_trail"]

        if action == "null":  # this is also for Registration
            print("In the condition")
            # if model == "base-class-grp":
            #     detail = post_group(org_id, user_id, model, data)
            #     return Response(detail)
            # if model == "users":
            #     detail = post_user(org_id, user_id, auth_trail, model, data)
            #     return Response(detail)
            # else:
            detail = post_data(org_id, user_id, auth_trail, model, data)  # CALL FROM BASE-REQUEST-CLASS
            return Response(detail)

    # def delete(self, request):
    #     model = request.query_params.get('model')
    #     auth_trail = request.session["auth_trail"]
    #
    #     if request.query_params.get("pk"):
    #         pk = request.query_params.get('pk')
    #         details = delete_data(model, pk, auth_trail)
    #         if details == 1:
    #             return Response({'msg': 'Record deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    #         else:
    #             return Response({'msg': details}, status=status.HTTP_400_BAD_REQUEST)
    #
    # def patch(self, request):
    #     # auth_trail = request.session["auth_trail"]
    #     model = request.query_params.get('model')
    #     key = request.data.get('key')
    #     data = request.data
    #     if model == "base-class-grp":
    #         detail = patch_group(model, key, data)
    #     elif model == "device-policy":
    #         action = request.query_params.get('action')
    #         detail = patch_data(model, key, data, action)
    #     else:
    #         detail = patch_data(model, key, data)
    #     if detail == 1:
    #         return Response("Record Updated Successfully.", status=status.HTTP_200_OK)
    #     else:
    #         return Response({"msg": detail}, status=status.HTTP_400_BAD_REQUEST)
    #
    # def put(self, request):
    #     key = int(request.query_params.get('key'))  # Key of the Row
    #     old = int(request.query_params.get('old'))  # Old position
    #     new = int(request.query_params.get('new'))  # New Position
    #     model = request.query_params.get('model')  # Rules
    #     detail = put_position(model, key, old, new)
    #     if detail == 1:
    #         return Response("Position Updated Successfully.", status=status.HTTP_200_OK)
    #     else:
    #         return Response({"msg": detail}, status=status.HTTP_400_BAD_REQUEST)
