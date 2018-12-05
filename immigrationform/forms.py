from django import forms

from django.forms import ModelForm, formset_factory, ModelChoiceField
from immigrationform.models import Question, MultiChoiceQuestion, Answer, FreeResponseQuestion, MultiChoiceResponse, PolarQuestion, Character, CharMultiResponse, CharPolarResponse


class MultiChoiceQuestionForm(ModelForm):
    answer = ModelChoiceField(queryset=MultiChoiceResponse.objects.all())

    class Meta:
        model = MultiChoiceQuestion
        fields = []


class PolarQuestionForm(ModelForm):
    answer = forms.BooleanField()

    class Meta:
        model = MultiChoiceQuestion
        fields = []
