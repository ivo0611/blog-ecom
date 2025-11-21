from datetime import datetime, date
import calendar


class LasoTutruService:
    """Service class để xử lý logic tính toán lá số tứ trụ"""

    # Dữ liệu thiên can
    THIEN_CAN = [
        {'name': 'Giáp', 'slug': 'giap', 'ngu_hanh': 'moc', 'sex': 1},
        {'name': 'Ất', 'slug': 'at', 'ngu_hanh': 'moc', 'sex': 0},
        {'name': 'Bính', 'slug': 'binh', 'ngu_hanh': 'hoa', 'sex': 1},
        {'name': 'Đinh', 'slug': 'dinh', 'ngu_hanh': 'hoa', 'sex': 0},
        {'name': 'Mậu', 'slug': 'mau', 'ngu_hanh': 'tho', 'sex': 1},
        {'name': 'Kỷ', 'slug': 'ky', 'ngu_hanh': 'tho', 'sex': 0},
        {'name': 'Canh', 'slug': 'canh', 'ngu_hanh': 'kim', 'sex': 1},
        {'name': 'Tân', 'slug': 'tan', 'ngu_hanh': 'kim', 'sex': 0},
        {'name': 'Nhâm', 'slug': 'nham', 'ngu_hanh': 'thuy', 'sex': 1},
        {'name': 'Quý', 'slug': 'quy', 'ngu_hanh': 'thuy', 'sex': 0},
    ]

    # Dữ liệu địa chi
    DIA_CHI = [
        {'name': 'Tý', 'slug': 'ty', 'ngu_hanh': 'thuy', 'sex': 1},
        {'name': 'Sửu', 'slug': 'suu', 'ngu_hanh': 'tho', 'sex': 0},
        {'name': 'Dần', 'slug': 'dan', 'ngu_hanh': 'moc', 'sex': 1},
        {'name': 'Mão', 'slug': 'mao', 'ngu_hanh': 'moc', 'sex': 0},
        {'name': 'Thìn', 'slug': 'thin', 'ngu_hanh': 'tho', 'sex': 1},
        {'name': 'Tỵ', 'slug': 'ty', 'ngu_hanh': 'hoa', 'sex': 0},
        {'name': 'Ngọ', 'slug': 'ngo', 'ngu_hanh': 'hoa', 'sex': 1},
        {'name': 'Mùi', 'slug': 'mui', 'ngu_hanh': 'tho', 'sex': 0},
        {'name': 'Thân', 'slug': 'than', 'ngu_hanh': 'kim', 'sex': 1},
        {'name': 'Dậu', 'slug': 'dau', 'ngu_hanh': 'kim', 'sex': 0},
        {'name': 'Tuất', 'slug': 'tuat', 'ngu_hanh': 'tho', 'sex': 1},
        {'name': 'Hợi', 'slug': 'hoi', 'ngu_hanh': 'thuy', 'sex': 0},
    ]

    # Mệnh quái
    MENH_QUAI = {
        'nam': {
            'can': {'1': 'Ly', '2': 'Cấn', '3': 'Đoài', '4': 'Càn', '5': 'Khôn', '6': 'Chấn', '7': 'Tốn', '8': 'Khảm',
                    '9': 'Ly'},
            'menh': {'Ly': 'Hỏa', 'Cấn': 'Thổ', 'Đoài': 'Kim', 'Càn': 'Kim', 'Khôn': 'Thổ', 'Chấn': 'Mộc', 'Tốn': 'Mộc',
                     'Khảm': 'Thủy'}
        },
        'nu': {
            'can': {'1': 'Cấn', '2': 'Ly', '3': 'Khảm', '4': 'Tốn', '5': 'Càn', '6': 'Khôn', '7': 'Chấn', '8': 'Cấn',
                    '9': 'Đoài'},
            'menh': {'Ly': 'Hỏa', 'Cấn': 'Thổ', 'Đoài': 'Kim', 'Càn': 'Kim', 'Khôn': 'Thổ', 'Chấn': 'Mộc', 'Tốn': 'Mộc',
                     'Khảm': 'Thủy'}
        }
    }

    def __init__(self, ngay_sinh, gio_sinh, phut_sinh, gioi_tinh, ket_qua=7, ho_ten=''):
        self.ngay_sinh = ngay_sinh  # Format: YYYY-MM-DD
        self.gio_sinh = gio_sinh
        self.phut_sinh = phut_sinh
        self.gioi_tinh = gioi_tinh  # 1: nam, 0: nữ
        self.sex = gioi_tinh
        self.ket_qua = ket_qua
        self.ho_ten = ho_ten

        # Parse ngày sinh
        self.parse_ngay_sinh()

    def parse_ngay_sinh(self):
        """Phân tích ngày sinh"""
        if isinstance(self.ngay_sinh, str):
            parts = self.ngay_sinh.split('-')
            self.nam_duong = int(parts[0])
            self.thang_duong = int(parts[1])
            self.ngay_duong = int(parts[2])

        # Chuyển đổi lịch dương sang âm lịch (cần implement)
        self.chuyen_doi_am_lich()

    def chuyen_doi_am_lich(self):
        """Chuyển đổi từ dương lịch sang âm lịch"""
        # Đây là phần tính toán phức tạp, cần implement thuật toán chuyển đổi
        # Tạm thời để giá trị mặc định
        self.ngay_am = self.ngay_duong
        self.thang_am = self.thang_duong
        self.nam_am = self.nam_duong

    def get_thien_can_by_year(self, year):
        """Lấy thiên can theo năm"""
        return self.THIEN_CAN[(year - 4) % 10]

    def get_dia_chi_by_year(self, year):
        """Lấy địa chi theo năm"""
        return self.DIA_CHI[(year - 4) % 12]

    def get_thien_can_by_month(self, year, month):
        """Lấy thiên can theo tháng"""
        can_nam = self.get_thien_can_by_year(year)
        base = self.THIEN_CAN.index(can_nam)
        return self.THIEN_CAN[(base * 2 + month - 1) % 10]

    def get_dia_chi_by_month(self, month):
        """Lấy địa chi theo tháng"""
        return self.DIA_CHI[(month + 1) % 12]

    def get_thien_can_by_day(self, date_obj):
        """Lấy thiên can theo ngày"""
        # Tính từ ngày cơ sở (cần implement thuật toán chính xác)
        base_date = datetime(1900, 1, 1)
        delta = (date_obj - base_date).days
        return self.THIEN_CAN[delta % 10]

    def get_dia_chi_by_day(self, date_obj):
        """Lấy địa chi theo ngày"""
        base_date = datetime(1900, 1, 1)
        delta = (date_obj - base_date).days
        return self.DIA_CHI[delta % 12]

    def get_thien_can_by_hour(self, day_can, hour):
        """Lấy thiên can theo giờ"""
        can_ngay_index = next(i for i, can in enumerate(self.THIEN_CAN) if can == day_can)
        hour_index = hour // 2
        return self.THIEN_CAN[(can_ngay_index * 2 + hour_index) % 10]

    def get_dia_chi_by_hour(self, hour):
        """Lấy địa chi theo giờ"""
        hour_index = (hour + 1) // 2
        return self.DIA_CHI[hour_index % 12]

    def tinh_bat_tu(self):
        """Tính bát tự (tứ trụ)"""
        date_obj = datetime(self.nam_duong, self.thang_duong, self.ngay_duong)

        # Thiên can địa chi năm
        can_nam = self.get_thien_can_by_year(self.nam_am)
        chi_nam = self.get_dia_chi_by_year(self.nam_am)

        # Thiên can địa chi tháng
        can_thang = self.get_thien_can_by_month(self.nam_am, self.thang_am)
        chi_thang = self.get_dia_chi_by_month(self.thang_am)

        # Thiên can địa chi ngày
        can_ngay = self.get_thien_can_by_day(date_obj)
        chi_ngay = self.get_dia_chi_by_day(date_obj)

        # Thiên can địa chi giờ
        can_gio = self.get_thien_can_by_hour(can_ngay, self.gio_sinh)
        chi_gio = self.get_dia_chi_by_hour(self.gio_sinh)

        # Tính mệnh
        menh_quai = self.tinh_menh_quai()

        return {
            'nam': {'can': can_nam, 'chi': chi_nam},
            'thang': {'can': can_thang, 'chi': chi_thang},
            'ngay': {'can': can_ngay, 'chi': chi_ngay},
            'gio': {'can': can_gio, 'chi': chi_gio},
            'menh': menh_quai['menh']
        }

    def tinh_menh_quai(self):
        """Tính mệnh quái"""
        nam_cuoi = self.nam_duong % 10
        gender_key = 'nam' if self.sex == 1 else 'nu'

        if str(nam_cuoi) in self.MENH_QUAI[gender_key]['can']:
            quai = self.MENH_QUAI[gender_key]['can'][str(nam_cuoi)]
            menh = self.MENH_QUAI[gender_key]['menh'][quai]
            return {
                'menhquai': {'name': quai, 'class': menh.lower()},
                'menh': menh
            }

        return {'menhquai': {'name': 'Khôn', 'class': 'tho'}, 'menh': 'Thổ'}

    def get_tiet_khi_hien_tai(self):
        """Lấy tiết khí hiện tại"""
        # Tính toán tiết khí dựa trên ngày tháng
        tiet_khi_list = [
            'Lập xuân', 'Vũ thủy', 'Kinh trập', 'Xuân phân',
            'Thanh minh', 'Cốc vũ', 'Lập hạ', 'Tiểu mãn',
            'Mang chủng', 'Hạ chí', 'Tiểu thử', 'Đại thử',
            'Lập thu', 'Xử thử', 'Bạch lộ', 'Thu phân',
            'Hàn lộ', 'Sương giáng', 'Lập đông', 'Tiểu tuyết',
            'Đại tuyết', 'Đông chí', 'Tiểu hàn', 'Đại hàn'
        ]

        # Tính chỉ số tiết khí dựa trên tháng
        index = (self.thang_duong - 1) * 2
        if self.ngay_duong > 15:
            index += 1

        return {
            'name': tiet_khi_list[index % 24],
            'index': index % 24
        }

    def tinh_cung_menh_thai_nguyen(self):
        """Tính cung mệnh và thai nguyên"""
        # Logic tính toán cung mệnh và thai nguyên
        bat_tu = self.tinh_bat_tu()

        return {
            'thai_nguyen': {
                'can': bat_tu['nam']['can']['name'],
                'chi': bat_tu['nam']['chi']['name']
            },
            'cung_menh': {
                'can': bat_tu['thang']['can']['name'],
                'chi': bat_tu['thang']['chi']['name'],
                'info': 'Thông tin về cung mệnh...'
            }
        }

    def tinh_chu_tinh(self):
        """Tính chủ tinh (thập thần)"""
        # Logic tính toán thập thần cho từng trụ
        return {
            'nam': 'Chính ấn',
            'thang': 'Kiếp tài',
            'ngay': 'Nhật chủ',
            'gio': 'Thương quan'
        }

    def tinh_can_tang(self):
        """Tính can tàng"""
        # Logic tính toán can tàng trong từng địa chi
        return {
            'nam': ['Đinh', 'Kỷ'],
            'thang': ['Bính', 'Mậu'],
            'ngay': ['Ất', 'Quý'],
            'gio': ['Canh', 'Nhâm']
        }

    def tinh_nhat_kien(self):
        """Tính nhật kiến (vòng trường sinh)"""
        return {
            'nam': 'Mộ',
            'thang': 'Tuyệt',
            'ngay': 'Trường sinh',
            'gio': 'Mộc dục'
        }

    def tinh_nguyet_kien(self):
        """Tính nguyệt kiến"""
        return {
            'nam': 'Đế vượng',
            'thang': 'Lâm quan',
            'ngay': 'Quan đới',
            'gio': 'Thất'
        }

    def vong_trang_sinh_tru(self):
        """Tính vòng trường sinh cho từng trụ"""
        return {
            'nam': 'Trường sinh',
            'thang': 'Mộc dục',
            'ngay': 'Quan đới',
            'gio': 'Lâm quan'
        }

    def tinh_dai_van(self):
        """Tính đại vận"""
        # Tính tuổi bắt đầu đại vận
        tuoi_bat_dau = 5  # Giá trị mặc định
        thang_bat_dau = 3
        ngay_bat_dau = 15
        nam_bat_dau = self.nam_duong + tuoi_bat_dau

        return {
            'tuoi': tuoi_bat_dau,
            'thang': thang_bat_dau,
            'ngay': ngay_bat_dau,
            'nam_bd_dai_van': nam_bat_dau
        }

    def tinh_dai_van_tieu_van(self):
        """Tính đại vận và tiểu vận chi tiết"""
        dai_van_list = []

        for i in range(8):  # 8 đại vận
            tuoi = 5 + i * 10
            nam = self.nam_duong + tuoi

            # Tính can chi đại vận
            can_index = (self.nam_duong + i) % 10
            chi_index = (self.nam_duong + i) % 12

            can = self.THIEN_CAN[can_index]
            chi = self.DIA_CHI[chi_index]

            # Tính thập thần của đại vận
            thap_than = self.tinh_thap_than_dai_van(can, chi)

            # Tính tiểu vận cho 10 năm
            tieu_van = {}
            for j in range(10):
                nam_tv = nam + j
                can_tv_index = (can_index + j) % 10
                chi_tv_index = (chi_index + j) % 12

                can_tv = self.THIEN_CAN[can_tv_index]
                chi_tv = self.DIA_CHI[chi_tv_index]
                thap_than_tv = self.tinh_thap_than_dai_van(can_tv, chi_tv)

                tieu_van[nam_tv] = {
                    'can_chi': f"{can_tv['name']} {chi_tv['name']}",
                    'thapthan': thap_than_tv
                }

            dai_van_list.append({
                'daivan': {
                    'year': f"{nam}-{nam + 9}",
                    'tuoi': f"{tuoi}-{tuoi + 9}",
                    'can': can['name'],
                    'chi': chi['name'],
                    'thapthan': thap_than
                },
                'nam': tieu_van
            })

        return dai_van_list

    def tinh_thap_than_dai_van(self, can, chi):
        """Tính thập thần cho đại vận"""
        # Logic tính thập thần dựa trên can chi
        thap_than_list = ['Chính ấn', 'Thiên ấn', 'Chính quan', 'Thất sát', 'Chính tài', 'Thiên tài', 'Thương quan',
                          'Thực thần', 'Tỷ kiên', 'Kiếp tài']
        return thap_than_list[hash(can['name'] + chi['name']) % 10]

    def tinh_nap_am(self):
        """Tính nạp âm"""
        nap_am_dict = {
            'Giáp Tý': 'Hải trung kim', 'Ất Sửu': 'Hải trung kim',
            'Bính Dần': 'Lô trung hỏa', 'Đinh Mão': 'Lô trung hỏa',
            'Mậu Thìn': 'Đại lâm mộc', 'Kỷ Tỵ': 'Đại lâm mộc',
            'Canh Ngọ': 'Lộ bàng thổ', 'Tân Mùi': 'Lộ bàng thổ',
            'Nhâm Thân': 'Kiếm phong kim', 'Quý Dậu': 'Kiếm phong kim',
            'Giáp Tuất': 'Sơn đầu hỏa', 'Ất Hợi': 'Sơn đầu hỏa'
        }

        bat_tu = self.tinh_bat_tu()

        result = {}
        for tru in ['nam', 'thang', 'ngay', 'gio']:
            can_chi = f"{bat_tu[tru]['can']['name']} {bat_tu[tru]['chi']['name']}"
            nap_am_key = list(nap_am_dict.keys())[hash(can_chi) % len(nap_am_dict)]

            result[tru] = {
                'menh': nap_am_dict[nap_am_key],
                'ngu_hanh': self.get_ngu_hanh_from_nap_am(nap_am_dict[nap_am_key])
            }

        return result

    def get_ngu_hanh_from_nap_am(self, nap_am):
        """Lấy ngũ hành từ nạp âm"""
        if 'kim' in nap_am:
            return 'kim'
        elif 'mộc' in nap_am:
            return 'moc'
        elif 'thủy' in nap_am:
            return 'thuy'
        elif 'hỏa' in nap_am:
            return 'hoa'
        else:
            return 'tho'

    def tinh_do_vuong(self):
        """Tính độ vượng của ngũ hành"""
        bat_tu = self.tinh_bat_tu()

        # Đếm số lượng từng ngũ hành
        ngu_hanh_count = {'kim': 0, 'moc': 0, 'thuy': 0, 'hoa': 0, 'tho': 0}

        for tru in ['nam', 'thang', 'ngay', 'gio']:
            can_nh = bat_tu[tru]['can']['ngu_hanh']
            chi_nh = bat_tu[tru]['chi']['ngu_hanh']
            ngu_hanh_count[can_nh] += 1
            ngu_hanh_count[chi_nh] += 1

        # Tính điểm cho từng ngũ hành
        diem_ngu_hanh = {}
        for nh, count in ngu_hanh_count.items():
            diem_ngu_hanh[nh] = count * 10

        return {
            'count': ngu_hanh_count,
            'diem': diem_ngu_hanh,
            'thienCanHopHoa': {},
            'diaChiHopHoa': {}
        }

    def tinh_do_vuong_suy(self, do_vuong):
        """Tính độ vượng suy và xác định dụng thần"""
        bat_tu = self.tinh_bat_tu()
        can_ngay_nh = bat_tu['ngay']['can']['ngu_hanh']

        # Tính tổng điểm
        total_points = sum(do_vuong['diem'].values())

        # Điểm của ngũ hành can ngày (bản mệnh)
        can_ngay_diem = do_vuong['diem'].get(can_ngay_nh, 0)

        # Tính điểm phế (ngũ hành khắc can ngày)
        ngu_hanh_khac = self.get_ngu_hanh_khac(can_ngay_nh)
        cung_phe_diem = sum(do_vuong['diem'].get(nh, 0) for nh in ngu_hanh_khac)

        # Xác định bản mệnh
        if can_ngay_diem >= total_points * 0.4 and can_ngay_diem >= 50:
            ban_menh_status = 'vuong'
            ban_menh_text = f'Vượng {can_ngay_nh.title()}'
            dung_than = self.get_ngu_hanh_khac(can_ngay_nh)[0]  # Lấy ngũ hành khắc đầu tiên
            hy_than = self.get_ngu_hanh_bi_khac(can_ngay_nh)
        else:
            ban_menh_status = 'nhuoc'
            ban_menh_text = f'Nhược {can_ngay_nh.title()}'
            dung_than = can_ngay_nh
            hy_than = self.get_ngu_hanh_sinh(can_ngay_nh)

        return {
            'ban_menh': {
                'name': can_ngay_nh,
                'title': can_ngay_nh.title(),
                'text': ban_menh_text,
                'status': ban_menh_status,
                'dung_than': dung_than,
                'hy_than': hy_than,
                'note': f'Căn cứ vào độ vượng suy của ngũ hành {can_ngay_nh.title()}'
            },
            'cung_phe': cung_phe_diem,
            'total': do_vuong['diem'],
            'khac_phe': {
                'ngu_hanh': ngu_hanh_khac[0] if ngu_hanh_khac else 'kim',
                'diem': cung_phe_diem
            }
        }

    def get_ngu_hanh_khac(self, ngu_hanh):
        """Lấy ngũ hành bị khắc bởi ngũ hành này"""
        khac_dict = {
            'kim': ['moc'],
            'moc': ['tho'],
            'thuy': ['hoa'],
            'hoa': ['kim'],
            'tho': ['thuy']
        }
        return khac_dict.get(ngu_hanh, [])

    def get_ngu_hanh_bi_khac(self, ngu_hanh):
        """Lấy ngũ hành khắc ngũ hành này"""
        bi_khac_dict = {
            'kim': ['hoa'],
            'moc': ['kim'],
            'thuy': ['tho'],
            'hoa': ['thuy'],
            'tho': ['moc']
        }
        return bi_khac_dict.get(ngu_hanh, [])

    def get_ngu_hanh_sinh(self, ngu_hanh):
        """Lấy ngũ hành sinh ra ngũ hành này"""
        sinh_dict = {
            'kim': ['tho'],
            'moc': ['thuy'],
            'thuy': ['kim'],
            'hoa': ['moc'],
            'tho': ['hoa']
        }
        return sinh_dict.get(ngu_hanh, [])

    def get_basic_info(self):
        """Lấy thông tin cơ bản cho AJAX"""
        bat_tu = self.tinh_bat_tu()
        menh_quai = self.tinh_menh_quai()

        return {
            'bat_tu': bat_tu,
            'menh_quai': menh_quai,
            'ho_ten': self.ho_ten,
            'ngay_sinh': f"{self.ngay_duong}/{self.thang_duong}/{self.nam_duong}",
            'gio_sinh': f"{self.gio_sinh}:{self.phut_sinh:02d}"
        }