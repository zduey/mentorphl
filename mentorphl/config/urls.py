from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^profile/', include('profiles.urls', namespace="profiles")),
    url(r'^matchmaker/', include('matchmaker.urls', namespace='matchmaker')),
    url(r'^$', include('urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
