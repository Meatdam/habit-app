from rest_framework.pagination import PageNumberPagination


class Paginator(PageNumberPagination):
    """
    Пагинация для списков
    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100
