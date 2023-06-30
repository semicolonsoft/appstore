from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    developer = models.ForeignKey(
        'accounts.User', on_delete=models.PROTECT, related_name='applications')
    cover = models.FileField(upload_to='app_covers')
    file = models.FileField(upload_to='applications')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Comment(models.Model):
    application = models.ForeignKey('store.Application', on_delete=models.PROTECT, related_name='comments')
    user = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='comments')
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
