from django.shortcuts import render, get_object_or_404
from .models import Answer, TmpMessage


def answer_list(request):
    answers = Answer.objects.all()
    tmpmessages = TmpMessage.objects.all()
    return render(
        request=request,
        template_name='ui_app/answer/answer_list.html',
        context={'answers': answers, 'tmpmsgs': tmpmessages},
    )


def answer_detail(request, year, month, day, answer):
    answer = get_object_or_404(Answer, slug=answer,
                               status='created',
                               created__year=year,
                               created__month=month,
                               created__day=day)
    return render(request,
                  'ui_app/answer/answer_detail.html', {'answer': answer})


def tmp_message_list(request):
    tmpmessages = TmpMessage.objects.all()
    return render(request, 'ui_app/tmpmessage/tmpmssmage_list.html', {'tmpmessages': tmpmessages})


def messagepanel(request):
    messagepanels = TmpMessage.objects.all()
    return render(request, 'ui_app/messagepanel/messagepanel.html', {'messagepanels': messagepanels})


