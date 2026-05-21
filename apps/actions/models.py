import uuid
from time import time

from django.db.models import (
    CASCADE,
    BigIntegerField,
    ForeignKey,
    Model,
    UUIDField,
)

from apps.catalog.models import Movie


def current_timestamp() -> int:
    return int(time())


class MovieGetAction(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    happened_at = BigIntegerField(default=current_timestamp, db_index=True)
    user_id = UUIDField(null=True, blank=True, db_index=True)
    movie = ForeignKey(
        Movie,
        on_delete=CASCADE,
        related_name="get_actions",
    )
