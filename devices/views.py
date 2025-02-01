from django.shortcuts import render, get_object_or_404, redirect
from .models import Device
from .forms import DeviceForm
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib import messages
import subprocess
import csv
from django.contrib.auth.decorators import login_required

@login_required
def device_list(request):
    devices = Device.objects.all()
    return render(request, 'devices/device_list.html', {'devices': devices})


@login_required
def device_create(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('device_list')
    else:
        form = DeviceForm()
    return render(request, 'devices/device_form.html', {'form': form})


def device_status_check(request, device_id):
    device = Device.objects.get(id=device_id)
    ip = device.ip_address
    response = subprocess.run(['ping', '-n', '1', ip], stdout=subprocess.PIPE)

    if response.returncode == 0:
        status = 'Online'
    else:
        status = 'Offline'

    return JsonResponse({'status': status})


def device_delete(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    device.delete()
    messages.success(request, f'Device "{device.name}" was successfully deleted.')
    return redirect('device_list')


def export_devices_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="devices.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'IP Address', 'Device Type', 'Status', 'Location', 'Notes'])

    devices = Device.objects.all()
    for device in devices:
        writer.writerow([device.name, device.ip_address, device.device_type, 'Active' if device.status else 'Inactive', device.location, device.notes])

    return response