from django.shortcuts import render,get_object_or_404
import datetime
# Create your views here.

from .models import (
	CountryDB,
	CountryFarmer,
	CountryFarm,
	SowingSchedule
)

def home_view(request):

	get_today 			= datetime.date.today()
	get_tomorrow 		= get_today + datetime.timedelta(days=1)

	get_farmers 		= CountryFarmer.objects.all()
	get_all_schedule 	= SowingSchedule.objects.all()

	list_sch 	= None
	list_crop 	= {}

	# To get all the farms schedules for sowing today and tomorrow.
	if get_all_schedule:
		list_sch = [sch for sch in get_all_schedule if sch.sowing_date == get_today or sch.sowing_date == get_tomorrow]

	
	# To get farmers who are growing a crop 
	if get_farmers:
		for farmer in get_farmers:
			if farmer.countryfarm_set.all():
				for c in farmer.countryfarm_set.all():
					list_crop[farmer.name] = c.crop

	template_name = 'home.html'

	context = {
		"schedules": list_sch,
		"crop": list_crop,
	}

	return render(request,template_name,context)



def farmer_detail(request,id):
	get_farmer = CountryFarmer.objects.get(id=id)

	cost = 0

	# To get total cost of fertilizer for the farmer.
	for f in get_farmer.countryfarm_set.all():
		for g in f.sowingschedule_set.all():
			cost += g.quantity * float(g.fert_unit)

	template_name = 'farmer_detail.html'

	context = {
		"total_cost":cost,
	}

	return render(request,template_name,context)













