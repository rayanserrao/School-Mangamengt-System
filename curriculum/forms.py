from django import forms
from curriculum.models import Lessons

class LessonForm(forms.ModelForm):
    class Meta:
            
        model = Lessons
        fields = ['lesson_id','name','position','video','ppt','notes']

# class CommentForm(Comment):
#     class Meta:
#         model = Comment
#         fields = ['body']
#         labels = {'body':'comment'}
#         widgets = {'body':forms.Textarea(attrs={'class':'form-control','rows':4,'cols':70,'placeholder':'Enter your comment'})}


# class ReplyForm(Reply):
#     class Meta:
#         model = Reply
#         fields = ['reply_body']
#         labels = {'reply_body':'reply'}
#         widgets = {'reply_body':forms.Textarea(attrs={'class':'form-control','rows':4,'cols':70,'placeholder':'Enter your reply'})}

