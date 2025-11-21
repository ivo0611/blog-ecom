from django import forms
from django.core.exceptions import ValidationError
import datetime


class BatTuForm(forms.Form):
    GENDER_CHOICES = [
        ('nam', 'Nam'),
        ('nu', 'Nữ'),
    ]

    hoten = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Họ và tên'
        }),
        label='Họ và tên'
    )

    ngay = forms.IntegerField(
        min_value=1,
        max_value=31,
        required=True,
        widget=forms.Select(choices=[(i, f"{i:02d}") for i in range(1, 32)]),
        label='Ngày'
    )

    thang = forms.IntegerField(
        min_value=1,
        max_value=12,
        required=True,
        widget=forms.Select(choices=[(i, f"{i:02d}") for i in range(1, 13)]),
        label='Tháng'
    )

    nam = forms.IntegerField(
        min_value=1900,
        max_value=2050,
        required=True,
        widget=forms.Select(choices=[(i, i) for i in range(1900, 2051)]),
        label='Năm'
    )

    gio = forms.IntegerField(
        min_value=0,
        max_value=23,
        required=True,
        widget=forms.Select(choices=[(i, f"{i:02d}") for i in range(24)]),
        label='Giờ'
    )

    phut = forms.IntegerField(
        min_value=0,
        max_value=59,
        required=False,
        initial=0,
        widget=forms.Select(choices=[(i, f"{i:02d}") for i in range(60)]),
        label='Phút'
    )

    gioitinh = forms.ChoiceField(
        choices=GENDER_CHOICES,
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        label='Giới tính',
        initial='nam'
    )

    def clean(self):
        cleaned_data = super().clean()
        ngay = cleaned_data.get('ngay')
        thang = cleaned_data.get('thang')
        nam = cleaned_data.get('nam')

        if ngay and thang and nam:
            try:
                # Kiểm tra ngày hợp lệ
                datetime.date(nam, thang, ngay)
            except ValueError:
                raise ValidationError("Ngày sinh không hợp lệ!")

        return cleaned_data

    def clean_hoten(self):
        hoten = self.cleaned_data.get('hoten')
        if hoten:
            # Loại bỏ các ký tự không mong muốn
            import re
            hoten = re.sub(r'[<>"\']', '', hoten).strip()
            if len(hoten) < 2:
                raise ValidationError("Họ tên phải có ít nhất 2 ký tự!")
        return hoten