from rest_framework import serializers
from .models import Submission


class SubmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Submission
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "service",
            "message",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]