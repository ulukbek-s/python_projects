from django.contrib.auth import authenticate

from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import RegisterApiSerializer, LoginApiSerializer


class RegisterApiView(generics.GenericAPIView):
    serializer_class = RegisterApiSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user).save()
            if user:
                user.is_active = True
                user.save()
            return Response({'status': 'user successfully created'})

        return Response({'error': 'something went wrong'})


class LoginApiView(APIView):
    serializer_class = LoginApiSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['phone_number'],
            password=serializer.validated_data['password'],
        )
        Token.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)
        if not user:
            return Response({"error": "invalid email or password"}, status='400')
        return Response({'info': 'logged in'})