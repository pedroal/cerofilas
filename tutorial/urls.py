"""tutorial URL Configuration

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
from django.urls import include, path
from rest_framework import routers

from tutorial.quickstart import views
from tutorial.quickstart.views import UsuarioSaveData

"""from tutorial.quickstart import view
from tutorial.quickstart.views import ListProductos"""

urlpatterns = [
    path('admin/', admin.site.urls),
"""" path('productos/', ListProductos.as_view()),"""
]

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


router.register(r'productos', views.ListProductos)

"""usuarios"""
router.register(r'usuarios', views.ListUsuarios)
"""router.register(r'create', UsuarioSaveData.as_view())"""

router.register(r'entidades', views.ListEntidades)
router.register(r'comercios', views.ListComercios)
router.register(r'pedidos', views.ListPedidos)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))


]