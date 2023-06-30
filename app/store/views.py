from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from store.models import *
from store.serializers import *
from store.views import *


class ApplicationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, req):
        serializer = ApplicationSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        application = serializer.create(req.user)
        data = ApplicationSerializer(instance=application).data
        return Response({'status': 'success', 'message': '', 'data': data})

    def get(self, req, application_id=None):
        if application_id is None:
            applications = Application.objects.filter(
                is_active=True).select_related('developer')
            serializer = BriefApplicationSerializer(applications, many=True)
        else:
            application = Application.objects.get(id=application_id)
            serializer = ApplicationSerializer(application)
        return Response({'status': 'success', 'message': '', 'data': serializer.data})


class CommentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, req):
        serializer = CommentSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        comment = serializer.create(req.user)
        data = CommentSerializer(instance=comment).data
        return Response({'status': 'success', 'message': '', 'data': data})

    def get(self, req):
        comments = Comment.objects.filter(
            application_id=req.GET['application']).select_related('user')
        serializer = CommentSerializer(comments, many=True)
        return Response({'status': 'success', 'message': '', 'data': serializer.data})
