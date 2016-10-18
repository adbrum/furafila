from django.conf.urls import url
from furafila.tickets.views import new, detail, counter

urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^(\d+)/$', detail, name='detail'),
]