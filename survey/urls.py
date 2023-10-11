from django.urls import path

from survey.views import index, count_notification


urlpatterns = [
    path("", index, name="index"),
    path("get-notification/<int:current>/", count_notification, name="get-notification")
]
