from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers

from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'senha']
        extra_kwargs = {'senha': {'write_only': True}} # Só aparece em formulario

    def create(self, validated_data):
        validated_data['senha'] = make_password(validated_data['senha'])
        return Usuario.objects.create(**validated_data)

from django.contrib.auth.hashers import check_password


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    senha = serializers.CharField(write_only=True)

    def validate(self, attrs):
        try:
            usuario = Usuario.objects.get(email=attrs['email'])
        except Usuario.DoesNotExist:
            raise serializers.ValidationError('E-mail ou senha inválidos.')

        if not check_password(attrs['senha'], usuario.senha):
            raise serializers.ValidationError('E-mail ou senha inválidos.')

        attrs['usuario'] = usuario
        return attrs
    
class LoginResponseSerializer(serializers.Serializer):
    mensagem = serializers.CharField()
    access = serializers.CharField()
    refresh = serializers.CharField()
    usuario_id = serializers.IntegerField()
    nome = serializers.CharField()