from django.core import mail
from django.test import TestCase, override_settings
from rest_framework.test import APIClient

from .models import Submission


@override_settings(EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend")
class SubmissionEmailTests(TestCase):

	def test_submission_sends_email_to_company_address(self):
		response = APIClient().post(
			"/api/submissions/",
			{
				"name": "Jane Doe",
				"email": "jane@example.com",
				"phone": "555-0100",
				"service": "medical_billing",
				"message": "Please contact me.",
			},
			format="json",
		)

		self.assertEqual(response.status_code, 201)
		self.assertEqual(Submission.objects.count(), 1)
		self.assertEqual(len(mail.outbox), 1)
		self.assertEqual(mail.outbox[0].to, ["jrao09802@gmail.com"])
