from django import forms
from curriculum.models import Lessons

class LessonForm(forms.ModelForm):
    class Meta:
            
        model = Lessons
        fields = ['lesson_id','name','position','video','ppt','notes']