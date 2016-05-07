from django.conf.urls import url
from furafila.screening.views import new

urlpatterns = [
    url(r'^$', new, name='new'),

]