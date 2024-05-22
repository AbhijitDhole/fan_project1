from django.shortcuts import render
from django.http import JsonResponse
from .models import FanSpecification, FanEvent
from .forms import FanControlForm, ConsumptionQueryForm
from django.utils import timezone
from datetime import datetime

def fan_control(request):
    if request.method == 'POST':
        form = FanControlForm(request.POST)
        if form.is_valid():
            status = form.cleaned_data['status'] == '1'
            speed_level = form.cleaned_data['speed_level']
            FanEvent.objects.create(status=status, speed_level=FanSpecification.objects.get(speed_level=speed_level))
            return JsonResponse({'message': 'Event recorded'})
    else:
        form = FanControlForm()
    return render(request, 'fan_control.html', {'form': form})

def consumption_query(request):
    if request.method == 'POST':
        form = ConsumptionQueryForm(request.POST)
        if form.is_valid():
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            print(f"Start Time: {start_time}")
            print(f"End Time: {end_time}")
            events = FanEvent.objects.filter(event_time__range=(start_time, end_time))
            print("Events:", events)

            power_factor = 0.8
            voltage = 220
            total_power = 0
            total_energy = 0
            last_time = None

            for event in events:
                print("TEST")
                if last_time is not None:
                    time_diff = (event.event_time - last_time).total_seconds() / 3600
                    last_event = FanEvent.objects.filter(event_time=last_time).first()
                    if last_event.status:
                        current = last_event.speed_level.current
                        print(f'Current: {current}')
                        power = current * voltage * power_factor
                        total_power += power
                        print(total_power)
                        total_energy += power * time_diff
                        print(total_energy)

                last_time = event.event_time
            print(f"Total Power: {total_power}")
            print(f"Total Energy: {total_energy}")
            return JsonResponse({
                'total_power': total_power,
                'total_energy': total_energy
            })

    else:
        form = ConsumptionQueryForm()
    return render(request, 'consumption_query.html', {'form': form})

