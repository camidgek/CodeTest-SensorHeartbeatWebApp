import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.generic.list import ListView

from .models import (Sensor, Heartbeat)
from .serializers import (SensorSerializer, HeartbeatSerializer)


PAGE_LIMIT = 25

def index(request):
    return redirect('/dashboard')

def dashboard(request):
    context = {}
    context['sensor_list'] = \
        Sensor.objects.all().order_by('-id')[:PAGE_LIMIT]
    context['heartbeat_list'] = \
        Heartbeat.objects.all().order_by('-id')[:PAGE_LIMIT]
    return render(request, 'sensorheartbeat/dashboard.html', context)

class PaginateMixin():
    paginate_by = PAGE_LIMIT

class SensorListView(PaginateMixin, ListView):
    model = Sensor

    def post(self, request, *args, **kwargs):
        return create_sensor(request)

def create_sensor(request):
    if request.method == 'POST':
        # Get and validate POST data
        json_data = json.loads(request.body)
        serializer = SensorSerializer(data=json_data)
        # Serialize data and create sensor if data is valid
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        # There was an error serializing the data
        return JsonResponse(serializer.errors, status=401)
    # Can only call this function as a POST request
    return HttpResponse(status=400)

class HeartbeatListView(PaginateMixin, ListView):
    model = Heartbeat

    def post(self, request, *args, **kwargs):
        return create_heartbeat(request)

def create_heartbeat(request):
    if request.method == 'POST':
        # Get and validate POST data
        data = json.loads(request.body)
        # Allow API to accept Sensor.serial_num instead of Sensor.id
        serial_num = data.get('serial_num')
        if serial_num and not data.get('sensor'):
            try:
                data['sensor'] = Sensor.objects.get(serial_num=serial_num).id
            except Sensor.DoesNotExist:
                error_data = {
                        'error': f"Sensor with serial_num '{serial_num}'" \
                            " does not exist"
                }
                return JsonResponse(error_data,status=401)
        # Serialize data and create heartbeat if data is valid
        serializer = HeartbeatSerializer(data=data.copy())
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        # There was an error serializing the data
        return JsonResponse(serializer.errors, status=401)
    # Can only call this function as a POST request
    return HttpResponse(status=400)
