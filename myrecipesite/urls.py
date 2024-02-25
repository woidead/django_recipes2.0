from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from myrecipesite.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("recipes.urls")),
    path('users/', include("users.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)