from re import S
from rest_framework.viewsets import ModelViewSet 
from mainapp.serializers import(
    Shop, ShopSerializer,
    Ticket, TicketSerializer,
)


class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer