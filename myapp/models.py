from django.db import models



class Vehicle(models.Model):

    CATEGORY_CHOICES =[('Car', 'Car'),
                       
                        ('Bike', 'Bike')]
    

    CAR_TYPE_CHOICES = [('SUV', 'SUV'),
                         
                         ('Sedan', 'Sedan'),

                         ('Hatchback', 'Hatchback')]
    

    

    BIKE_TYPE_CHOICES = [('Cruiser', 'Cruiser'),
                         
                         ('Sports', 'Sports'),

                         ('Commuter', 'Commuter')]
    

    
    OWNERSHIP_CHOICES=[('First','First'),
                       
                       ('Second','Second'),
                        
                       ( 'Third','Third')]
    
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    preview_image=models.ImageField(upload_to="previewimages",null=True,blank=True)

    brand = models.CharField(max_length=100)

    model = models.CharField(max_length=100)

    price = models.PositiveIntegerField()

    km_drive = models.IntegerField()

    ownership = models.CharField(max_length=100, choices=OWNERSHIP_CHOICES,blank=True,null=True)
    
    car_type = models.CharField(max_length=100, choices=CAR_TYPE_CHOICES, blank=True, null=True)

    bike_type = models.CharField(max_length=100, choices=BIKE_TYPE_CHOICES, blank=True, null=True)

    





    



