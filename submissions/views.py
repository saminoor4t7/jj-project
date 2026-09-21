from django.conf import settings
from django.core.mail import send_mail

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Submission
from .serializer import *


class SubmissionViewSet(viewsets.ModelViewSet):

    queryset = Submission.objects.all().order_by("-created_at")
    serializer_class = SubmissionSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        submission = serializer.save()

        subject = f"New Service Inquiry - {submission.get_service_display()}"

        message = f"""
New service inquiry received.

Name: {submission.name}
Email: {submission.email}
Phone: {submission.phone}
Service: {submission.get_service_display()}

Message:
{submission.message}

Submitted at:
{submission.created_at}
"""

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=(settings.COMPANY_EMAIL,),
            fail_silently=False,
        )

        return Response(
            {
                "message": "Submission received successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )