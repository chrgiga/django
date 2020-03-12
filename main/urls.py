from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('question/<int:pk>', views.question, name='question'),
    path('question/<int:pk>/validate', views.validate, name='question_validate'),
]

