from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200,null=True)
    content = models.TextField(null=True)
    time = models.DateTimeField(null=True)
    category = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.title    



