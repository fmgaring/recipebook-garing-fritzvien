from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ledger/', include('ledger.urls', namespace='ledger'))
]
