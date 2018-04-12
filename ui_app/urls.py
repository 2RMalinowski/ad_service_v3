from django.urls import path
from ui_app import views

app_name = 'ui_app'

urlpatterns = [
    # path('', views.answer_list, name='answer_list'), for function view
    path('answer/', views.AnswerListView.as_view(), name='answer_list'),
    path('tmpmessage/', views.TmpMessageListView.as_view(), name='tmpmssmage_list'),
    path('messagepanel/', views.MessagePanelView.as_view(), name='messagepanel'),
    # path('<int:year>/<int:month>/<int:day>/\<answer>', views.answer_list, name='answer_list'),


]
