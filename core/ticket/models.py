from django.conf import settings
from django.db import models


class TicketModel(models.Model):
    status_choice = (
        (0, 'در حال بررسی'),
        (1, 'تکمیل شده')
    )
    title = models.CharField(max_length=32)
    text = models.TextField(max_length=512)
    status = models.SmallIntegerField(choices=status_choice, default=0)
    unread = models.BooleanField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def change_unread(self, user):
        if user.is_staff:
            self.unread = True
        else:
            self.unread = False


class SubTicketModel(models.Model):
    parent = models.ForeignKey(TicketModel, on_delete=models.CASCADE)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(max_length=512)
    created_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
