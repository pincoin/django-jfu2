from django.contrib import admin

from .models import Attachment


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content_type', 'object_id')


admin.site.register(Attachment, AttachmentAdmin)
