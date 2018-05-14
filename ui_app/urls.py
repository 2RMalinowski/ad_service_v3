from django.urls import path
from ui_app import views

app_name = 'ui_app'

urlpatterns = [
    path('answer/', views.answer_list, name='answer_list'),
    path('tmpmessage/', views.tmp_message_list, name='tmpmssmage_list'),
    path(r'', views.messagepanel, name='messagepanel'),
    path('<int:year>/<int:month>/<int:day>/\<Answer>', views.answer_list, name='answer_detail'),

]
