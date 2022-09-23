from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def update_rating(self, user):
        pass


class Category(models.Model):
    category = models.TextField(unique=True)

    def __str__(self):
        return f'{self.category}'


article = 'AR'
news = 'NW'

TYPE = [
    (article, "Статья"),
    (news, "Новость")
]


class Post(models.Model):
    authors = models.ForeignKey("Author", on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE)
    date_create = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField("Category", through='PostCategory')
    header = models.CharField(max_length=128)
    body = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating = +1
        self.save()

    def dislike(self):
        self.rating = -1
        self.save()

    def preview(self):
        return self.body[:128] + print('...')

    def __str__(self):
        return f'{self.header}: {self.body[:20]}'


class PostCategory(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating = +1

    def dislike(self):
        self.rating = -1
