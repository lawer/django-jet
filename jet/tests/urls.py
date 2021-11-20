from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

from django.urls import path

urlpatterns = [
	path('jet/', include('jet.urls', 'jet')),
	path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
	path('admin/doc/', include('django.contrib.admindocs.urls')),
	path('admin/', admin.site.urls),
]
