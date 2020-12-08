from django import forms
from django.utils.translation import ugettext as _


class MessageForm(forms.Form):
    image = forms.ImageField()
    message = forms.CharField(label='Mensaje', max_length=100)

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        self.fields['image'].widget.attrs.update({'ng-model': 'formData.image'})
        self.fields['message'].widget.attrs.update({'ng-model': 'formData.message'})
        self.fields['message'].widget.attrs.update({'class': 'write_msg'})
        self.fields['message'].widget.attrs.update({'placeholder': _('Escribe un mensaje')})
