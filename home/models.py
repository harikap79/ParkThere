from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser): #User kind of extends the django user model
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

class RecordedParkingLot(models.Model):
    carParkName = models.CharField(max_length = 200) # Might not need a foreignkey?
    carParkLot = models.CharField(max_length = 50)
    carParkLevel = models.CharField(max_length = 50)
    carParkZone = models.CharField(max_length = 50)
    dateTime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('User', on_delete = models.CASCADE)

    def __str__(self):
        return self.carParkName

class CarPark(models.Model):
    carParkName = models.CharField(max_length = 200)
    category = models.CharField(max_length = 200)
    weekDaysRate1 = models.CharField(max_length = 200)
    weekDaysRate2 = models.CharField(max_length = 200)
    satRate = models.CharField(max_length = 200)
    sunRate = models.CharField(max_length = 200)
    carParkType = models.CharField(max_length = 200)
    parkingSystem = models.CharField(max_length = 200)
    freeParking = models.CharField(max_length = 200)
    nightParking = models.CharField(max_length = 200)
    lat = models.FloatField()
    lng = models.FloatField()


    def __str__(self):
        return self.carParkName

class BookmarkedCarPark(models.Model):
    user = models.ForeignKey('User', on_delete = models.CASCADE)
    carPark = models.ForeignKey('CarPark', on_delete = models.CASCADE)
    def __str__(self):
        stringtoreturn = self.user.email
        stringtoreturn += ":"
        stringtoreturn += self.carPark.carParkName
        return stringtoreturn

class SearchHistory(models.Model):
    user = models.ForeignKey('User', on_delete = models.CASCADE)
    dateTime = models.DateTimeField(auto_now=True)#date object created, not updated
    carPark = models.ForeignKey('CarPark', on_delete = models.CASCADE)

    def __str__(self):
        stringtoreturn = self.user.email
        stringtoreturn += ":"
        stringtoreturn += self.carPark.carParkName
        return stringtoreturn


class CarParkPrice(models.Model):
    carPark = models.ForeignKey('CarPark', on_delete = models.CASCADE)
    firsthour = models.FloatField()
    subhalfhour = models.FloatField()
    subfifteen = models.FloatField(default = 0)
    subhour = models.FloatField(default = 0)
    perentry = models.FloatField()
    freeperiod = models.FloatField(default = 0)

    def __str__(self):
    	return self.carPark.carParkName


# Create your models here.
