from django.db import models


class Device(models.Model):
    DEVICE_TYPE_CHOICES = [
        ('Router', 'Router'),
        ('Switch', 'Switch'),
        ('Firewall', 'Firewall'),
        ('Server', 'Server'),
    ]

    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField(protocol='both', unpack_ipv4=True)
    device_type = models.CharField(max_length=50, choices=DEVICE_TYPE_CHOICES)
    status = models.BooleanField(default=True)  # True = active, False = inactive
    location = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.ip_address})"
