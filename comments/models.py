from django.db import models
from news.models import New


class Comment(models.Model):
    news = models.ForeignKey(New, on_delete=models.SET_NULL, null=True, related_name='comments')
    author_name = models.CharField(max_length=100)
    author_email = models.EmailField(unique=True)
    content = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author_name} on {self.news}"
