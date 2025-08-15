from drf_spectacular.views import SpectacularAPIView

class ApiSchemaView(SpectacularAPIView):
    patterns = i18n_patterns()
