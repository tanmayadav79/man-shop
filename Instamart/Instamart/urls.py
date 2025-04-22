from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Insta_grocery import views  # your main app views

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ Home page of Instamart
    path('', views.home, name='home'),

    # ✅ Product actions
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),

    # ✅ Auth system
    path('accounts/', include('accounts.url')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
