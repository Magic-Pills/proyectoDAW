"""servidorDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from AdminSite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', views.UsuariosList.as_view()),
    path('usuarios/<str:pk>/', views.UsuariosDetalle.as_view()),
    path('clientes/', views.ClientesList.as_view()),
    path('clientes/<str:pk>/', views.ClientesDetalle.as_view()),
    path('pagos/', views.PagoList.as_view()),
    path('pagos/<str:pk>/', views.PagoDetalle.as_view()),
    path('productos/', views.ProductosList.as_view()),
    path('productos/<str:pk>/', views.ProductosDetalle.as_view()),
    path('ventas/', views.VentaList.as_view()),
    path('ventas/<str:pk>/', views.VentaDetalle.as_view()),
    path('ventaProductos/', views.VentaProductoList.as_view()),
    path('ventaProductos/<str:pk>/', views.VentaProductoDetalle.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
