from django.db import models

# Create your models here.

class Color(models.Model):

    CQ1 = models.TextField(max_length=10)
    CQ2 = models.TextField(max_length=10)
    CQ3 = models.TextField(max_length=10)
    CQ4 = models.TextField(max_length=10)
    CQ5 = models.TextField(max_length=10)
    CQ6 = models.TextField(max_length=10)
    


    def __str__(self):
        return self.title