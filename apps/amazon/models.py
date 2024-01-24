from django.db import models

# Create your models here.


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Order(TimeStampModel):
    order_id = models.CharField(max_length=50)
    item = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)


class Return(TimeStampModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    return_reason = models.TextField()
    return_tracking = models.CharField(max_length=50)


class Dispute(TimeStampModel):
    OPEN = "Open"
    PENDING = "Pending"
    CLOSE = "Close"

    STATUS_CHOICES = [
        (OPEN, "Open"),
        (PENDING, "Pending"),
        (CLOSE, "Close"),
    ]
    return_order = models.ForeignKey(Return, on_delete=models.CASCADE)
    reason = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=OPEN)
    resolution = models.TextField()
