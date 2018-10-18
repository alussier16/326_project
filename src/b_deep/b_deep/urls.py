from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('closeknit/', include('closeknit.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/closeknit/')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
