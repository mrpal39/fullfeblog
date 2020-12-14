from django.db import models
# Creating a comment systems
from blog.models import Post


from django.db import models
from django.conf import settings
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                     on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                         blank=True)
                         
    def __str__(self):
      return f'Profile for user {self.user.username}'


class Comment(models.Model):
    post = models.ForeignKey(Post,
                               on_delete=models.CASCADE,
                               related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
   
   
    class Meta:
        ordering = ('created',)
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
