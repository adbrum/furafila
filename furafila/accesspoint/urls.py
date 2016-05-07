from django.conf.urls import url
from furafila.accesspoint.views import new

urlpatterns = [
    url(r'^$', new, name='new'),

]