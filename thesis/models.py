from django.db import models

class Thesis(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)  # Example of adding a slug field
    status = models.CharField(max_length=50)  # Example of adding a status field
    created_on = models.DateTimeField(auto_now_add=True)  # Example of adding a created_on field

    # Your other fields and methods

    