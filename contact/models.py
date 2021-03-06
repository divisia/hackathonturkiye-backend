from django.db import models


class ContactFormCategory(models.Model):
    name = models.CharField(max_length=32)
    url = models.URLField(null=True)
    def __str__(self): return str(self.name)

class ContactForm(models.Model):
    # server filled fields
    created_at = models.DateTimeField(auto_now_add=True)
    remote_addr = models.GenericIPAddressField(null=True)
    user_agent = models.CharField(max_length=256, null=True)
    path = models.CharField(max_length=256, null=True)

    # request filled fields
    title = models.CharField(max_length=256, null=True, blank=True)
    category = models.ForeignKey(ContactFormCategory, null=True, on_delete=models.SET_NULL, blank=True)
    body = models.TextField(max_length=2048)
    email = models.EmailField()
    contact = models.CharField(max_length=64)
    phone = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return f'[{self.category.name}] {self.contact} ({self.email})'
