class DomainException(Exception):
    """Общее исключение для бизнес-логики"""
    pass


class SubscriptionNotFound(DomainException):
    pass


class SubscriptionExpired(DomainException):
    pass


class PermissionDenied(DomainException):
    pass
