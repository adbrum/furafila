from django.contrib import admin
from furafila.core.models import Service, Ticket


class TicketModelAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'created_at')


# admin.site.register(Counter)
# admin.site.register(Attendance)
# admin.site.register(Position)
# admin.site.register(AccessPoint)
# admin.site.register(Priority)
admin.site.register(Service)
admin.site.register(Ticket, TicketModelAdmin)
