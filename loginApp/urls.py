from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('blog.urls')),  # Redirige la raíz a la app "blog"
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),  # Añadido
]