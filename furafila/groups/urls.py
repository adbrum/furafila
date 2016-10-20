from django.conf.urls import url
from furafila.groups.views import new, detail

urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^(\d+)/$', detail, name='detail'),
]