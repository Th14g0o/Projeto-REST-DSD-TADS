from rest_framework import generics
from .models import Usuario
from .serializers import UsuarioSerializer, LoginSerializer, LoginResponseSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema

class UsuarioListView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class LoginView(APIView):
    serializer_class = LoginSerializer

    @swagger_auto_schema(request_body=LoginSerializer, responses={200: LoginResponseSerializer})
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        usuario = serializer.validated_data['usuario']

        refresh = RefreshToken.for_user(usuario)

        return Response({
            'mensagem': 'Login realizado com sucesso.',
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'usuario_id': usuario.id,
            'nome': usuario.nome,
        })