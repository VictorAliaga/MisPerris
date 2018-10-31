from django.urls import path
from . import views
# importamos settings y static para las imagenes de los perritos
from django.conf import settings
from django.conf.urls.static import static
# importamos vistas predeterminadas en django
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

# REEMPLAZE post_list por index ... !!!
urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.register_view, name='vista_registro'),
    path('login/', views.login_view, name='vista_login'),
    path('logout/', views.logout_view, name='vista_logout'),
    path('mascotas/', views.mascotas_view, name='vista_mascotas'),
    path('perrito/<int:pk>/', views.perrito_detalle_view, name='vista_perrito_detalle'),
    path('accounts/login/', views.login_view, name ='vista_login'),
    path('adopcion/completado/', views.adopcion_completa_view, name='vista_adopcion_completa'),

    #Urls Recuperacion de Contraseña
    path('reset/password/', PasswordResetView.as_view(), name='reset_password'),
    path('reset/password/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/password/confirm/P<uidb64>P<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    # url para las imagenes que suben de los perritos
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)