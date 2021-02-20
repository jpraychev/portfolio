from django.db import models
from django.utils import timezone
from accounts.models import CustomUser
from math import floor

STATUS = (
    (0, 'Publish'),
    (1, 'Draft'),
    (2, 'Preview'),
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
    # time_since_created = models.DateTimeField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    author_bio = models.CharField(max_length=200, default='default-bio')
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    status = models.IntegerField(choices=STATUS, default=0)
    
    def get_tags(self):
        return ", ".join([str(p) for p in self.tags.all()])

    # A property is a dynamic field based on another field.
    # Calculates time since post was published
    # This should be used
    @property
    def time_created_before(self):
        time_diff = timezone.now() - self.date_posted
        seconds = floor(time_diff.total_seconds())
        time_since_creation = 0
        if seconds < 3600:
            time_since_creation = str(seconds//60) + ' mins ago'
        elif seconds > 3600 and seconds < 86400:
            time_since_creation = str(seconds//3600) + ' hours ago'
        elif seconds > 8600 and seconds < 432.000:
            time_since_creation = str(seconds//86000) + ' days ago'
        else:
            posted_on = str(self.date_posted.strftime('%b. %d'))
            time_since_creation = 'on ' + posted_on
        return time_since_creation

    # Overriding save method creates a new field which is not dynamic
    # def save(self, *args, **kwargs):
    #     self.time_since_created = timezone.now()-self.date_posted
    #     super(Post, self).save(*args, **kwargs) # Call the "real" save() method.

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return str(self.title)