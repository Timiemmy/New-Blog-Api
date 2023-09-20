from rest_framework import pagination


class CustomPagination(pagination.PageNumberPagination):
    page_size = 1 # maximum result to show per page
    page_size_query_param = 'page_size' # Client can use this to override and show mmore
    max_page_size = 50 # Maximum page size a client can override to
    page_query_param = 'p' # Changing the default page of drf to p