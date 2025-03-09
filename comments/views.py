from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        # POST /api/comments//approve/
        comment = self.get_object()
        comment.is_approved = True
        comment.save()
        return Response({'status': 'Comment approved successfully'}, status=200)