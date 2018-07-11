# Import modules
from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # All polls
    path('', views.index, name='index'),
    # Single poll
    path('<int:question_id>/', views.detail, name='detail'),
    # Results for a single poll
    path('<int:question_id>/results/', views.results, name='results'),
    # Vote on a poll
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
