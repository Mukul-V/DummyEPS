from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from nividapp.src.views.BaseRequestFile import get_data, post_data


class BaseView(APIView):
    def get(self, request):
        if request.query_params.get('page') and request.query_params.get('rows'):  # Pagination
            model = request.query_params.get('model')
            page = int(request.query_params.get('page'))
            rows = int(request.query_params.get('rows'))
            column = request.query_params.get('column')
            val = request.query_params.get('value')
            field = request.query_params.get('field', default="key")  # Field to order the data accordingly
            order = request.query_params.get('order', default="1")  # Type of order the data accordingly
            types = request.query_params.get('types', default=None)
            data = get_data(model, page, rows, field, order, column, val, types)
            return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        model = request.query_params.get('model')
        data = request.data
        detail = post_data(model, data)

