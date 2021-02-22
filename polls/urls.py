from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.home, name='home'),
    path('poll/', views.index, name='index'),
    path('poll/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('poll/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('poll/<int:question_id>/vote/', views.vote, name='vote'),
]