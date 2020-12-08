from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext as _

User = get_user_model()

class Message(models.Model):
    author = models.ForeignKey(User, verbose_name=_("Autor"), blank=True, db_index=True, null=True, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Fecha de publicación'))
    image_file = models.ImageField(upload_to='images', null=True, blank=True, verbose_name=_("Imagen"))
    message = models.TextField(null=True, blank=True, verbose_name=_("Mensaje"))
