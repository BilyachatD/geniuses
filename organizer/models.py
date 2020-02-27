from django.db import models
from django.contrib.auth.models import User

class Notation(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = 1)
    title = models.CharField('заголовок напоминания', max_length= 100)
    text = models.TextField('текст напоминания')
    pub_date = models.DateTimeField('дата публикации')
    important = models.BooleanField('важность', default=False)
    public = models.BooleanField("опубликовано или нет", default=False)
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title
    
