from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# import debug_toolbar # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('__debug__/', include(debug_toolbar.urls)),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls', namespace='core')),
]

# Check if the DEBUG mode is enabled in the project settings
if settings.DEBUG:
    # If DEBUG mode is enabled, import the debug_toolbar module
    import debug_toolbar # type: ignore
    
    # Add the debug toolbar URLs to the project's URL patterns
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]


# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
