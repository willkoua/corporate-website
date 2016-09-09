from django.conf.urls import url, patterns
from pages import views

urlpatterns = patterns(
    '',
    url(
        r'^$',
        views.Home.as_view(),
        name='home'
    ),
)