from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

class CustomUser(AbstractUser):
    # add additional fields in here
    department = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    profile_image = models.ImageField(default='profile_default.jpg', upload_to='profile_images')

    def __str__(self):
        return self.username

    # Overrides the default save method and prepopulates slug field with the user's username
    def save(self, *args, **kwargs):
        self.slug = self.username
        super().save(*args, **kwargs)
        
        img = Image.open(self.profile_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)

        