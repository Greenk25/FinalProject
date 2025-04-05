from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import InventoryItem

@receiver(post_save, sender=InventoryItem)
def track_inventory_changes(sender, instance, created, **kwargs):
    print(f"Inventory Updated: {instance.name}, Quantity: {instance.quantity}")

