from django.db import models


class accessPost(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    service = models.CharField(max_length=200)
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    comment = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
