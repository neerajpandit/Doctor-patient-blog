from django.db import models
from taskapp.models import User

class Blog(models.Model):

    CATEGORY_CHOICES = (
        ('Mental Health', 'Mental Health'),
        ('Heart Disease', 'Heart Disease'),
        ('Covid19', 'Covid19'),
        ('Immunization', 'Immunization'),
    )
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=30)
    thumbnail = models.ImageField(upload_to = 'images/')
    category = models.CharField(max_length=20, choices = CATEGORY_CHOICES)
    summary = models.CharField(max_length=200)
    content = models.TextField()
    is_draft = models.BooleanField(default = False)

    def __str__(self):
        return str(self.id)
