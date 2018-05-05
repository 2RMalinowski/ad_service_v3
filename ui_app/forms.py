from django import forms
from .models import ANSWER_CHOICES, MessagePanel, Answer


class MessagePanelForm(forms.ModelForm):

    class Meta:
        model = MessagePanel
        fields = 'answer_box'
        widgets = {
            "answer": forms.CharField()
        }


class AnswerForm(forms.Form):
    answers = forms.ModelMultipleChoiceField(label="choose answer",
                                             choices=ANSWER_CHOICES,
                                             queryset=Answer.objects.all(),
                                             widget=forms.SelectMultiple())

    # class Meta:
    #     model = Answer
    #     fields = 'body'


# class MessagePanelForm(forms.Form):
#     answers = forms.ModelMultipleChoiceField(label="choose answer",
#                                              queryset=Answer.objects.all(),
#
