from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^mentors/', include('mentors.urls', namespace="mentor")),
    url(r'^$', include('urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
