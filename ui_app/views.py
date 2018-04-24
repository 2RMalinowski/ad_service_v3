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
        answers = Answer.objects.all()
        return render(request, 'ui_app/answer/answer_list.html', {'answers': answers})

    def answer_detail(request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        return render(request, 'ui_app/answer/answer_detail.html', {'answer': answer})


class TmpMessageListView(ListView):
    queryset = TmpMessage.objects.all()
    context_object_name = 'tmpmessages'
    template_name = 'ui_app/tmpmessage/tmpmessage_list.html'

    def tmp_message_list(request):
        tmpmessages = TmpMessage.objects.all
        return render(request, 'ui_app/tmpmessage/tmpmssmage_list.html', {'tmpmessages': tmpmessages})


# class MessagePanelView(View):
#
#     def message_panel(request):
#         messagepanels = MessagePanel.objects.all().order_by()
#         return render(request, 'ui_app/messagepanel/messagepanel.html', {'messagepanels': messagepanels})


def messagepanel(request):
    tmpmessages = TmpMessage.objects.all()
    return render(request, 'ui_app/messagepanel/messagepanel.html', {'tmpmessages': tmpmessages})


def messagepanel2(request):
    messagepanels = TmpMessage.objects.all()
    return render(request, 'ui_app/messagepanel/messagepanel2.html', {'messagepanels': messagepanels})


# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog_app/post_edit.html', {'form': form})
#
#
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog_app/post_detail.html', {'post': post})
