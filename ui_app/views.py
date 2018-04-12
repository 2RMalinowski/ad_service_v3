from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from django.views.generic import ListView, View
from .models import Answer, MessagePanel, TmpMessage
from django import forms


class MessagePanelView(View):
    queryset = MessagePanel.objects.all()
    context_object_name = 'messagepanel'
    template_name = 'ui_app/messagepanel/messagepanel.html'

    def message_panel(request):
        messagepanels = MessagePanel.objects.all
        return render(request, 'ui_app/messagepanel/messagepanel.html', {'messagepanels': messagepanels})


class AnswerListView(ListView):
    queryset = Answer.objects.all()
    context_object_name = 'answers'
    template_name = 'ui_app/answer/answer_list.html'

    def answer_list(request):
        answers = Answer.objects.all()
        return render(request, 'ui_app/answer/answer_list.html', {'answers': answers})


class TmpMessageListView(ListView):
    queryset = TmpMessage.objects.all()
    context_object_name = 'tmpmessages'
    template_name = 'ui_app/tmpmessage/tmpmessage_list.html'

    def tmp_message_list(request):
        tmpmessages = TmpMessage.objects.all
        return render(request, 'ui_app/tmpmessage/tmpmssmage_list.html', {'tmpmessages': tmpmessages})


# def temppost_list(request):
#     tempposts = TempPost.objects.all()
#     return TemplateResponse(request, 'ui_app/tmpmessage/tmpmessage_list.html', {'tempposts': tempposts})
