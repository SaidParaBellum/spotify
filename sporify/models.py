from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=50, null=True, blank=True)
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Users"

class Musician(models.Model):
    name = models.CharField(max_length=100, null=True)
    user = models.OneToOneField(User, related_name='musician', on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    image = models.ImageField(upload_to='musician')

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    musician =models.ForeignKey(Musician, on_delete=models.CASCADE)
    duration = models.CharField(max_length=5)
    file = models.FileField(upload_to='songs')
    cover = models.ImageField(upload_to='songs')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ManyToManyField(User, related_name='playlist')
    longetivity = models.CharField(max_length=8)
    songs = models.ManyToManyField(Song, related_name='playlist')

    def __str__(self):
        return self.name


class Application(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    submitted_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.user.username} - {self.status}"