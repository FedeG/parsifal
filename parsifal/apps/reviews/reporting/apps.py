from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ReportingConfig(AppConfig):
    name = "parsifal.apps.reviews.reporting"
    verbose_name = _("Reviews: Reporting")
