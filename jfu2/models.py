from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractAttachment(models.Model):
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('file name'),
    )

    file = models.FileField(
        verbose_name=_('uploaded file'),
        upload_to="attachment",
    )

    created = models.DateTimeField(
        verbose_name=_('created time'),
        auto_now_add=True,
    )

    class Meta:
        abstract = True


class Attachment(AbstractAttachment):
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        verbose_name=_('content type'),
        related_name='%(app_label)s_%(class)s_attachments',
    )

    content_object = GenericForeignKey()

    object_id = models.IntegerField(
        verbose_name=_('object id'),
        db_index=True,
    )

    class Meta:
        verbose_name = _('attachment')
        verbose_name_plural = _('attachments')
        app_label = 'jfu2'
        index_together = [
            ["content_type", "object_id"],
        ]
        ordering = ['-created']
