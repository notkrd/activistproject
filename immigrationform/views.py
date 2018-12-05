from django.shortcuts import render
from django.http import HttpResponse
from django.forms import formset_factory, modelformset_factory

from .forms import MultiChoiceQuestionForm, PolarQuestionForm
from .models import MultiChoiceQuestion, PolarQuestion, Question, MultiChoiceResponse
from random import sample

# Create your views here.


def index(request, num_mc = 20, num_polar = 20):
    some_mcs = MultiChoiceQuestion.objects.order_by('?')[:num_mc]
    some_ps = MultiChoiceQuestion.objects.order_by('?')[:num_polar]

    MultiChoiceFormset = modelformset_factory(MultiChoiceQuestion, form=MultiChoiceQuestionForm, extra=0)
    PolarFormset = modelformset_factory(PolarQuestion, form=PolarQuestionForm, extra=0)

    if request.method == 'POST':
        mc_formset = MultiChoiceFormset(request.POST, request.FILES, prefix='mc')
        polar_formset = PolarFormset(request.POST, request.FILES, prefix='polar')

        if mc_formset.is_valid() and polar_formset.is_valid():
            return HttpResponse(request)

    else:
        mc_formset = MultiChoiceFormset(queryset=some_mcs, prefix='mc')
        for form in mc_formset:
            form.fields['answer'].label = form.instance.question_text
            form.fields['answer'].queryset = MultiChoiceResponse.objects.filter(for_question=form.instance)

        polar_formset = PolarFormset(queryset=some_ps, prefix='polar')
        for form in polar_formset:
            form.fields['answer'].label = form.instance.question_text

        return render(request, 'immigrationform/character_form.html', {'mc_formset': mc_formset, 'polar_formset': polar_formset})
