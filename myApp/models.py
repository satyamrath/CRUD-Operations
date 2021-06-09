from django.db import models
from datetime import datetime

# Create your models here.
class Document(models.Model): #inheriting from models.py
    document_title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    creation_time = models.DateTimeField(default=datetime.now())
    document_file = models.FileField(upload_to="myApp/document_files", default="")
    document_type = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.document_title + " by " + self.author
