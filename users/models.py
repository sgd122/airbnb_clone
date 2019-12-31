from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True, help_text="프로필사진")
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, blank=True, help_text="성별"
    )
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True, help_text="생일")
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, blank=True, help_text="언어"
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, blank=True, help_text="통화"
    )
    superhost = models.BooleanField(default=False)
