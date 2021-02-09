from django.urls import path
from curriculum.views import StandardListView,SubjectDetailView,LessonDetailView,LessonDataView,LessonCreateView

urlpatterns = [
    path('',StandardListView.as_view(),name='standardlist'),
    path('<slug:slug>/',SubjectDetailView.as_view(),name='subjectdetail'),
    path('<str:standard>/<slug:slug>/',LessonDetailView.as_view(),name='lessondetail'),
    path('<str:standard>/<str:slug>/create/',LessonCreateView.as_view(),name='lessoncreate'),
    path('<str:standard>/<str:subject>/<slug:slug>/',LessonDataView.as_view(),name='lessondata'),
    
    


]
