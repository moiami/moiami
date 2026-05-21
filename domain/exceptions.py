class DomainException(Exception):
    """Общее исключение для бизнес-логики"""

    pass


class SubscriptionNotFound(DomainException):
    pass


class SubscriptionExpired(DomainException):
    pass


class PermissionDenied(DomainException):
    pass


class NotFoundMoviesBySubscriptionId(DomainException):
    pass


class NotFoundGenresByMovieId(DomainException):
    pass


class NotFoundMovie(DomainException):
    pass


class NotFoundVideo(DomainException):
    pass


class NotFoundImage(DomainException):
    pass


class NotFoundGenre(DomainException):
    pass
