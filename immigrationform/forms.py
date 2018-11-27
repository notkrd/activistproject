from django.forms import ModelForm
from immigrationform.models import Question, Answer, FreeResponse, MultiChoiceResponse


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']


class FreeQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'current_answer']


class MultiChoiceQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'current_answer']


class PolarQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'current_answer']


