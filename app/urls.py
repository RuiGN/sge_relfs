from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('brands.urls')),
    path('api/v1/', include('categories.urls')),
    path('api/v1/', include('inflows.urls')),
    path('api/v1/', include('outflows.urls')),
    path('api/v1/', include('products.urls')),
    path('api/v1/', include('suppliers.urls')),

    path('', views.home, name='home'),
    path('', include('suppliers.urls')),
    path('', include('brands.urls')),
    path('', include('categories.urls')),
    path('', include('products.urls')),
    path('', include('inflows.urls')),
    path('', include('outflows.urls')),
]
