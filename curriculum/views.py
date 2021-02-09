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
    # form_class = CommentForm
    # second_form_class =  ReplyForm

    # ''' send two forms to page
    #   cehck which is posted
    #   take action on theform whivh isn posted '''

    # def get_context_data(self,**kwargs):
    #     context = super(LessonDataView,self).self.get_context_data(**kwargs)
    #     if 'form' not in  context:
    #         context['form'] = self.form_class(request = self.request)

    #     if  'form2' not in context:
    #         context['form2'] = self.second_form_class(request = self.request)


    #     return context
        

    # def post(self,request,*args,**kwargs):

    #     self.object = self.get_object()
    #     if 'form' in request.POST:
    #         form_class = self.get_form_class()
    #         form_name = 'form'

    #     else:
    #         form_class = self.second_form_class
    #         form_name = 'form2'

    #     form = self.get_form(form_class)

    #     if form_name == 'form' and form.is_valid():
    #         print('Comment form is returned')
    #         return self.form_valid(form)

    #     elif form_name == 'form2' and form.is_valid():
    #         print("reply form is retuerned")
    #         return self.form2_valid(form)

        
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
