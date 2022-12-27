from django import forms

from core import settings
from ticket.models import TicketModel, SubTicketModel


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

class SubTicketForm(forms.ModelForm):
    class Meta:
        model = SubTicketModel
        fields = ('text', )
    def __init__(self, *args, **kwargs):
        super(SubTicketForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class':'w-75 rounded-4 textarea-input p-3',
                                                 'placeholder': 'متن خود را وارد کنید...'})