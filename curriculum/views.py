from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,ListView,FormView
from curriculum.models import Standard,Subject,Lessons

# Create your views here.
class StandardListView(ListView):
    model = Standard
    context_object_name='standards'
    template_name = 'standardlist.html'

class SubjectDetailView(DetailView):
    model= Standard
    context_object_name='standards'
    template_name = 'subjectdetail.html'

class LessonDetailView(DetailView):
    model= Subject
    context_object_name='subjects'
    template_name = 'lessondetail.html'

class LessonDataView(DetailView):
    model = Lessons
    context_object_name='lessons'
    template_name='lessondata.html'
