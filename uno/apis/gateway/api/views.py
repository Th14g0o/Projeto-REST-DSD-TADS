from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from .serializers import StatusSerializer


class StatusView(APIView):
    @swagger_auto_schema(responses={200: StatusSerializer})
    def get(self, request):
        return Response({'status': 'online', 'servico': 'gateway'})