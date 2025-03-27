from django.shortcuts import render

def home(request):
    return render(request, "home/home_page.html")  # Đúng theo thư mục templates trong app
# from django.http import HttpResponse
#
# def home(request):
#     return HttpResponse("<h1>Trang chủ đang hoạt động</h1>")
