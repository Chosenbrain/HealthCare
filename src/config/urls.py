from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('pages/', include('pages.urls')),
    path('', RedirectView.as_view(url='pages/')),

]

if settings.DEBUG:
    urlpatterns += static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns



