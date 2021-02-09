from django.shortcuts import render,redirect
from django.views.generic import TemplateView,DetailView,ListView,FormView,CreateView,UpdateView,DeleteView 
from curriculum.models import Standard,Subject,Lessons
from curriculum.forms import LessonForm
from django.urls import reverse_lazy

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


    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.standard
        return reverse_lazy('lessondetail',kwargs={'standard':standard.slug,'slug':self.object.slug})

    #validating forms
    def form_valid(self,form,*args,**kwargs):
        self.object = self.get_object() # object of subject model
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.standard = self.object.standard
        fm.subject = self.object
        fm.save()
        return redirect(self.get_success_url())

class LessonUpdateview(UpdateView):
    fields = ['name','position','video','ppt','notes']
    model = Lessons
    template_name = 'lessonupdate.html'
    context_object_name = 'lessons'

class LessonDeleteView(DeleteView):
    model = Lessons
    context_object_name = 'lessons'
    template_name='lessondelete.html'

    def get_success_url(self):
        standard = self.object.standard
        subject = self.object.subject
        return reverse_lazy('lessondetail',kwargs={'standard':standard.slug,'slug':subject.slug})
