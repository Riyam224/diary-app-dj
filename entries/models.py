from tkinter.tix import Tree
from django.db import models

# Create your models here.
from django.utils.translation import gettext as _
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


class Entry(models.Model):
    text = models.TextField(_("text"))
    date_added = models.DateTimeField(_("date added"), default=timezone.now)
    slug = models.SlugField(_("slug") , blank=Tree , null=Tree)

    

    class Meta:
        verbose_name = _("Entry")
        verbose_name_plural = _("Entries")

    def __str__(self):
        return self.text

    def save(self , *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.text)
        return super(Entry , self).save(*args, **kwargs)
