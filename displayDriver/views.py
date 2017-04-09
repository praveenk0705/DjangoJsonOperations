from django.shortcuts import render
from datetime import datetime
import json
from django.template import loader
from django.views.generic import TemplateView
from django.http import HttpResponse
from dateutil import tz

def DisplayView(request):
    template = loader.get_template('index.html')
    with open('displayDriver\static\driverlog.json') as data_file:
        data = json.load(data_file)
        drivers= data['drivers']
    context = {
        'drivers' : drivers
    }
    return HttpResponse(template.render(context, request))

class AboutPageView(TemplateView):
	template_name = "about.html"

def Canvas(request):
    template= loader.get_template('canvas.html')
    with open('displayDriver\static\driverlog.json') as data_file:
        data = json.load(data_file)
    current_timelog_events = []
    for driver in data['drivers']:
       if driver['driver_license'] == request.GET['lic']:
            for timelog in driver['timelogs']:
                if timelog['timelog_id'] == request.GET['timelog_id']:
                    current_timelog_events = timelog['timelog_events']



    timelog_state_dict = {'OFF_DUTY': 7.0,'ON_DUTY': 1.0, 'SLEEPER_BERTH' : 5.0 , 'DRIVING': 3.0 }
    timelog_display_array = []
    for x in current_timelog_events:
        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz('US/Pacific')
        utc = datetime.strptime(x['event_start_time'], '%Y-%m-%dT%H:%M:%SZ')
        utc = utc.replace(tzinfo=from_zone)
        central = utc.astimezone(to_zone)
        hr = float(central.strftime("%H"))
        min = float(central.strftime("%M"))
        sec = float(central.strftime("%S"))
        x_timestamp = hr + (min/60) + (sec/3600)


        temp_display = {
            'x': x_timestamp,
            'y': timelog_state_dict[x['driver_status']]
        }
        timelog_display_array.append(temp_display)
    context = {
        'timelog_display_array' :timelog_display_array
    }

    return HttpResponse(template.render(context,request ))





