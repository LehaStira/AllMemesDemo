from django.db import models

# Create your models here.


class Meme(models.Model):
    picture = models.ImageField(upload_to='memes/')
    published = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'<Meme - {self.picture}>'


class Tag(models.Model):
    name = models.CharField(max_length=200)
    memes = models.ManyToManyField(Meme, related_name='tags')

    def __str__(self):
        return f'Tag - {self.name}'