from django.conf.urls import url, include
from django.contrib import admin
from furafila.core.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'triagem/', include('furafila.screening.urls', namespace='screening')),
    url(r'senha/', include('furafila.tickets.urls', namespace='ticket')),
    url(r'pontoacesso/', include('furafila.accesspoint.urls', namespace='accesspoint')),
    url(r'grupo/', include('furafila.groups.urls', namespace='group')),
    url(r'^admin/', admin.site.urls),
]
