from django_filters import rest_framework as filters


class ReviewFilters(filters.FilterSet):
    """
    FilterSet enabling API filtering for reviews based on the business user
    being reviewed and the user who wrote the review. This allows clients
    to efficiently retrieve reviews linked to specific users.
    """

    business_user_id = filters.NumberFilter(field_name="business_user_id")
    reviewer_id = filters.NumberFilter(field_name="reviewer_id")
