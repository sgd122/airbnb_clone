from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

# Create your models here.
class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """ RoomType Model Definition """

    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):

    """ Amenity Model Definition """

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """ Facility Model Definition """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """ HouseRule Model Definition """

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    name = models.CharField(max_length=140, help_text="이름")
    description = models.TextField()
    country = CountryField
    city = models.CharField(max_length=80, help_text="도시")
    price = models.IntegerField(help_text="가격")
    address = models.CharField(max_length=140, help_text="주소")
    guests = models.IntegerField(help_text="인원수")
    beds = models.IntegerField(help_text="침대")
    bedrooms = models.IntegerField(help_text="침실")
    baths = models.IntegerField(help_text="화장실")
    check_in = models.TimeField(help_text="체크인")
    check_out = models.TimeField(help_text="체크아웃")
    instant_book = models.BooleanField(default=False, help_text="바로예약")
    host = models.ForeignKey("users.User", on_delete=models.CASCADE, help_text="호스트")
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    amenties = models.ManyToManyField("Amenity", blank=True)
    facilities = models.ManyToManyField("Facility", blank=True)
    house_rules = models.ManyToManyField("HouseRule", blank=True)

    def __str__(self):
        return self.name
