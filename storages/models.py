from django.db import models
from common.models import CommonModel


class Image(CommonModel):
    image = models.ImageField(upload_to="uploaded_images/")

    def __str__(self):
        return f"Image_{self.id}"


class Excel(CommonModel):
    excel = models.FileField(upload_to="uploaded_excels/")
    a1 = models.CharField(max_length=30, null=True, blank=True)
    b1 = models.CharField(max_length=30, null=True, blank=True)
    c1 = models.CharField(max_length=30, null=True, blank=True)
    d1 = models.CharField(max_length=30, null=True, blank=True)
    e1 = models.CharField(max_length=30, null=True, blank=True)
    a2 = models.CharField(max_length=30, null=True, blank=True)
    b2 = models.CharField(max_length=30, null=True, blank=True)
    c2 = models.CharField(max_length=30, null=True, blank=True)
    d2 = models.CharField(max_length=30, null=True, blank=True)
    e2 = models.CharField(max_length=30, null=True, blank=True)
    a3 = models.CharField(max_length=30, null=True, blank=True)
    b3 = models.CharField(max_length=30, null=True, blank=True)
    c3 = models.CharField(max_length=30, null=True, blank=True)
    d3 = models.CharField(max_length=30, null=True, blank=True)
    e3 = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f"Excel_{self.excel}"
