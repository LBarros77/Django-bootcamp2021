from django.db import models
import uuid
from django.urls.base import reverse

class Project(models.Model):
    #owner =
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    feactured_image = models.ImageField(null=True, blank=True, default='default.png')
    demo_link = models.CharField(max_length=1000, null=True, blank=True)
    source_link = models.CharField(max_length=1000, null=True, blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def get_absolute_url(self):
        return reverse('project_page', kwargs={'pk': self.id})

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            img = self.feactured_image.url
        except:
            img = ''
        return img

class Review(models.Model):

    VOTE_TYPE = (
        ('up', 'up'),
        ('down', 'down'),
    )
    #owner
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=50, choices=VOTE_TYPE)
    update = models.DateTimeField(auto_now_add=True)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name