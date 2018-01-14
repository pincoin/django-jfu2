from django.contrib import admin

from .models import Attachment


class AttachmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Attachment, AttachmentAdmin)
