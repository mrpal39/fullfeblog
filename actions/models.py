from django.db import models
from django.contrib.contenttypes.fields import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Action(models.Model):
    user=models.ForeignKey('auth.user',related_name='actions',db_index=True,
    on_delete= models.CASCADE)
    """image_type = ContentType.objects.get(app_label='images',model='image')
    docstring
    """
    verb =models.CharField(max_length=255)
    target_ct=models.ForeignKey(ContentType,blank=True,null=True,related_name='target_obj',on_delete=models.CASCADE)
    target_id=models.PositiveIntegerField(null=True,blank=True)
    target=GenericForeignKey('target_ct','target_id')

    created=models.DateTimeField(auto_now_add=True,db_index=True)


    class Meta:
        ordering=('-created',)
