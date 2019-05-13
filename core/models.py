from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.FileField(upload_to='profiles', null=True, blank=True)
    ph_no = models.IntegerField(verbose_name="Phone Number",null=True,  blank=True)
    company = models.CharField(max_length=50,null=True, blank=True)
    designation = models.CharField(max_length=50,null=True, blank=True)
    birth_date = models.DateField( null=True, blank=True)
    website = models.URLField(null=True, blank=True)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)

    subcategories = models.ManyToManyField('self', symmetrical=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=120)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Passenger(models.Model):
    name = models.CharField(max_length=34)
    sex = models.CharField(max_length=34)
    survived = models.BooleanField()
    age = models.FloatField()
    pclass = models.PositiveSmallIntegerField()
    embarked = models.CharField(max_length=34)