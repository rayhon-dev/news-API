from rest_framework import viewsets
from .models import New
from .serializers import NewsSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from comments.serializers import CommentSerializer



class NewsViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewsSerializer

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        # POST /api/news//publish/
        news = self.get_object()
        news.is_published = True
        news.save()
        return Response({'status': 'News published successfully'}, status=200)

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        # POST /api/news/1/comments/
        news = self.get_object()
        comments = news.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)