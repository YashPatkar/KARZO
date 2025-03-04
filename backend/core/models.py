# from django.db import models
# from driver.models import Driver  # Import the Driver model from the driver app
# import uuid
# # Create your models here.
# class Event(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=100)
#     date = models.DateField()
#     time = models.TimeField()
#     location = models.CharField(max_length=100)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     drivers = models.ManyToManyField(Driver, related_name='events', blank=True)  # Many-to-many relationship with Driver
#     def __str__(self):
#         return f'{self.name} - {self.date}'