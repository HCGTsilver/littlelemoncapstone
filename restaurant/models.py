from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField(default=6)
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField(default=5)

    def __str__(self):
        return self.title


class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, default=None, blank=True, null=True, on_delete=models.PROTECT)
    inventory = models.SmallIntegerField(null=True)

    def __str__(self):
        return self.title

    def get_item(self):
        return f'{self.title} : {str(self.price)}'
