from django.db import models


class Submission(models.Model):

    SERVICE_CHOICES = [
        ("medical_billing", "Medical Billing"),
        ("medical_coding", "Medical Coding"),
        ("medical_credentialing", "Medical Credentialing"),
        ("revenue_cycle_management", "Revenue Cycle Management"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_service_display()}"