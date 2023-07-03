from django.db import models


class License(models.Model):
    license_number = models.CharField(max_length=200)
    expiration_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.license_number


class WeaponItem(models.Model):
    item_name = models.CharField(max_length=200)
    item_license = models.ForeignKey('License', on_delete=models.CASCADE)
    is_cleared = models.BooleanField(default=False)
    is_need_repair = models.BooleanField(default=False)
    is_zeroed = models.BooleanField(default=True)
