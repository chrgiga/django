from django import forms
from .models import Symptom

choices = []
for symptom in Symptom.objects.all():
    choices.append((symptom.id, symptom.symptom_name))


class QuestionForm(forms.Form):
    symptoms = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=choices,
        required=True
    )
