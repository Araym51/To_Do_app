from rest_framework.pagination import LimitOffsetPagination


class UsersLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    