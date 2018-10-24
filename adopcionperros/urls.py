from django.urls import path
from . import views
# importamos settings y static para las imagenes de los perritos
from django.conf import settings
from django.conf.urls.static import static

# REEMPLAZE post_list por index ... !!!
urlpatterns = [
    path('', views.index, name='index'),
    # url para las imagenes que suben de los perritos
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

