from django.db import models

# Create your models here.
class student(models.Model):
	first_name=models.CharField(max_length=20)
	middle_name=models.CharField(max_length=20)
	last_name=models.CharField(max_length=20)
	student_img=models.CharField(max_length=1000)
	registration_date = models.DateField()
	gender=models.BooleanField()	
	def __str__(self):
		return "name: "+ self.first_name + " " + self.middle_name + " " + self.last_name
 
