from django.db import models


class Category(models.Model):
        name = models.CharField(max_length=200, null=False, blank=False)
        description = models.CharField(max_length=500, null=True, blank=True)


        def __str__(self):
            return self.name

class Photo(models.Model):
    
        name = models.CharField(max_length=200, null=True, blank=True)
        category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
        image= models.ImageField(null=False, blank=False)
        description = models.CharField(max_length=200, null=True, blank=True)

        def __str__(self):
            return self.description
