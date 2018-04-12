from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ui_app.urls', namespace='answer')),
    path('', include('ui_app.urls', namespace='tmpmessage')),
    path('', include('ui_app.urls', namespace='messagepanel')),

]

