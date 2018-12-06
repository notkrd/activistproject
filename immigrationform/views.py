from django.shortcuts import render
from django.http import HttpResponse
from django.forms import formset_factory, modelformset_factory

from .forms import MultiChoiceQuestionForm, PolarQuestionForm, NameForm
from .models import MultiChoiceQuestion, PolarQuestion, Question, MultiChoiceResponse, Character, CharMultiResponse, CharPolarResponse
from random import sample

# Create your views here.


def index(request, num_mc = 20, num_polar = 20):
    some_mcs = MultiChoiceQuestion.objects.order_by('?')[:num_mc]
    some_ps = PolarQuestion.objects.order_by('?')[:num_polar]

    MultiChoiceFormset = modelformset_factory(MultiChoiceQuestion, form=MultiChoiceQuestionForm, extra=0)
    PolarFormset = modelformset_factory(PolarQuestion, form=PolarQuestionForm, extra=0)

    if request.method == 'POST':
        name_form = NameForm(request.POST, prefix='charname')
        mc_formset = MultiChoiceFormset(request.POST, request.FILES, prefix='mc')
        polar_formset = PolarFormset(request.POST, request.FILES, prefix='polar')

        if mc_formset.is_valid() and polar_formset.is_valid() and name_form.is_valid():
            mcd = mc_formset.cleaned_data
            pd = polar_formset.cleaned_data
            charname = name_form.cleaned_data

            char = Character.objects.create(name=charname)

            for mc in mcd:
                the_a = mc['answer']
                if the_a:
                    an_r = CharMultiResponse.objects.create(by_character=char, with_response=the_a)

            for plr in pd:
                a_parent = plr['question_ptr']
                the_q = PolarQuestion.objects.get(question_ptr=a_parent)
                the_a = plr['answer']
                an_r = CharPolarResponse.objects.create(by_character=char, for_question=the_q, with_response=the_a)

            return HttpResponse(char.str_attributes())
        else:
            return HttpResponse("Something has gone wrong. Please try again in 4 months.")

    else:
        name_form = NameForm(prefix="charname")

        mc_formset = MultiChoiceFormset(queryset=some_mcs, prefix='mc')
        for form in mc_formset:
            form.fields['answer'].label = form.instance.question_text
            form.fields['answer'].queryset = MultiChoiceResponse.objects.filter(for_question=form.instance)

        polar_formset = PolarFormset(queryset=some_ps, prefix='polar')
        for form in polar_formset:
            form.fields['answer'].label = form.instance.question_text

        return render(request, 'immigrationform/character_form.html', {'mc_formset': mc_formset, 'polar_formset': polar_formset, 'name_form': name_form})
