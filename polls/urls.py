from django.urls import path
from . import views


app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5
    path('<int:pk>/', views.DetailView.as_view(), name='poll_detail'),
    # ex: /polls/5/results
    path('<int:pk>/results/', views.ResultView.as_view(), name='poll_results'),
    # ex: /polls/5/votes
    path('<int:question_id>/vote/', views.vote, name='poll_votes')
]
