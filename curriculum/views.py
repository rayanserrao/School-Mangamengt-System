from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,ListView,FormView,CreateView,UpdateView,DeleteView 
from curriculum.models import Standard,Subject,Lessons
from curriculum.forms import LessonForm

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

class LessonCreateView(CreateView):
    model = Subject
    form_class = LessonForm
    context_object_name= 'subject'
    template_name = 'lessoncreate.html'
