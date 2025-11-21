from django.urls import path
from . import views
from blog.views import home_view
from .views import vat_pham_view, bat_tu_view
from django.conf.urls import handler404
from .views import custom_404
urlpatterns = [
    path('', home_view, name='home'),
path('laso/', bat_tu_view, name='home'),
    path('ajax/create-image-tu-tru/', views.create_image_tu_tru, name='create_image_tu_tru'),
    path('ajax/bat-tu-calculation/', views.ajax_bat_tu_calculation, name='ajax_bat_tu_calculation'),

]
