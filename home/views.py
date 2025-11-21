from django.shortcuts import render

def home(request):
    return render(request, "home/home_page.html")  # Đúng theo thư mục templates trong app
# from django.http import HttpResponse
#
# def home(request):
#     return HttpResponse("<h1>Trang chủ đang hoạt động</h1>")
def vat_pham_view(request):
    return render(request, "home/vat_pham_phong_thuy.html")  # Đúng theo thư mục templates trong app
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import BatTuCalculation
from .forms import BatTuForm
from .services import LasoTutruService
import json


def bat_tu_view(request):
    """View chính cho trang lá số tứ trụ"""
    form = BatTuForm()
    context = {
        'form': form,
        'render': False,
        'day_range': range(1, 32),
        'month_range': range(1, 13),
        'year_range': range(1900, 2051),
        'hour_range': range(0, 24),
        'minute_range': range(0, 60),
    }

    # Xử lý form submit
    if request.method == 'GET' and all(key in request.GET for key in ['ngay', 'thang', 'nam', 'gio']):
        form = BatTuForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data

            # Tính toán lá số
            try:
                laso_service = LasoTutruService(
                    ngay_sinh=f"{data['nam']}-{data['thang']}-{data['ngay']}",
                    gio_sinh=data['gio'],
                    phut_sinh=data.get('phut', 0),
                    gioi_tinh=1 if data['gioitinh'] == 'nam' else 0,
                    ho_ten=data.get('hoten', '')
                )

                # Tính toán các thông tin cần thiết
                bat_tu = laso_service.tinh_bat_tu()
                tiet_khi = laso_service.get_tiet_khi_hien_tai()
                cung_menh = laso_service.tinh_cung_menh_thai_nguyen()
                chu_tinh = laso_service.tinh_chu_tinh()
                can_tang = laso_service.tinh_can_tang()
                nhat_kien = laso_service.tinh_nhat_kien()
                nguyet_kien = laso_service.tinh_nguyet_kien()
                vts_tru = laso_service.vong_trang_sinh_tru()
                dai_van = laso_service.tinh_dai_van()
                dai_van_list = laso_service.tinh_dai_van_tieu_van()
                nap_am = laso_service.tinh_nap_am()
                do_vuong = laso_service.tinh_do_vuong()
                do_vuong_suy = laso_service.tinh_do_vuong_suy(do_vuong)

                # Xác định dụng thần và hỷ thần
                total = sum(do_vuong_suy['total'].values())
                so_ngu_hanh = int(total * 0.4)
                than_nhuoc = do_vuong_suy['cung_phe'] < so_ngu_hanh or do_vuong_suy['cung_phe'] < 50

                # Cập nhật context với kết quả tính toán
                context.update({
                    'render': True,
                    'ho_ten': data.get('hoten', ''),
                    'ngay_sinh_full': f"{data['ngay']}-{data['thang']}-{data['nam']}",
                    'gio_phut_sinh': f"{data['gio']}:{data.get('phut', 0)}",
                    'gioi_tinh_text': 'Nam' if data['gioitinh'] == 'nam' else 'Nữ',
                    'bat_tu': bat_tu,
                    'tiet_khi': tiet_khi,
                    'cung_menh': cung_menh,
                    'chu_tinh': chu_tinh,
                    'can_tang': can_tang,
                    'nhat_kien': nhat_kien,
                    'nguyet_kien': nguyet_kien,
                    'vts_tru': vts_tru,
                    'dai_van': dai_van,
                    'dai_van_list': dai_van_list,
                    'nap_am': nap_am,
                    'do_vuong_suy': do_vuong_suy,
                    'than_nhuoc': than_nhuoc,
                    'form_data': data,
                })

            except Exception as e:
                messages.error(request, f"Có lỗi xảy ra khi tính toán: {str(e)}")
                context['render'] = False

    return render(request, 'home/laso.html', context)


@csrf_exempt
def create_image_tu_tru(request):
    """API endpoint để tạo file ảnh lá số"""
    if request.method == 'POST':
        try:
            ho_ten = request.POST.get('hoten')
            ngay = request.POST.get('ngay')
            gio = request.POST.get('gio')
            phut = request.POST.get('phut')
            gioi_tinh = request.POST.get('s')

            # Logic tạo file ảnh hoặc PDF
            # Có thể sử dụng PIL, ReportLab, etc.

            # Trả về URL của file đã tạo
            file_url = f"/media/laso/{ho_ten}_{ngay}_{gio}.pdf"
            return JsonResponse({'url': file_url})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


def ajax_bat_tu_calculation(request):
    """AJAX endpoint cho tính toán nhanh"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Xử lý tính toán
            service = LasoTutruService(
                ngay_sinh=data['ngay_sinh'],
                gio_sinh=data['gio_sinh'],
                phut_sinh=data.get('phut_sinh', 0),
                gioi_tinh=data['gioi_tinh'],
                ho_ten=data.get('ho_ten', '')
            )

            result = service.get_basic_info()

            return JsonResponse({
                'success': True,
                'data': result
            })

        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })

    return JsonResponse({'error': 'Method not allowed'}, status=405)
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html', status=404)
