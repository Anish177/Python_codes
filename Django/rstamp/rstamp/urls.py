"""
URL configuration for rstamp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from store import views
from django.conf import settings
from django.conf.urls.static import static
from allauth.socialaccount import providers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('', include('allauth.urls')),
    # path('login/google_login/', views.google_login, name='google_login'),
    path('accounts/profile/', views.profile, name='profile'),
    path('logout', views.logout_view, name='logout'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('orders/', views.orders, name='orders'),
    path('contact/', views.contact, name='contact')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
