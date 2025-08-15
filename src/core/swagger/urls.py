from django.urls import path
from django.urls.resolvers import URLPattern, URLResolver
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView

from core.swagger.views import (ApiSchemaView)

swagger_urlpatterns: list[URLPattern | URLResolver] = [
    # api services
    path(
        "api/schema/",
        ApiSchemaView.as_view(),
        name="schema",
    ),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
