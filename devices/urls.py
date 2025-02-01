from django.urls import path
from .views import device_list, device_create, device_status_check, export_devices_csv, device_delete

urlpatterns = [
    path('', device_list, name='device_list'),
    path('create/', device_create, name='device_create'),
    path('status/<int:device_id>/', device_status_check, name='device_status'),
    path('export/csv/', export_devices_csv, name='export_devices_csv'),
    path('delete/<int:device_id>/', device_delete, name='device_delete'),  # 削除用のパス
]
