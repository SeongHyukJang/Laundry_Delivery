from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('laundry', views.LaundryView)
router.register('repair', views.RepairView)
router.register('customer', views.CustomerView)


urlpatterns = [
    path('', include(router.urls))
]