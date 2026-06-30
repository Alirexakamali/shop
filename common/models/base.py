from common.models.timestamp import TimeStampedModel
from common.models.uuid import UUIDModel


class BaseModel(UUIDModel, TimeStampedModel):
    """
    Base model for all project models.
    """

    class Meta:
        abstract = True