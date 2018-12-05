from django.shortcuts import render
from django.http import HttpResponse
from django.forms import formset_factory, modelformset_factory

from .forms import MultiChoiceQuestionForm, PolarQuestionForm
from .models import MultiChoiceQuestion, PolarQuestion, Question, MultiChoiceResponse

# Create your views here.


def index(request):
    MultiChoiceFormset = modelformset_factory(MultiChoiceQuestion, form=MultiChoiceQuestionForm, extra=0)
    PolarFormset = modelformset_factory(PolarQuestion, form=PolarQuestionForm, extra=0)

    if request.method == 'POST':
        return HttpResponse(request)

    else:
        mc_formset = MultiChoiceFormset()
        for form in mc_formset:
            form.fields['answer'].label = form.instance.question_text
            form.fields['answer'].queryset = MultiChoiceResponse.objects.filter(for_question=form.instance)

        polar_formset = PolarFormset()
        for form in polar_formset:
            form.fields['answer'].label = form.instance.question_text

    return render(request, 'immigrationform/character_form.html', {'mc_formset': mc_formset, 'polar_formset': polar_formset})
