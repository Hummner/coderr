from rest_framework import pagination
from rest_framework.pagination import Response


class CustomPagination(pagination.PageNumberPagination):
    """
    Custom paginator that returns a simple paginated API response structure,
    including navigation links, total item count, and the current page results.
    """

    def get_paginated_response(self, data):
        """
        Build and return the paginated response format containing next/previous
        page links, total count, and serialized results.
        """
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })
    

class OfferPageNumberPagination(pagination.PageNumberPagination):
    """
    Pagination class specifically configured for offer listings, allowing
    page-size customization via query parameters and supporting large datasets.
    """

    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000

    def get_paginated_response(self, data):
        """
        Return the paginated response for offer queries, including pagination
        navigation links, total count, and the current page's results.
        """
        print(self)
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })
