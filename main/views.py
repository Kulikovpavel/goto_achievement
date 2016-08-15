from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView

from main.models import Student, Achievement, Record


class StudentView(DetailView):
    model = Student
    context_object_name = "student"


class AchievementView(DetailView):
    model = Achievement
    context_object_name = "achievement"


class AchievementListView(ListView):
    model = Achievement
    context_object_name = "achievement_list"


def index_view(request):
    context = dict()
    context['students'] = Student.objects.all()
    context['records'] = Record.objects.all()
    return render(request, 'main/index.html', context=context)
