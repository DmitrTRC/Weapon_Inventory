from django.db import models


# Create your models here.
class WeaponItem(models.Model):
    item_model = models.ForeignKey('ItemModel', on_delete=models.CASCADE)
    item_photo = models.ImageField(upload_to='weapon_item_photos', blank=True)
    item_license = models.ForeignKey('License', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    caliber = models.FloatField(default=0)
    barrel_number = models.IntegerField(default=0)
    barrel_shots = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    is_cleared = models.BooleanField(default=False)
    is_need_repair = models.BooleanField(default=False)
    is_alligned = models.BooleanField(default=False)
    optics_one = models.ForeignKey('Optics', on_delete=models.CASCADE, related_name='optics_one', blank=True, null=True)
    optics_two = models.ForeignKey('Optics', on_delete=models.CASCADE, related_name='optics_two', blank=True, null=True)
    last_clean = models.DateField(blank=True, null=True)
    last_shoot = models.DateField(blank=True, null=True)
    notes = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.item_model.name


class Optics(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='optics_item_photos', blank=True)
    optics_type = models.CharField(max_length=100, blank=False, null=False, default='Day')

    def __str__(self):
        return self.name


class ItemModel(models.Model):
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class License(models.Model):
    license_number = models.CharField(max_length=200)
    expiration_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='license_photos', blank=True)
    is_active = models.BooleanField(default=True)
    weapon_item = models.ForeignKey('WeaponItem', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.license_number
