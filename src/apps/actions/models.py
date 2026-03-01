from django.conf import settings
from django.db.models import (
    CASCADE,
    PROTECT,
    CharField,
    DateTimeField,
    ForeignKey,
    Model,
)


class ActionType(Model):
    name = CharField(max_length=255)

class Action(Model):
    happened_at = DateTimeField()
    user = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        related_name='actions',
    )
    type = ForeignKey(
        ActionType,
        on_delete=PROTECT,
        related_name='actions',
    )
