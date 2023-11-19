from django.urls import path, include

from .views import *

urlpatterns = [
    # path("", tools, name="tuls")
    # path("", ToolsView.as_view(), name="tuls")
    path("", ToolsTemplateView.as_view(), name="tuls"),
    path("abc/", include("abc_model.urls")),
]
