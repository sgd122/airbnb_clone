from django.db import models
from core import models as core_models

# Create your models here.
class Reservation(core_models.TimeStampedModel):

    """ Reservation Model Definition """

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STAUS_CHOICES = (
        (STATUS_PENDING, "대기"),
        (STATUS_CONFIRMED, "확인"),
        (STATUS_CANCELED, "취소"),
    )

    status = models.CharField(
        max_length=12, choices=STAUS_CHOICES, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"
