from django.views.generic import TemplateView

from django.shortcuts import render
from sensores.models import SensorData

class IndexView(TemplateView):
    template_name = "index.html"

class Quem_SomosView(TemplateView):
    template_name = "quem_somos.html"

class ContatosView(TemplateView):
    template_name = "contatos.html"

def grafico(request):
    sensor_data = SensorData.objects.all().order_by('timestamp')
    temperatures = [data.temperature for data in sensor_data]
    humidities = [data.humidity for data in sensor_data]
    timestamps = [data.timestamp.strftime("%Y-%m-%d %H:%M:%S") for data in sensor_data]

    context = {
        'temperatures': temperatures,
        'humidities': humidities,
        'timestamps': timestamps,
    }
    return render(request, 'grafico.html', context)

