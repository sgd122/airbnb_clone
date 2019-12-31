from django.db import models
from core import models as core_models
from users import models as user_models

# Create your models here.
class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    review = models.TextField()
    accuracy = models.IntegerField(help_text="정확성")
    communication = models.IntegerField(help_text="통신")
    cleanliness = models.IntegerField(help_text="청결")
    location = models.IntegerField(help_text="위치")
    check_in = models.IntegerField(help_text="체크인")
    value = models.IntegerField()
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room}"

    def rating_average(self):
        avg = (
            self.accuracy
            + self.communication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 2)

    rating_average.short_description = "avg"
