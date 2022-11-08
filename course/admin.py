from django.contrib import admin

from django.contrib import admin
from .models import Question, Choice, Chapter, ImportantInstructionContent
from django.forms import TextInput, Textarea
from django.db import models




class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4 # this adds extra possible slots, to add another this is default # of options

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question Information", {'fields': ['question_text','chapter','explanation']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),

    ]

    inlines = [ChoiceInline]

    list_display = ('question_text',)
    list_filter = ['pub_date']
    search_fields = ['question_text']


class ImportantInstructionContentInLine(admin.TabularInline):
    model = ImportantInstructionContent


    extra = 2
class InstructionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['title']}),
        ('Instruction Content:', {'fields': ['chapter_covers','completed','content','summary']}),
       # ('Important Instructions / Notes',{'fields':})

    ]
    inlines = [ImportantInstructionContentInLine]

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '140'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 30, 'cols': 130})},
    }


admin.site.register(Question, QuestionAdmin)
admin.site.register(Chapter, InstructionAdmin)
