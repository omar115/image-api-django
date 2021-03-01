"""
create table for images to store the images

"""


from django.db import models
from django.utils import timezone  #capture time when user upload the image
from django.contrib.auth.models import User  #record users who upload the images, django admin panel

# Create your models here.

#create a user directory path where to upload the images

def user_directory_path(instance, filename):
    return 'images/{0}/'.format(filename)


#create category table

class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
    

class Images(models.Model):

    options = (
        ('active', 'Active'),
        ('deactivated', 'Deactivated'),
    )

    #create a foreign key to connect category to the image table
    #models.protect == prevent someone to delete the images from the category

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    
    title = models.CharField(max_length=250)

    alt = models.TextField(null=True)

    image = models.ImageField(upload_to=user_directory_path, default='posts/default.jpg')

    slug = models.SlugField(max_length=250, unique_for_date='created')
    created = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='author'
    )