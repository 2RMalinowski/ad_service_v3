from django.urls import path
from ui_app import views

app_name = 'ui_app'

urlpatterns = [
    path('answer/', views.answer_list, name='answer_list'),
    # path('answer/<int:pk>', views.AnswerListView.as_view(), name='answer_detail'),
    path('tmpmessage/', views.tmp_message_list, name='tmpmssmage_list'),
    path('messagepanel/', views.messagepanel, name='messagepanel'),
    path('<int:year>/<int:month>/<int:day>/\<Answer>', views.answer_list, name='answer_detail'),


]
