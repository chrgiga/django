from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Question, Symptom
from .forms import QuestionForm
from .utils.diagnostic import Diagnostic


class HomePageView(generic.TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['welcome_message'] = 'Welcome to the health questionnaire'
        return context


def question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    form_fields = QuestionForm()
    return render(request, 'main/question.html', {
        'question': question,
        'form_fields': form_fields,
    })


def validate(request, pk):
    current_question = get_object_or_404(Question, pk=pk)
    form_fields = request.POST.getlist('symptoms')

    if not form_fields:
        return render(request, 'main/question.html', {
            'question': current_question,
            'error_message': "You didn't select a symptom.",
        })
    else:
        symptoms_ids = [int(symptom_id) for symptom_id in form_fields]
        symptoms = Symptom.objects.filter(pk__in=symptoms_ids)
        diagnostic = Diagnostic.get_diagnostic(Diagnostic(), symptoms)
        return render(request, 'main/question_result.html', {
            'question': current_question,
            'selected_symptoms': symptoms,
            'diagnostic': diagnostic,
        })

