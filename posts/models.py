from django.db import models
from django.utils import timezone
from accounts.models import CustomUser

STATUS = (
    (0, 'Publish'),
    (1, 'Draft')
)

class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return str(self.name)

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return str(self.name)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    header_image = models.ImageField(null=True, blank=True, upload_to='post_images')
    date_posted = models.DateTimeField(default=timezone.now)
    posted_before = models.DateTimeField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default='jraychev')
    author_bio = models.CharField(max_length=200, default='default-bio')
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return str(self.title)

