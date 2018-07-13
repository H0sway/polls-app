# Import modules
from django.urls import path
from . import views

app_name = 'polls'
app_name = 'polls'
urlpatterns = [
    # All polls
    path('', views.IndexView.as_view(), name='index'),
    # Single poll
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # Results for a single poll
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # Vote on a poll
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
