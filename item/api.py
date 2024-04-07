from rest_framework                 import viewsets,permissions
from django_filters.rest_framework  import DjangoFilterBackend
from .models                        import Item,Categoria,Review,Order
from rest_framework.filters         import SearchFilter
from .serializers                   import ItemSerializer,CategoriaSerializer,ReviewSerializer,OrderSerializer
import django_filters
from rest_framework                 import status
from rest_framework.views           import APIView
from rest_framework.response        import Response

class ItemFilter(django_filters.FilterSet):
    category            = django_filters.CharFilter(field_name="category__name", lookup_expr='icontains')
    name                = django_filters.CharFilter(lookup_expr='icontains')
    description         = django_filters.CharFilter(lookup_expr='icontains')
    date                = django_filters.DateFilter(field_name="created_at")
    date_range          = django_filters.DateFromToRangeFilter(field_name="created_at")
    min_price           = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price           = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    class Meta:
        model = Item
        fields = ["stock","sellerID"]
class ItemViewSet(viewsets.ModelViewSet):
    '''View Set'''
    queryset            = Item.objects.all()
    serializer_class    = ItemSerializer
    permission_classes  = [permissions.AllowAny]
    filter_backends     = (SearchFilter,DjangoFilterBackend)
    filterset_class     = ItemFilter
    search_fields       = ('category', 'name',"sellerID")

class CategoryViewSet(viewsets.ModelViewSet):
    '''View Set'''
    queryset            = Categoria.objects.all()
    serializer_class    = CategoriaSerializer
    permission_classes  = [permissions.AllowAny]
    filter_backends     = (SearchFilter,DjangoFilterBackend)
    filterset_fields    = ["name"]
    search_fields       = ["name"]
class ReviewViewSet(viewsets.ModelViewSet):
    '''View Set'''
    queryset            = Review.objects.all()
    serializer_class    = ReviewSerializer
    permission_classes  = [permissions.AllowAny]
    filter_backends     = (SearchFilter,DjangoFilterBackend)
    filterset_fields    = ["item"]
    search_fields       = ["item"]
class OrderViewSet(viewsets.ModelViewSet):
    '''View Set'''
    queryset            = Order.objects.all()
    serializer_class    = OrderSerializer
    permission_classes  = [permissions.AllowAny]
    filter_backends     = (SearchFilter,DjangoFilterBackend)
    filterset_fields    = ["userID"]
    search_fields       = ["userID"]