from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    category = models.CharField(max_length=32, default=None, blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '%s' % self.category


class Task(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=128, unique=True, default=None, blank=True, null=True)
    task = models.TextField(default=None, blank=True, null=True)
    priority = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    category = models.ForeignKey(Category, default=None, blank=True, null=True, on_delete=models.SET_NULL)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_time = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return '%s' % self.title


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     task = models.ForeignKey(Task, null=True, on_delete=models.SET_NULL)
#
#     @receiver(post_save, sender=User)
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user=instance)
#
#     @receiver(post_save, sender=User)
#     def save_user_profile(sender, instance, **kwargs):
#         instance.profile.save()

