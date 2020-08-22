from django.db import models

# Create your models here.
class Category(models.Model):
    tittle=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.tittle

class Image(models.Model):
    tittle=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='images')
    added_date=models.DateTimeField()
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.tittle