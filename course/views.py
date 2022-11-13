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
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.views import generic
from django.http import Http404
from .models import Chapter, ImportantInstructionContent, Question, Choice, Topic

# Create your views here.
# class IndexView(generic.ListView):
#     template_name = 'course/base.html'
#     context_object_name = 'Instruction_Chapters'
#
#     de get_con
#     def get_queryset(self):
#         Chapters = Chapter.objects.all().order_by('id')
#         return # #old in#old index view

error_message = "One of the following occured: \n1.) You Navigated Too Far Back \n2.) We're Still Working On This. Please be patient with us"
class IndexView(generic.ListView):
    template_name = 'course/base.html'
    context_object_name = 'Chapters'



    def get_queryset(self):
        return Topic.objects.all().order_by('id')


def IndexViewa(request):

    topics = Topic.objects.all().order_by('id')

    return render(request,'course/base.html',{'Topicclass':Topic,'Chapter':Chapter,'topiclist':topics})



# return render(request, 'course/base.html',context={})
def LoginRedirect(request):
    return render(request,'course/login_redirect.html',context={})

def subtract(first,last):
    return first-last
def add(first,last):
    return first+last

@login_required
def ChapterView(request,chapter_id):
    try:
        print("chapter.id" + str(chapter_id))

        CurrentChapter = Chapter.objects.get(pk=chapter_id)
        InstructionImportant = ImportantInstructionContent.objects.filter(chapter=CurrentChapter)
        object = "Chapter"

    except (KeyError, Chapter.DoesNotExist):
        return render(request,'course/ObjectDoesNotExist.html',{'object':'Chapter','error_message':error_message})
    else:
        # Always return an HttpResponseRedirect after successfully decmdaling
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render(request, 'course/chapter_base.html',{'Chapter':CurrentChapter,
                                                           'ImportantInstructionContent':InstructionImportant})

@login_required
def QuizView(request,chapter_id):
    try:
        CurrentChapter = Chapter.objects.get(id=chapter_id)
        QuizQuestion = Question.objects.get(chapter=CurrentChapter)

    except (KeyError, Question.DoesNotExist):
        return(render(request,'course/ObjectDoesNotExist.html',{'object':'Quiz','error_message':error_message}))
    else:
        return render(request, 'course/question_base.html',{'question':QuizQuestion,'chapter':CurrentChapter})

@login_required
def ResultsView(request,chapter_id):
    print(request.POST)
    user = User.objects.get(pk=chapter_id)
    CurrentChapter = Chapter.objects.get(pk=chapter_id)

    QuizQuestion = Question.objects.get(chapter=CurrentChapter)

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

            return render(request, 'course/results_base.html',{'question':QuizQuestion,'selected_choice':selected_choice,'chapter':CurrentChapter})

        elif selected_choice.correct_choice == False:
            return render(request, 'course/results_base.html',{'question':QuizQuestion,'selected_choice':selected_choice,'chapter':CurrentChapter})

