from django.db import models

from wagtail.models import Page


class HomePage(Page):
    pass
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import datetime


class BatTuCalculation(models.Model):
    GENDER_CHOICES = [
        (0, 'Nữ'),
        (1, 'Nam'),
    ]

    ho_ten = models.CharField(max_length=100, verbose_name="Họ và tên")
    ngay_sinh = models.IntegerField(verbose_name="Ngày sinh")
    thang_sinh = models.IntegerField(verbose_name="Tháng sinh")
    nam_sinh = models.IntegerField(verbose_name="Năm sinh")
    gio_sinh = models.IntegerField(verbose_name="Giờ sinh")
    phut_sinh = models.IntegerField(verbose_name="Phút sinh")
    gioi_tinh = models.IntegerField(choices=GENDER_CHOICES, verbose_name="Giới tính")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Lá số tứ trụ"
        verbose_name_plural = "Lá số tứ trụ"

    def __str__(self):
        return f"{self.ho_ten} - {self.ngay_sinh}/{self.thang_sinh}/{self.nam_sinh}"


class ThienCan(models.Model):
    name = models.CharField(max_length=10)
    slug = models.CharField(max_length=20)
    ngu_hanh = models.CharField(max_length=10)
    sex = models.IntegerField()

    def __str__(self):
        return self.name


class DiaChi(models.Model):
    name = models.CharField(max_length=10)
    slug = models.CharField(max_length=20)
    ngu_hanh = models.CharField(max_length=10)
    sex = models.IntegerField()

    def __str__(self):
        return self.name


class NguHanh(models.Model):
    name = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name