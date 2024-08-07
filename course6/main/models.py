from django.db import models


class Client(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"


class Message(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"


class MailingManager(models.Manager):
    def active(self):
        return self.filter(status="started")


class Mailing(models.Model):
    STATUS_CHOICES = [
        ("created", "Created"),
        ("started", "Started"),
        ("completed", "Completed"),
    ]

    first_send_time = models.DateTimeField()
    periodicity = models.CharField(
        max_length=50,
        choices=[
            ("daily", "Daily"),
            ("weekly", "Weekly"),
            ("monthly", "Monthly"),
        ],
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="created")
    message = models.OneToOneField("Message", on_delete=models.CASCADE)
    clients = models.ManyToManyField("Client")

    def __str__(self):
        return f"Mailing {self.id} - {self.status}"

    class Meta:
        verbose_name = "Mailing"
        verbose_name_plural = "Mailings"


class Attempt(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    attempt_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ("success", "Success"),
            ("failure", "Failure"),
        ],
    )
    response = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Attempt {self.id} - {self.status}"

    class Meta:
        verbose_name = "Attempt"
        verbose_name_plural = "Attempts"
