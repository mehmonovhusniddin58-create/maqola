from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from common.models import Userprofile


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Maqola(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    content = RichTextField()
    created_at = models.DateTimeField()
    views = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
        
    
class Comment(models.Model):
    user = models.ForeignKey(Userprofile,on_delete=models.CASCADE, )
    article = models.ForeignKey(Maqola,on_delete=models.CASCADE,)
    text = models.TextField()
    vaqti = models.DateTimeField(default=timezone.now)
    admin_reply = models.TextField()
    admin_name = models.CharField(max_length=50)
    status = models.BooleanField(default=False)

    def str(self):
        return f"{self.user} {self.article}"
    
class Like(models.Model):
    user = models.ForeignKey(Userprofile,on_delete=models.CASCADE,)
    article = models.ForeignKey( Maqola,on_delete=models.CASCADE)
    vaqti = models.DateTimeField(default=timezone.now)


    def str(self):
        return f"{self.user.username} ❤️ {self.article.title}"

