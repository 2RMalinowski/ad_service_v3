from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('answer/', include('ui_app.urls', namespace='answer')),
    path('tmpmessage/', include('ui_app.urls', namespace='tmpmessage'))

]

