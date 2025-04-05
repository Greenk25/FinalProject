from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

class UserRegistration(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key})

