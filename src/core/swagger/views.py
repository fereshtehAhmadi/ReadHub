from django.conf.urls.i18n import i18n_patterns
from drf_spectacular.views import SpectacularAPIView


class ApiSchemaView(SpectacularAPIView):
    patterns = i18n_patterns()
