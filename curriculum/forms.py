from django import forms
from curriculum.models import Lessons

class LessonForm(forms.ModelForm):
    class Meta:
            
        model = Lessons
        fields = ('__all__')