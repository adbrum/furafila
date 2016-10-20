from django.contrib import admin
from furafila.core.models import Service, Ticket, AccessPoint, WorkGroup


class TicketModelAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'created_at')
    fields = ('ticket', 'service')
    date_hierarchy = 'created_at'
    search_fields = ('ticket', 'service', 'created_at')
    list_filter = ('created_at',)

    #remover o botão add
    def get_form(self, request, obj=None, **kwargs):  # Just added this override
        form = super(TicketModelAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['service'].widget.can_add_related = False
        return form


# admin.site.register(Counter)
# admin.site.register(Attendance)
# admin.site.register(Position)
admin.site.register(AccessPoint)
admin.site.register(WorkGroup)
# admin.site.register(Priority)
admin.site.register(Service)
admin.site.register(Ticket, TicketModelAdmin)
