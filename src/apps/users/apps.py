from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'apps.users'

    def ready(self) -> None:
        from apps.users import signals  # noqa: F401
