from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ActivationSerializer, LoginSerializer, RegistrationSerializer, ChangePasswordSerializer, \
    ForgotPasswordSerializer
from rest_framework import status


class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
            return Response('You successfully registered', status=201)


class ActivationView(APIView):
    def post(self, request):
        serializer = ActivationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response('Account successfully activated', status=200)


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('You successfully logout')


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = ChangePasswordSerializer(data=request.data,
                                               context={'request':request})
        if serializer.is_valid(raise_exeption=True):
            serializer.set_new_password()
            return Response('Password successfully changed')


class ForgotPasswordView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exeption=True):
            serializer.set_new_password()
            return Response('Password successfully changed')


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('You successfully logout')
