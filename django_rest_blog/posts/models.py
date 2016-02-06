from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Post(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("author"))

    title = models.CharField(max_length=200, verbose_name=_("title"))
    slug = models.SlugField(editable=False)
    bodytext = models.TextField(verbose_name=_("message"))

    created = models.DateTimeField(auto_now_add=True, verbose_name=_("post date"))
    modified = models.DateTimeField(null=True, verbose_name=_("modified"))

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ['-created']

    def __unicode__(self):
        return self.title
