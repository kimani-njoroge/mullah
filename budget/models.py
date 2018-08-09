from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from djmoney.models.fields import MoneyField


class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
   if created:
       Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
   instance.profile.save()


class Transaction(models.Model):
    FOOD = 'FOOD'
    ENTERTAINMENT = 'ENTERTAINMENT'
    FUEL = 'FUEL'
    NAME = (
        (FOOD, 'food'),
        (ENTERTAINMENT, 'entertainment'),
        (FUEL, 'fuel')
    )
    name = models.CharField(max_length=15, choices=NAME, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = MoneyField(max_digits=8,decimal_places=2,default_currency='KES')
    date = models.DateField()

    def __str__(self):
        return self.name

    def transaction_save(self):
        self.save()
