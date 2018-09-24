'''
Views.py contains the logic for the website. Each function is for 
a page in the website. 
'''

from .forms import LocationsForm
from django.shortcuts import render
from mq.utils.mapquest_module import *
from mq.utils.classes_module import *
from django.contrib import messages

form = LocationsForm()

'''Sends the form to the html page to be displayed'''
def get_locations(request):
    return render(request, 'mq/enter_locations.html', {'form': form})

'''Uses the information from the form to build a url and retrieve the JSON
data from it. Crawls through JSON data to retrieve directions, total
distance, total time, and the latitudes and longitudes of the start and
end locations. Sends this information to an html page to be displayed.'''
def display_directions(request):
	if request.method == 'POST':
		form = LocationsForm(request.POST)
		if form.is_valid():
			start = form.cleaned_data['start_location']
			end = form.cleaned_data['end_location']

			try:
				json_result = [get_result(build_url(start, end))]

				steps = Steps().generate(json_result)
				totaldistance = TotalDistance().generate(json_result)
				totaltime = TotalTime().generate(json_result)
				latlong = LatLong().generate(json_result)

				if totaldistance == 0 and totaltime == 0:
					if latlong[0] == '39.78 N 100.45 W':
						#error message saying to input valid inputs
						messages.error(request, 'Please enter valid addresses/locations.', "danger")
						return render(request, 'mq/enter_locations.html', {'form': form})
					else:
						#error message saying location and destination are same
						messages.error(request, 'The start and end locations are the same, please enter two different locations.', "danger")
						return render(request, 'mq/enter_locations.html/', {'form': form})

				s = [word.capitalize() for word in start.split()]
				e = [word.capitalize() for word in end.split()]

				return render(request, 'mq/display_directions.html', {'steps': steps, 'totaldistance': totaldistance, 'totaltime': totaltime, 
					'startlatlong': latlong[1], 'endlatlong': latlong[0], 'start': ' '.join(s), 'end': ' '.join(e)})
			except:
				#error message saying to enter valid inputs that are driveable from each other
				messages.error(request, 'Please enter valid addresses/locations that are driveable from one another.', "danger")
				return render(request, 'mq/enter_locations.html', {'form': form})

	else:
		messages.error(request, "Error with request, try again.", "danger")
		return render(request, 'mq/enter_locations.html', {'form': form})


	