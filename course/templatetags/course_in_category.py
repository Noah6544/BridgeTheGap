from django import template
register = template.Library()

from course.models import Chapter, Topic

@register.filter  # code from stack overflow but it cool
def in_category(ch,topicins): #LEAVE AS ch. cuz then it's basicallly a blank argument and just uses the 2nd topic and not the first. please. this was a dumb bug that took me a minute to resolve
    #i resolved it 100% by accident by not using the first argument
    return Chapter.objects.filter(topic=topicins)