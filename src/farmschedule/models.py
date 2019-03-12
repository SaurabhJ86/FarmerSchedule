import re

from django.core.validators import RegexValidator 
from django.db import models

# Create your models here.
fert_choice = [
	('solid','SOLID'),
	('liquid',"LIQUID")
]

unit_choice = [
	('1000','ton'),
	('1','kg'),
	('.001','gram'),
	('1000',"l"),
	('.001','ml'),
]

class CountryDB(models.Model):

	country 	= models.CharField(max_length=120,unique=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "CountryDB"
		verbose_name_plural = "CountryDB"

	def __str__(self):
		return self.country



class CountryFarmer(models.Model):

	country 	= models.ForeignKey(CountryDB,on_delete=models.CASCADE)
	name 		= models.CharField(max_length=120)
	language 	= models.CharField(max_length=120)
	phone_regex = RegexValidator(regex=re.compile("(0/91)?[7-9][0-9]{9}"))
	phone 		= models.CharField(validators=[phone_regex],max_length=120,unique=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.name



class CountryFarm(models.Model):

	farmer 		= models.ForeignKey(CountryFarmer,on_delete=models.CASCADE)
	area 		= models.CharField(max_length=120)
	village 	= models.CharField(max_length=120)
	crop		= models.CharField(max_length=50)
	sowing_date = models.DateField()

	class Meta:
		verbose_name = "Farm"

	def __str__(self):
		return self.farmer.name + " Farm"



class SowingSchedule(models.Model):

	farm 		= models.ForeignKey(CountryFarm,on_delete=models.CASCADE)
	# This can't be equal to CountryFarmSowing Date.
	sowing_date = models.DateField()
	fert_type 	= models.CharField(max_length=10,choices=fert_choice,default="solid")
	quantity	= models.IntegerField()
	fert_unit 	= models.CharField(max_length=5,choices=unit_choice,default="1")


	def __str__(self):
		return self.farm.farmer.name + " Farm Schedule"




