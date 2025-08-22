from rest_framework.pagination import PageNumberPagination


class MoviePagination(PageNumberPagination):
    page_size = 2
    max_page_size = 100
    page_query_param = 'sahifa'
    page_size_query_param = 'miqdor'


class ReviewPagination(PageNumberPagination):
    page_size = 4
    max_page_size = 100
    page_query_param = 'sahifa'
    page_size_query_param = 'miqdor'