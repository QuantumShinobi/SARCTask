from django.db import models

# Create your models here.


class Item(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Session(models.Model):
    session_id = models.UUIDField(primary_key=True, editable=False)
    key = models.BinaryField()


class Cart(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False)
    items = models.ManyToManyField(Item)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    session_id = models.ForeignKey(
        Session, on_delete=models.CASCADE)

    def __str__(self):
        return self.uuid
