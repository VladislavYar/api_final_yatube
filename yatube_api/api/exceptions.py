from rest_framework.exceptions import APIException


class PermissionNotAuthorChangeDenied(APIException):
    """Исключение при несоответсвии автора с пользователем."""
    status_code = 403
    default_detail = 'Изменение(удаление) чужого контента запрещено.'
    default_code = 'not_author_update_destroy_prohibited'


class PermissionDenied(APIException):
    """Исключение при запросе неавторизованного пользователя."""
    status_code = 401
    default_detail = 'Требуется авторизация.'
    default_code = 'unauthorized_access_prohibited'


class PermissionAddChangeDenied(APIException):
    """Исключение при запросе добавления и изменения."""
    status_code = 405
    default_detail = 'В добавлении(изменении) отказано.'
    default_code = 'add_change_prohibited'
