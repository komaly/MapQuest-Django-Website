from .forms import LocationsForm
from django.shortcuts import render

# Create your views here.
def get_locations(request):
    form = LocationsForm()
    return render(request, 'mq/enter_locations.html', {'form': form})