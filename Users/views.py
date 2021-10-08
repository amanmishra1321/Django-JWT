from datetime import datetime
from django.shortcuts import render
from rest_framework.views import APIView

from Users.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime

class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'response':'Successfully Created'})
    
class LoginView(APIView):
    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email).first()
        if not user:
            return AuthenticationFailed("Invalid Email Address")
        if not user.check_password(password):
            return AuthenticationFailed("Invalid Password")
        user.check_password(password)
        payload = {
            "email":user.email,
            "exp":datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
            "iat":datetime.datetime.utcnow()
        }
        token = jwt.encode(payload,'secret',algorithm='HS256')
        response = Response()
        response.set_cookie(key='jwt',value=token,httponly=True)
        response.data={"token":token}
        return response



