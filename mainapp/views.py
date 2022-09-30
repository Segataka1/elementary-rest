from re import S
from rest_framework.viewsets import ModelViewSet 
from django_filters.rest_framework import DjangoFilterBackend
from mainapp.serializers import(
    Shop, ShopSerializer,
    Ticket, TicketSerializer,
)
from rest_framework import filters
from mainapp.paginations import StandardResultsSetPagination


class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['address']
    ordering_fields = ['time_start','time_end']
    search_fields = ['name',]
    pagination_class = StandardResultsSetPagination

class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields = ['shop',]
    # ordering_fields = ['replace_from','replace_to',]
    search_fields = ['shop__name','price',]