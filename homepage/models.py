from django.db import models


class Vechile(models.Model):
    name = models.CharField(max_length=200)
    gps_tracking_no = models.CharField(max_length=200)
    number_plate = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.name


class VechileDriver(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    joined_date = models.CharField(max_length=200)
    using_vehicle = models.ForeignKey(Vechile, related_name="vechile_driver", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()
    

class VechileMaitenance(models.Model):
    name = models.CharField(max_length=200)
    vechile = models.ForeignKey(Vechile, related_name="vechile_maitanance", on_delete=models.CASCADE)
    price = models.CharField(max_length=200)
    date = models.CharField(max_length=200)


    def __str__(self) -> str:
        return super().__str__()
    


