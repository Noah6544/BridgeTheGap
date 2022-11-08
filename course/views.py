from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.urls import reverse
from django.views import generic
from django.http import Http404
from .models import Chapter, ImportantInstructionContent, Question, Choice

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'course/base.html'
    context_object_name = 'Instruction_Chapters'

    def get_queryset(self):
        return Chapter.objects.all().order_by('id')


# return render(request, 'course/base.html',context={})

def subtract(first,last):
    return first-last
def add(first,last):
    return first+last
def ChapterView(request,chapter_id):
    print(chapter_id)
    CurrentChapter = Chapter.objects.get(id=chapter_id)
    InstructionImportant = ImportantInstructionContent.objects.filter(chapter=CurrentChapter)


    # Always return an HttpResponseRedirect after successfully decmdaling
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return render(request, 'course/chapter_base.html',{'Instruction':CurrentChapter,
                                                       'ImportantInstructionContent':InstructionImportant})
def QuizView(request,Quiz_id):
    print(Quiz_id)
    print("hey")
    QuizQuestion = Question.objects.get(id=Quiz_id)
    return render(request, 'course/question_base.html',{'question':QuizQuestion
                                                        })

def ResultsView(request,Quiz_id):
    CurrentChapter = Chapter.objects.get(pk=Quiz_id)
    QuizQuestion = Question.objects.get(pk=Quiz_id)
    ChoiceOptions = Choice.objects.filter(question=QuizQuestion) # took me awhile to understand filter, but i thought that this was necessary to check if the asnwer is right or not, its not necessary

    try:
        selected_choice = QuizQuestion.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'course/question_base.html',{'question':QuizQuestion,
                                                           'error_message':"You didn't select a choice."})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        CurrentChapter.completed = True
        CurrentChapter.save()

        if selected_choice.correct_choice == True:
            print("the selected choice: " + str(selected_choice) + "Is true")

            return render(request, 'course/results_base.html',{'question':QuizQuestion,'selected_choice':selected_choice,
                                                               'Quiz_id':Quiz_id},)

        elif selected_choice.correct_choice == False:
            return render(request, 'course/results_base.html',{'question':QuizQuestion,'selected_choice':selected_choice,
                                                               'Quiz_id':Quiz_id},)

