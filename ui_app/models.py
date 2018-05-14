from django.db import models
from django.urls import reverse
from django.utils import timezone


class Answer(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=300, unique_for_date='created')
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    objects = models.Manager()

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('ui_app:answer_detail  ',
    #                    args=[self.created, self.slug])

    def get_absolute_url(self):
        return reverse('ui_app:answer_detail',
                       args=[self.created.year,
                             self.created.strftime('%m'),
                             self.created.strftime('%d'),
                             self.slug])


class TmpMessage(models.Model):
    user = models.CharField(max_length=50)
    advert_title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300, unique_for_date='created')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    objects = models.Manager()

    class Meta:
        ordering = ('created',)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.advert_title


# class MessageManager(models.Manager):
#     def get_queryset(self):
#         return super(MessageManager, self).get_queryset().filter(status='unread')


ANSWER_CHOICES = (
    ('answer_this_wk', 'this_week'),
    ('answer_this_wk<18', 'this_week<18'),
    ('answer_mr_this_wk', 'mr_this_week'),
    ('answer_ms_this_wk', 'ms_this_week'),
    ('answer_next_wk', 'next_week'),
    ('answer_next_wk<18', 'next_week<18'),
    ('answer_mr_next_wk', 'mr_next_week'),
    ('answer_ms_next_wk', 'ms_next_week'),
    ('answer_other_term', 'other_term'),
    ('answer_other_term_mr', 'mr_other_term'),
    ('answer_other_term_ms', 'ms_other_term'),
    ('answer_office', 'office'),
    ('invitation_m_orday', 'inv_m'),
    ('invitation_m_wknday', 'inv_m_wknd'),
    ('invitation_f_orday', 'inv_f'),
    ('invitation_f_wknday', 'inv_f_wknd'),
    ('invitation_mr_orday', 'inv_mr'),
    ('invitation_mr_wknday', 'inv_mr_wknd'),
    ('invitation_ms_orday', 'inv_ms'),
    ('invitation_ms_wknday', 'inv_ms_wknd'),
    ('invitation_scnd', 'inv_rptd'),
    ('invitation_mr_scnd', 'inv_mr_rptd'),
    ('invitation_ms_scnd', 'inv_ms_rptd'),
)


class MessagePanel(models.Model):
    post = TmpMessage.objects.all()
    answer_txt = models.TextField(blank=True)
    # answer_txt = Answer.body
    selected = models.BooleanField(default=False)
    trash = models.BooleanField(default=False)
    ans_choice = models.TextField(choices=ANSWER_CHOICES, default='ans_this_wk')
    answer_box = models.TextField(verbose_name="content")

    # date = models.DateTimeField(default=timezone.now)

    # class Meta: ordering = ('created',)

    def __str__(self):
        return self.answer_box
