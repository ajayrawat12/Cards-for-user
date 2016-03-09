from django.db import models
from apps.users.models import UserProfile
import datetime
# Create your models here.
class Cards(models.Model):
    """docstring for cards"""
    user_profile=models.ForeignKey(UserProfile, related_name='card', default=1)

    card_hero_image=models.ImageField(upload_to='Cards', blank=True, null=True, verbose_name='Card display image', help_text='Add')
    
    card_title=models.CharField(max_length=255, blank=False, null=False,)

    card_created_on=models.DateTimeField(
        'Card Created  On',
        default=datetime.datetime.now,
        )

    card_description=models.TextField(
        blank=False,
        null=False,
        verbose_name='card_description'
        )

    def __unicode__(self):
        return self.card_title

#changes on 28 FEB
    class Meta:
        verbose_name='Cards'
        verbose_name_plural='Cards'


"""Model For including Comment Feature"""
# class Comments(models.Model):
#     user_profile = models.ForeignKey(UserProfile, related_name='user_comments')

#     card = models.ForeignKey(Cards, related_name='card_comments')

#     Comment = models.TextField(blank=True, null=True, verbose_name='Comments')

#     def __unicode__(self):
#         return self.Comment

#     class Meta:
#         """docstring for Meta"""
#         verbose_name='Comments'
#         verbose_name_plural='Comments'


# """Model For including Like Feature"""
# class Post(models.Model):
#     likes = models.ForeignKey(UserProfile, null=True, blank=True, related_name="likes")

#     def __unicode__(self):
#         return self.likes
