# FarmerSchedule
This project is used to create schedules for sowing for farmers and also calculate the total cost involved for individual farmer.

# Steps for local machine installation
1.git clone https://github.com/SaurabhJ86/FarmerSchedule

2.cd FarmerSchedule

3.virtualenv -p python3 .

4.source bin/activate

5.cd src

6.python manage.py migrate

7.python manage.py createsuperuser

8.python manage.py runserver
