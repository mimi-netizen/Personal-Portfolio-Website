from django.contrib import admin
#from users import views
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from django.urls import include, path
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve media files in both development and production
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += [
        re_path(r'^favicon\.ico$', serve, {
                'document_root': settings.STATIC_ROOT,
                'path': 'favicon.ico',
            }
        ),
    ]
