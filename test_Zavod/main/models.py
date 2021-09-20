from django.db import models
from taggit.managers import TaggableManager

class NewPost(models.Model):
    tittle = models.CharField('Заголовок', max_length=75)
    text = models.TextField('Новость')
    image = models.ImageField('Картинка')
    tags = TaggableManager()
    views = models.IntegerField('Просмотры', default=0)
    def __str__(self):
        return self.tittle
