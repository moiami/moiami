from rest_framework.exceptions import APIException

class InternalServer(APIException):
    status_code = 500
    default_detail = 'Ошибка сервера'
    default_code = 'Ошибка сервера'

class NotFoundMoviesBySubscriptionId(APIException):
    status_code = 404
    default_detail = 'Фильмы не найдены'
    default_code = 'Фильмы не найдены'

class NotFoundGenresByMovieId(APIException):
    status_code = 404
    default_detail = 'Жанры не найдены'
    default_code = 'Жанры не найдены'

class NotFoundMovie(APIException):
    status_code = 404
    default_detail = 'Фильм не найден'
    default_code = 'Фильм не найден'

class NotFoundVideo(APIException):
    status_code = 404
    default_detail = 'Видео не найдено'
    default_code = 'Видео не найдено'

class NotFoundImage(APIException):
    status_code = 404
    default_detail = 'Обложка не найдена'
    default_code = 'Обложка не найдена'

class NotFoundGenre(APIException):
    status_code = 404
    default_detail = 'Жанр не найден'
    default_code = 'Жанр не найден'


