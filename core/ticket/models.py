from django.conf import settings
from django.db import models



class Ticket(models.Model):
    status_choice = (
        (0, 'در حال بررسی'),
        (1, 'تکمیل شده')
    )
    title = models.TextField(max_length=128)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.SmallIntegerField(choices=status_choice, default=0)
    unread = models.BooleanField()
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)


class SubTicket(models.Model):
    parent = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(max_length=512)
    created_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
