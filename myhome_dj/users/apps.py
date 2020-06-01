from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "myhome_dj.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import myhome_dj.users.signals  # noqa F401
        except ImportError:
            pass
