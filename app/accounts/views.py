from accounts.models import User
from accounts.serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class Register(APIView):

    def post(self, req):
        data = req.data

        if User.objects.filter(phone=data['phone']).exists():
            return Response({'status': 'failed', 'message': 'already used', 'data': {}}, status=422)

        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'status': 'success', 'message': '', 'data': serializer.data})


class Register(APIView):

    def post(self, req):
        data = req.data
        if User.objects.filter(phone=data['phone']).exists():
            return Response({'status': 'failed', 'message': 'already used', 'data': {}}, status=422)
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh, access = user.new_token()
        return Response({'status': 'success', 'data': {'refresh_token': refresh, 'access_token': f'Bearer {access}'}, 'message': ''})


class Login(APIView):

    def post(self, req):
        data = req.data
        user = User.objects.filter(phone=data['phone']).first()
        if not user or not user.check_password(data['password']):
            return Response({'status': 'failed', 'message': 'invalid data', 'data': {}}, status=422)
        refresh, access = user.new_token()
        return Response({'status': 'success', 'data': {'refresh_token': refresh, 'access_token': f'Bearer {access}'}, 'message': ''})


class UserProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, req):
        serializer = UserSerializer(req.user)
        return Response({'status': 'success', 'message': '', 'data': serializer.data})
