from django import forms

from core import settings
from ticket.models import TicketModel


class TicketForm(forms.ModelForm):

    class Meta:
        model = TicketModel
        fields = ('title', 'text')

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'col-12 rounded-2 input',
             'type': 'text',
             'placeholder': 'موضوع تیکت خود را وارد کنید'}
        )
        self.fields['text'].widget.attrs.update(
            {'class': 'form-control col-12 rounded-2',
             'aria-label': 'With textarea',
             'placeholder': 'توضیحات مربوط به تیکت خودرادراین قسمت واردنمایید'}
        )