from django.db import models


class record(models.Model):
	task=models.CharField(max_length=100)
	created_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.task
