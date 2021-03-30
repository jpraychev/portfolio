from django.db import models
from PIL import Image

COLORS = [
    ( '#ec5453', 'Red' ),
    ( '#2fa499', 'Green' ),
    ( '#2c98f0', 'Blue' ),
    ( '#4054b2', 'Dark blue' ),
    ( '#f9bf3f', 'Yellow' ),
    ( '#a84cb8', 'Purple' ),
]

ICONS = [
    ( 'fas fa-network-wired', 'Network wired' ),
    ( 'fab fa-linux', 'Linux' ),
    ( 'fab fa-css3-alt', 'HTML & CSS3' ),
    ( 'fab fa-js-square', 'Javascript' ),
    ( 'fas fa-database', 'SQL' ),
    ( 'fab fa-python', 'Python' ),
    ( 'fas fa-code', 'Code')
]

def image_resize(image, width, height):

    img = Image.open(image.path)

    if img.height > height or img.width > width:
        output_size = (height, height)
        img.thumbnail(output_size)
        img.save(image.path)
        
class Skills(models.Model):

    skill_name = models.CharField(max_length=50)
    skill_percent = models.CharField(max_length=50)
    skill_class = models.CharField(
        max_length=20,
        choices=ICONS,
        default='Python',
    )
    skill_color = models.CharField(
        max_length=20,
        choices=COLORS,
        default='Red',
    )


class Testimonials(models.Model):

    quote_text = models.TextField(max_length=200)
    quote_author = models.CharField(max_length=20)
    quote_author_company = models.CharField(max_length=20)
    quote_author_image = models.ImageField(default='quote_images/default.jpg', upload_to='quote_images')
    quote_color = models.CharField(
        max_length=20,
        choices=COLORS,
        default='Red',
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        image_resize(self.quote_author_image, 300, 300)


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
    service_icon = models.CharField(
        max_length=20,
        choices=ICONS,
        default='Python',
    )
    service_color = models.CharField(
        max_length=20,
        choices=COLORS,
        default='Red',
    )