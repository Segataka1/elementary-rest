from django.db.models import Max, Min, Avg, Sum
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import random, string


class Shop(models.Model):
    name = models.CharField(max_length=127)
    time_start = models.TimeField()
    time_end = models.TimeField()
    address = models.CharField(max_length=127)
    status = models.BooleanField(False)

    def __str__(self) -> str:
        return self.name

    @property
    def avg_ticket_price(self):
        return self.tickets.aggregate(Avg('price'))['price__avg']

    def max_ticket_price(self):
        return self.tickets.aggregate(Max('price'))['price__max']

    def min_ticket_price(self):
        return self.tickets.aggregate(Min('price'))['price__min']

    def sum_ticket_price(self):
        return self.tickets.aggregate(Sum('price'))['price__sum']


class Ticket(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='tickets')
    name =models.CharField(max_length=127)
    price =models.PositiveIntegerField(default=0)
    replace_from =models.CharField(max_length=127)
    replace_to =models.CharField(max_length=127)

    def __str__(self) -> str:
        return self.name


def create_ticket(sender, instance, created, **kwargs):
    post_save.disconnect(create_ticket, sender=sender)
    if instance.status:
        instance.name = f'{instance.name} - is active'
        instance.save()
    post_save.connect(create_ticket, sender=sender)
post_save.connect(create_ticket, sender=Shop)

    # @receiver(post_save, sender=Shop)
    # if created:
    #     S = 10
    #     ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
    #     Ticket.objects.create(
    #         shop=instance,
    #         name=ran,
    #         price=random.randint(1_000, 10_000),
    #         replace_from=''.join(random.choices(string.ascii_uppercase + string.digits, k=S)),
    #         replace_to=''.join(random.choices(string.ascii_uppercase + string.digits, k=S)),
    #     )

