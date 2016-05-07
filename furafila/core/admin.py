from django.contrib import admin
from furafila.core.models import Counter, Attendance, Position, AccessPoint, Priority, Service

admin.site.register(Counter)
# admin.site.register(Attendance)
admin.site.register(Position)
admin.site.register(AccessPoint)
admin.site.register(Priority)
admin.site.register(Service)