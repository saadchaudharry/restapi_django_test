from django.db import models

# Create your models here.

class Blog(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    description=models.TextField()
    price=models.IntegerField()

    def __str__(self):
        return str(self.title)