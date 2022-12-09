from django.conf import settings
from django.db import models


class TicketStatus(models.TextChoices):
    TO_DO = 'برای ارسال تیکت'
    IN_PROGRESS = 'در حال پیگیری تیکت'
    IN_REVIEW = 'در حال بررسی تیکت'
    DONE = 'تمام شده'


class TicketModel(models.Model):
    title = models.CharField(max_length=100)
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=TicketStatus.choices, default=TicketStatus.TO_DO)
    description = models.TextField()
    created_at = models.DateTimeField('ایجاد شده در', auto_now_add=True)
    updated_at = models.DateTimeField('به روز شده در', auto_now=True)

# class Ticket(models.Model):
#     status_choice = (
#         (0, 'در حال بررسی'),
#         (1, 'تکمیل شده')
#     )
#     title = models.TextField(max_length=128)
#     text_ticket = models.TextField(max_length=512)
#     created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     status = models.SmallIntegerField(choices=status_choice, default=0)
#     unread = models.BooleanField()
#     create_time = models.DateTimeField(auto_now_add=True)
#     modify_time = models.DateTimeField(auto_now=True)

#
# class SubTicket(models.Model):
#     parent = models.ForeignKey(Ticket, on_delete=models.CASCADE)
#     sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     text = models.TextField(max_length=512)
#     created_time = models.DateTimeField(auto_now_add=True)
#     modify_time = models.DateTimeField(auto_now=True)
