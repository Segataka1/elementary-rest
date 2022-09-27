from rest_framework.routers import DefaultRouter as DR
from mainapp.views import *

router = DR()
router.register('shops', ShopViewSet, basename='shops')
router.register('tickets', TicketViewSet, basename='tickets')

urlpatterns = []

urlpatterns += router.urls

