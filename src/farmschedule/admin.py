from django.contrib import admin

from .models import (
	CountryDB,
	CountryFarmer,
	CountryFarm,
	SowingSchedule,
)


admin.site.register(CountryDB)
admin.site.register(CountryFarmer)
admin.site.register(CountryFarm)
admin.site.register(SowingSchedule)