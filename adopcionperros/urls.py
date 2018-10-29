from django.urls import path
from . import views
# importamos settings y static para las imagenes de los perritos
from django.conf import settings
from django.conf.urls.static import static

# REEMPLAZE post_list por index ... !!!
urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.register_view, name='vista_registro'),
    path('login/', views.login_view, name='vista_login'),
    path('logout/', views.logout_view, name='vista_logout'),
    path('mascotas/', views.mascotas_view, name='vista_mascotas'),
    path('perrito/<int:pk>/', views.perrito_detalle_view, name='vista_perrito_detalle'),
    # url para las imagenes que suben de los perritos
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)