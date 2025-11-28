from django_filters import rest_framework as filters

class OfferFilters(filters.FilterSet):
    creator_id = filters.NumberFilter(field_name='creator_id')
    min_price = filters.NumberFilter(field_name="offer_detail__price", lookup_expr='gte')
    max_delivery_time = filters.NumberFilter(field_name="offer_detail__delivery_time_in_days", lookup_expr='lte')