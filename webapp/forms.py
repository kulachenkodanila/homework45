from django import forms
from django.forms import widgets

from webapp.models import status_choices


class To_DoForm(forms.Form):
    description = forms.CharField(max_length=100, required=True, label='Description')
    status = forms.ChoiceField(choices=status_choices, label='Status')
    d_date = forms.DateField(label="дата сдачи")
    title = forms.CharField(max_length=1000, required=True, label='Title',
                              widget=widgets.Textarea(attrs={"cols": 40, "rows": 3}))


