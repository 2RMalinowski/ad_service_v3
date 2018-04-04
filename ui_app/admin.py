from django.contrib import admin
from .models import Answer, TmpMessage


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created')
    list_filter = ('title', 'created')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created'
    ordering = ['title', 'created']


admin.site.register(Answer, AnswerAdmin)


class TmpMessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'message_author', 'created')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created'


admin.site.register(TmpMessage, TmpMessageAdmin)
