from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from django.views.generic import ListView, View
from .models import Answer, MessagePanel, TmpMessage
# from . forms import MessagePanelForm


class AnswerListView(ListView):
    queryset = Answer.objects.all()
    context_object_name = 'answers'
    template_name = 'ui_app/answer/answer_list.html'

    def answer_list(request):
        answers = Answer.created.all()
        return render(request, 'ui_app/answer/answer_list.html', {'answers': answers})

    # def answer_detail(request, pk):
    #     answer = get_object_or_404(Answer, pk=pk)
    #     return render(request, 'ui_app/answer/answer_detail.html', {'answer': answer})

    def answer_detail(request, year, month, day, answer):
        answer = get_object_or_404(Answer, slug=answer,
                                   status='created',
                                   created__year=year,
                                   created__month=month,
                                   created__day=day)
        return render(request,
                      'ui_app/answer/answer_detail.html', {'answer': answer})


class TmpMessageListView(ListView):
    queryset = TmpMessage.objects.all()
    context_object_name = 'tmpmessages'
    template_name = 'ui_app/tmpmessage/tmpmessage_list.html'

    def tmp_message_list(request):
        tmpmessages = TmpMessage.objects.all
        return render(request, 'ui_app/tmpmessage/tmpmssmage_list.html', {'tmpmessages': tmpmessages})


# class MessagePanelView(View):
#     queryset = MessagePanel.objects.all()
#     context_object_name = 'messagepanel'
#     template_name = 'ui_app/messagepanel/messagepanel.html'
#
#     def message_panel(self, request):
#         messagepanels = TmpMessage.objects.all().order_by()
#         return render(request, 'ui_app/messagepanel/messagepanel.html', {'messagepanels': messagepanels})


def messagepanel(request):
    messagepanels = TmpMessage.objects.all()
    return render(request, 'ui_app/messagepanel/messagepanel.html', {'messagepanels': messagepanels})


