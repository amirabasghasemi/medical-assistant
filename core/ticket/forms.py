from django import forms

from core import settings


class TicketForm(forms.Form):
    text = forms.TextInput()
