from django import forms

from django.forms import ModelForm, formset_factory, ModelChoiceField
from immigrationform.models import Question, MultiChoiceQuestion, Answer, FreeResponseQuestion, MultiChoiceResponse, PolarQuestion, Character, CharMultiResponse, CharPolarResponse


class NameForm(forms.Form):
    name = forms.CharField()


class MultiChoiceQuestionForm(ModelForm):
    answer = ModelChoiceField(queryset=MultiChoiceResponse.objects.all(), required=False)

    class Meta:
        model = MultiChoiceQuestion
        fields = []


class PolarQuestionForm(ModelForm):
    answer = forms.BooleanField(required=False)

    class Meta:
        model = MultiChoiceQuestion
        fields = []
