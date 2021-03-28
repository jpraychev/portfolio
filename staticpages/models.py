from django.db import models
from PIL import Image


class Skills(models.Model):

    skill_name = models.CharField(max_length=50)
    skill_percent = models.CharField(max_length=50)
    skill_class = models.CharField(max_length=50)
    skill_color = models.CharField(default='red', max_length=50)


class Testimonials(models.Model):

    quote_text = models.TextField(max_length=100)
    quote_author = models.CharField(max_length=20)
    quote_author_company = models.CharField(max_length=20)
    quote_author_image = models.ImageField(default='quote_images/default.jpg', upload_to='quote_images')
    quote_color = models.CharField(default='red', max_length=50)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.quote_author_image.path)

        # TO DO
        # Saved image should have static height and width in order to prevent the user to upload too big files
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.quote_author_image.path)


class Education(models.Model):
    
    degree_name = models.CharField(max_length=50)
    degree_field = models.CharField(max_length=50)
    degree_year = models.CharField(max_length=50)
    degree_description = models.TextField(max_length=300)


class Experience(models.Model):
    
    experience_name = models.CharField(max_length=50)
    experience_field = models.CharField(max_length=50)
    experience_year = models.CharField(max_length=50)
    experience_description = models.TextField(max_length=300)


class Project(models.Model):
    
    project_name = models.CharField(max_length=50)
    project_description = models.TextField(max_length=300)
    project_homepage = models.CharField(max_length=50)
    project_image = models.ImageField(default='project_images/default.jpg', upload_to='project_images')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.project_image.path)

        # TO DO
        # Saved image should have static height and width in order to prevent the user to upload too big files
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.project_image.path)


class Service(models.Model):
    
    service_name = models.CharField(max_length=50)
    service_description = models.TextField(max_length=300)
    service_icon = models.CharField(max_length=50)
    service_color = models.CharField(default='red', max_length=50)