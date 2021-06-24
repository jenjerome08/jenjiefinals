from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('data/', views.data, name='data'),

    path('respondent/<str:pk_test>/', views.respondent, name="respondent"),


    path('create_assessment/', views.createAssessment, name="create_assessment"),
    path('create_respondent/', views.createRespondent, name="create_respondent"),
    path('create_predictor/', views.createRelation, name="create_predictor"),
    path('create_symptom/', views.createSymptoms, name="create_symptom"),

    path('questionnaire/', views.createQuestionnaires, name="questionnaire"),


    path('update_assessment/<str:pk>/', views.updateAssessment, name="update_assessment"),
    path('delete_assessment/<str:pk>/', views.deleteAssessment, name="delete_assessment"),
    path('update_respondent/<str:pk>/', views.updateRespondent, name="update_respondent"),
    path('delete_respondent/<str:pk>/', views.deleteRespondent, name="delete_respondent"),


]