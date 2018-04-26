from django.urls import path
from ui_app import views

app_name = 'ui_app'

urlpatterns = [
    # path('', views.answer_list, name='answer_list'), for function view
    path('answer/', views.AnswerListView.as_view(), name='answer_list'),
    # path('answer/<int:pk>', views.AnswerListView.as_view(), name='answer_detail'),
    path('tmpmessage/', views.TmpMessageListView.as_view(), name='tmpmssmage_list'),
    path('messagepanel/', views.messagepanel, name='messagepanel'),
    path('messagepanel2/', views.messagepanel2, name='messagepanel2'),

    path('<int:year>/<int:month>/<int:day>/\<answer>', views.AnswerListView.as_view(), name='answer_detail'),


]
