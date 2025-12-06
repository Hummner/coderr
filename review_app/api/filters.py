from django_filters import rest_framework as filters

class ReviewFilters(filters.FilterSet):
    business_user_id = filters.NumberFilter(field_name="business_user_id")
    reviewer_id = filters.NumberFilter(field_name="reviewer_id")