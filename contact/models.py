from django.db import models


class ContactFormCategory(models.Model):
    name = models.CharField(max_length=32)
    url = models.URLField()


class ContactForm(models.Model):
    # server filled fields
    created_at = models.DateTimeField(auto_now_add=True)
    remote_addr = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=256)
    path = models.CharField(max_length=256)

    # request filled fields
    title = models.CharField(max_length=256)
    category = models.ForeignKey(ContactFormCategory, null=True, on_delete=models.SET_NULL)
    body = models.TextField(max_length=2048)
    email = models.EmailField()
    contact = models.CharField(max_length=64)
    phone = models.CharField(max_length=32, null=True)

