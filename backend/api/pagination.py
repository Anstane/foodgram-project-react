from rest_framework import pagination


class CustomPagination(pagination.PageNumberPagination):
    """Кастомный класс пагинации на 6 записей."""

    page_size_query_param = 'limit'
