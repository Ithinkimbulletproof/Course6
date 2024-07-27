from django.contrib import admin
from .models import Client, Message, Mailing, Attempt


class ClientAdmin(admin.ModelAdmin):
    list_display = ("email", "full_name", "comment")
    search_fields = ("email", "full_name")
    list_filter = ("comment",)


class MessageAdmin(admin.ModelAdmin):
    list_display = ("subject",)
    search_fields = ("subject",)


class MailingAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "first_send_time", "periodicity", "message")
    list_filter = ("status", "periodicity")
    search_fields = ("status", "message__subject")


class AttemptAdmin(admin.ModelAdmin):
    list_display = ("mailing", "attempt_time", "status")
    list_filter = ("status",)
    search_fields = ("mailing__status",)


admin.site.register(Client, ClientAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Mailing, MailingAdmin)
admin.site.register(Attempt, AttemptAdmin)
