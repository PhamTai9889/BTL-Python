danh_sach_nguoi_nop_thue = []

def nhap_thong_tin():
    print("\nNHẬP THÔNG TIN NGƯỜI NỘP THUẾ")
    while True:
        ten = input("Nhập họ tên: ")
        if ten.strip():
            break
        print("Tên không được để trống!")

    while True:
        try:
            thu_nhap = float(input("Nhập tổng thu nhập tháng (VNĐ): "))
            if thu_nhap < 0:
                print("Thu nhập không được âm!")
                continue
            break
        except:
            print("Vui lòng nhập số hợp lệ!")
    
    while True:
        try:
            so_nguoi_phu_thuoc = int(input("Nhập số người phụ thuộc: "))
            if so_nguoi_phu_thuoc < 0:
                print("Số người phụ thuộc không được âm!")
                continue
            break
        except:
            print("Vui lòng nhập số nguyên hợp lệ!")
    
    while True:
        try:
            bao_hiem = float(input("Nhập tổng bảo hiểm (VNĐ): "))
            if bao_hiem < 0:
                print("Bảo hiểm không được âm!")
                continue
            break
        except:
            print("Vui lòng nhập số hợp lệ!")
    
    # Xác nhận thông tin trước khi lưu
    print("\nTHÔNG TIN VỪA NHẬP:")
    print(f"Họ tên: {ten}")
    print(f"Thu nhập: {thu_nhap:,.0f} VNĐ")
    print(f"Số người phụ thuộc: {so_nguoi_phu_thuoc}")
    print(f"Bảo hiểm: {bao_hiem:,.0f} VNĐ")
    
    while True:
        xac_nhan = input("\nBạn có muốn lưu thông tin này? (y/n): ").lower()
        if xac_nhan in ['y', 'n']:
            break
        print("Vui lòng nhập 'y' hoặc 'n'")
    
    if xac_nhan == 'n':
        print("Đã hủy thông tin vừa nhập!")
        return None
    
    return {
        'ten': ten,
        'thu_nhap': thu_nhap,
        'so_nguoi_phu_thuoc': so_nguoi_phu_thuoc,
        'bao_hiem': bao_hiem
    }

def tinh_giam_tru(so_nguoi_phu_thuoc, bao_hiem):
    GIAM_TRU_BAN_THAN = 11000000
    GIAM_TRU_PHU_THUOC = 4400000
    return GIAM_TRU_BAN_THAN + (so_nguoi_phu_thuoc * GIAM_TRU_PHU_THUOC) + bao_hiem

def tinh_thue(thu_nhap_chiu_thue):
    if thu_nhap_chiu_thue <= 5000000:
        return thu_nhap_chiu_thue * 0.05
    elif thu_nhap_chiu_thue <= 10000000:
        return 250000 + (thu_nhap_chiu_thue - 5000000) * 0.1
    elif thu_nhap_chiu_thue <= 18000000:
        return 750000 + (thu_nhap_chiu_thue - 10000000) * 0.15
    elif thu_nhap_chiu_thue <= 32000000:
        return 1950000 + (thu_nhap_chiu_thue - 18000000) * 0.2
    elif thu_nhap_chiu_thue <= 52000000:
        return 4750000 + (thu_nhap_chiu_thue - 32000000) * 0.25
    elif thu_nhap_chiu_thue <= 80000000:
        return 9750000 + (thu_nhap_chiu_thue - 52000000) * 0.3
    else:
        return 18150000 + (thu_nhap_chiu_thue - 80000000) * 0.35

def luu_vao_danh_sach(thong_tin, thue_phai_nop):
    thong_tin['thue_phai_nop'] = thue_phai_nop
    danh_sach_nguoi_nop_thue.append(thong_tin)
    print("\nĐã lưu thông tin thành công!")

def hien_thi_ds():
    if not danh_sach_nguoi_nop_thue:
        print("\nDanh sách trống!")
        return
    
    print("\nDANH SÁCH NGƯỜI NỘP THUẾ")
    # Tiêu đề cột
    print("| {:<4} | {:<20} | {:<15} | {:<10} | {:<10} | {:<15} |".format(
        "STT", "Họ tên", "Thu nhập", "Phụ thuộc", "Bảo hiểm", "Thuế phải nộp"))
    
    for i, nguoi in enumerate(danh_sach_nguoi_nop_thue, 1):
        print("| {:<4} | {:<20} | {:>15,.0f} | {:>10} | {:>10,.0f} | {:>15,.0f} |".format(
            i, 
            nguoi['ten'][:20],  # Giới hạn độ dài tên
            nguoi['thu_nhap'], 
            nguoi['so_nguoi_phu_thuoc'], 
            nguoi['bao_hiem'], 
            nguoi['thue_phai_nop']))
    
    print(f"\nTổng số người: {len(danh_sach_nguoi_nop_thue)}")

def tim_kiem_theo_ten():
    if not danh_sach_nguoi_nop_thue:
        print("\nDanh sách trống!")
        return
    
    ten = input("\nNhập tên cần tìm: ")
    found = False
    
    for nguoi in danh_sach_nguoi_nop_thue:
        if ten.lower() in nguoi['ten'].lower():
            print("\nThông tin tìm thấy:")
            print(f"Họ tên: {nguoi['ten']}")
            print(f"Thu nhập: {nguoi['thu_nhap']:,.0f} VNĐ")
            print(f"Số người phụ thuộc: {nguoi['so_nguoi_phu_thuoc']}")
            print(f"Bảo hiểm: {nguoi['bao_hiem']:,.0f} VNĐ")
            print(f"Thuế phải nộp: {nguoi['thue_phai_nop']:,.0f} VNĐ")
            found = True
    
    if not found:
        print("\nKhông tìm thấy thông tin!")

def sap_xep_theo_thue():
    if not danh_sach_nguoi_nop_thue:
        print("\nDanh sách trống!")
        return
    
    sorted_list = sorted(danh_sach_nguoi_nop_thue, key=lambda x: x['thue_phai_nop'], reverse=True)
    
    print("\nDANH SÁCH SẮP XẾP THEO THUẾ (GIẢM DẦN)")
    print("| {:<4} | {:<20} | {:<15} | {:<10} | {:<10} | {:<15} |".format(
        "STT", "Họ tên", "Thu nhập", "Phụ thuộc", "Bảo hiểm", "Thuế phải nộp"))
    
    for i, nguoi in enumerate(sorted_list, 1):
        print("| {:<4} | {:<20} | {:>15,.0f} | {:>10} | {:>10,.0f} | {:>15,.0f} |".format(
            i, 
            nguoi['ten'][:20],
            nguoi['thu_nhap'], 
            nguoi['so_nguoi_phu_thuoc'], 
            nguoi['bao_hiem'], 
            nguoi['thue_phai_nop']))

def xoa_thong_tin():
    if not danh_sach_nguoi_nop_thue:
        print("\nDanh sách trống!")
        return
    
    ten = input("\nNhập tên người cần xóa: ")
    found = False
    
    for i, nguoi in enumerate(danh_sach_nguoi_nop_thue):
        if ten.lower() == nguoi['ten'].lower():
            print("\nTHÔNG TIN SẼ XÓA:")
            print(f"Họ tên: {nguoi['ten']}")
            print(f"Thu nhập: {nguoi['thu_nhap']:,.0f} VNĐ")
            print(f"Số người phụ thuộc: {nguoi['so_nguoi_phu_thuoc']}")
            print(f"Bảo hiểm: {nguoi['bao_hiem']:,.0f} VNĐ")
            print(f"Thuế phải nộp: {nguoi['thue_phai_nop']:,.0f} VNĐ")
            
            while True:
                xac_nhan = input("\nBạn có chắc chắn muốn xóa? (y/n): ").lower()
                if xac_nhan in ['y', 'n']:
                    break
                print("Vui lòng nhập 'y' hoặc 'n'")
            
            if xac_nhan == 'y':
                del danh_sach_nguoi_nop_thue[i]
                print("\nĐã xóa thông tin thành công!")
            else:
                print("\nĐã hủy thao tác xóa!")
            found = True
            break
    
    if not found:
        print("\nKhông tìm thấy thông tin!")

def tinh_tong_thue():
    if not danh_sach_nguoi_nop_thue:
        print("\nDanh sách trống!")
        return
    
    tong_thue = sum(nguoi['thue_phai_nop'] for nguoi in danh_sach_nguoi_nop_thue)
    print(f"\nTổng số thuế phải nộp: {tong_thue:,.0f} VNĐ")

def thong_ke_thu_nhap():
    if not danh_sach_nguoi_nop_thue:
        print("\nDanh sách trống!")
        return
    
    thu_nhap_list = [nguoi['thu_nhap'] for nguoi in danh_sach_nguoi_nop_thue]
    trung_binh = sum(thu_nhap_list) / len(thu_nhap_list)
    cao_nhat = max(thu_nhap_list)
    thap_nhat = min(thu_nhap_list)
    
    print("\nTHỐNG KÊ THU NHẬP")
    print(f"Thu nhập trung bình: {trung_binh:,.0f} VNĐ")
    print(f"Thu nhập cao nhất: {cao_nhat:,.0f} VNĐ")
    print(f"Thu nhập thấp nhất: {thap_nhat:,.0f} VNĐ")

def sua_thong_tin():
    if not danh_sach_nguoi_nop_thue:
        print("\nDanh sách trống!")
        return
    
    ten = input("\nNhập tên người cần sửa: ")
    found = False
    
    for i, nguoi in enumerate(danh_sach_nguoi_nop_thue):
        if ten.lower() == nguoi['ten'].lower():
            print("\nTHÔNG TIN HIỆN TẠI:")
            print(f"Họ tên: {nguoi['ten']}")
            print(f"Thu nhập: {nguoi['thu_nhap']:,.0f} VNĐ")
            print(f"Số người phụ thuộc: {nguoi['so_nguoi_phu_thuoc']}")
            print(f"Bảo hiểm: {nguoi['bao_hiem']:,.0f} VNĐ")
            print(f"Thuế phải nộp: {nguoi['thue_phai_nop']:,.0f} VNĐ")
            
            print("\nNhập thông tin mới (bấm Enter để giữ nguyên):")
            ten_moi = input(f"Họ tên [{nguoi['ten']}]: ") or nguoi['ten']
            
            while True:
                thu_nhap_moi = input(f"Thu nhập [{nguoi['thu_nhap']:,.0f}]: ")
                if not thu_nhap_moi:
                    thu_nhap_moi = nguoi['thu_nhap']
                    break
                try:
                    thu_nhap_moi = float(thu_nhap_moi)
                    if thu_nhap_moi < 0:
                        print("Thu nhập không được âm!")
                        continue
                    break
                except:
                    print("Vui lòng nhập số hợp lệ!")
            
            while True:
                so_nguoi_moi = input(f"Số người phụ thuộc [{nguoi['so_nguoi_phu_thuoc']}]: ")
                if not so_nguoi_moi:
                    so_nguoi_moi = nguoi['so_nguoi_phu_thuoc']
                    break
                try:
                    so_nguoi_moi = int(so_nguoi_moi)
                    if so_nguoi_moi < 0:
                        print("Số người phụ thuộc không được âm!")
                        continue
                    break
                except:
                    print("Vui lòng nhập số nguyên hợp lệ!")
            
            while True:
                bao_hiem_moi = input(f"Bảo hiểm [{nguoi['bao_hiem']:,.0f}]: ")
                if not bao_hiem_moi:
                    bao_hiem_moi = nguoi['bao_hiem']
                    break
                try:
                    bao_hiem_moi = float(bao_hiem_moi)
                    if bao_hiem_moi < 0:
                        print("Bảo hiểm không được âm!")
                        continue
                    break
                except:
                    print("Vui lòng nhập số hợp lệ!")
            
            print("\nTHÔNG TIN MỚI:")
            print(f"Họ tên: {ten_moi}")
            print(f"Thu nhập: {thu_nhap_moi:,.0f} VNĐ")
            print(f"Số người phụ thuộc: {so_nguoi_moi}")
            print(f"Bảo hiểm: {bao_hiem_moi:,.0f} VNĐ")
            
            while True:
                xac_nhan = input("\nBạn có muốn cập nhật thông tin này? (y/n): ").lower()
                if xac_nhan in ['y', 'n']:
                    break
                print("Vui lòng nhập 'y' hoặc 'n'")
            
            if xac_nhan == 'y':
                danh_sach_nguoi_nop_thue[i]['ten'] = ten_moi
                danh_sach_nguoi_nop_thue[i]['thu_nhap'] = thu_nhap_moi
                danh_sach_nguoi_nop_thue[i]['so_nguoi_phu_thuoc'] = so_nguoi_moi
                danh_sach_nguoi_nop_thue[i]['bao_hiem'] = bao_hiem_moi
                
                giam_tru = tinh_giam_tru(so_nguoi_moi, bao_hiem_moi)
                thu_nhap_chiu_thue = max(0, thu_nhap_moi - giam_tru)
                thue_phai_nop = tinh_thue(thu_nhap_chiu_thue)
                danh_sach_nguoi_nop_thue[i]['thue_phai_nop'] = thue_phai_nop
                
                print("\nĐã cập nhật thông tin thành công!")
            else:
                print("\nĐã hủy thao tác cập nhật!")
            
            found = True
            break
    
    if not found:
        print("\nKhông tìm thấy thông tin!")

def xuat_ra_file():
    if not danh_sach_nguoi_nop_thue:
        print("\nDanh sách trống!")
        return
    
    ten_file = input("\nNhập tên file để lưu (ví dụ: ds_thue.txt): ")
    
    try:
        with open(ten_file, 'w', encoding='utf-8') as f:
            f.write("DANH SÁCH NGƯỜI NỘP THUẾ\n")
            f.write("| {:<4} | {:<20} | {:<15} | {:<10} | {:<10} | {:<15} |\n".format(
                "STT", "Họ tên", "Thu nhập", "Phụ thuộc", "Bảo hiểm", "Thuế phải nộp"))
            
            for i, nguoi in enumerate(danh_sach_nguoi_nop_thue, 1):
                f.write("| {:<4} | {:<20} | {:>15,.0f} | {:>10} | {:>10,.0f} | {:>15,.0f} |\n".format(
                    i, 
                    nguoi['ten'][:20],
                    nguoi['thu_nhap'], 
                    nguoi['so_nguoi_phu_thuoc'], 
                    nguoi['bao_hiem'], 
                    nguoi['thue_phai_nop']))
        
        print(f"\nĐã xuất danh sách ra file '{ten_file}' thành công!")
    except:
        print("\nLỗi khi xuất file!")

def doc_tu_file():
    ten_file = input("\nNhập tên file cần đọc (ví dụ: ds_thue.txt): ")
    
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()[2:]  # Bỏ qua 2 dòng đầu (tiêu đề)
            for line in lines:
                if line.startswith('|') and '|' in line[1:]:
                    parts = [p.strip() for p in line.split('|')[1:-1]]
                    if len(parts) >= 6: 
                        try:
                            stt = parts[0]
                            ten = parts[1]
                            thu_nhap = float(parts[2].replace(',', ''))
                            so_nguoi_phu_thuoc = int(parts[3])
                            bao_hiem = float(parts[4].replace(',', ''))
                            thue = float(parts[5].replace(',', ''))
                            
                            danh_sach_nguoi_nop_thue.append({
                                'ten': ten,
                                'thu_nhap': thu_nhap,
                                'so_nguoi_phu_thuoc': so_nguoi_phu_thuoc,
                                'bao_hiem': bao_hiem,
                                'thue_phai_nop': thue
                            })
                        except:
                            continue
        
        print(f"\nĐã đọc dữ liệu từ file '{ten_file}' thành công!")
    except:
        print("\nLỗi khi đọc file!")

def dem_so_nguoi():
    print(f"\nTổng số người nộp thuế: {len(danh_sach_nguoi_nop_thue)}")

def tim_nguoi_co_thue_cao_nhat():
    if not danh_sach_nguoi_nop_thue:
        print("\nDanh sách trống!")
        return
    
    max_thue = max(danh_sach_nguoi_nop_thue, key=lambda x: x['thue_phai_nop'])
    print("\nNGƯỜI CÓ THUẾ CAO NHẤT")
    print(f"Họ tên: {max_thue['ten']}")
    print(f"Thuế phải nộp: {max_thue['thue_phai_nop']:,.0f} VNĐ")

def tim_nguoi_co_thue_thap_nhat():
    if not danh_sach_nguoi_nop_thue:
        print("\nDanh sách trống!")
        return
    
    min_thue = min(danh_sach_nguoi_nop_thue, key=lambda x: x['thue_phai_nop'])
    print("\nNGƯỜI CÓ THUẾ THẤP NHẤT")
    print(f"Họ tên: {min_thue['ten']}")
    print(f"Thuế phải nộp: {min_thue['thue_phai_nop']:,.0f} VNĐ")

def xoa_toan_bo_danh_sach():
    global danh_sach_nguoi_nop_thue
    if not danh_sach_nguoi_nop_thue:
        print("\nDanh sách đã trống!")
        return
    
    while True:
        xac_nhan = input("\nBạn có chắc chắn muốn xóa TOÀN BỘ danh sách? (y/n): ").lower()
        if xac_nhan in ['y', 'n']:
            break
        print("Vui lòng nhập 'y' hoặc 'n'")
    
    if xac_nhan == 'y':
        danh_sach_nguoi_nop_thue = []
        print("\nĐã xóa toàn bộ danh sách thành công!")
    else:
        print("\nĐã hủy thao tác xóa!")

def menu():
    while True:
        print("\n" + "="*50)
        print("CHƯƠNG TRÌNH QUẢN LÝ THUẾ THU NHẬP CÁ NHÂN".center(50))
        print("="*50)
        print("1. Nhập thông tin")
        print("2. Hiển thị danh sách")
        print("3. Tìm kiếm theo tên")
        print("4. Sắp xếp theo thuế (giảm dần)")
        print("5. Xóa thông tin")
        print("6. Tính tổng thuế")
        print("7. Thống kê thu nhập")
        print("8. Sửa thông tin")
        print("9. Xuất ra file")
        print("10. Đọc từ file")
        print("11. Đếm số người nộp thuế")
        print("12. Người có thuế cao nhất")
        print("13. Người có thuế thấp nhất")
        print("14. Xóa toàn bộ danh sách")
        print("0. Thoát")
        print("="*50)
        
        lua_chon = input("Nhập lựa chọn (0-14): ")
        
        if lua_chon == '1':
            thong_tin = nhap_thong_tin()
            if thong_tin:
                giam_tru = tinh_giam_tru(thong_tin['so_nguoi_phu_thuoc'], thong_tin['bao_hiem'])
                thu_nhap_chiu_thue = max(0, thong_tin['thu_nhap'] - giam_tru)
                thue_phai_nop = tinh_thue(thu_nhap_chiu_thue)
                print(f"\nThuế phải nộp: {thue_phai_nop:,.0f} VNĐ")
                luu_vao_danh_sach(thong_tin, thue_phai_nop)
            input("\nNhấn Enter để tiếp tục...")
        elif lua_chon == '2':
            hien_thi_ds()
            input("\nNhấn Enter để tiếp tục...")
        elif lua_chon == '3':
            tim_kiem_theo_ten()
            input("\nNhấn Enter để tiếp tục...")
        elif lua_chon == '4':
            sap_xep_theo_thue()
            input("\nNhấn Enter để tiếp tục...")
        elif lua_chon == '5':
            xoa_thong_tin()
            input("\nNhấn Enter để tiếp tục...")
        elif lua_chon == '6':
            tinh_tong_thue()
            input("\nNhấn Enter để tiếp tục...")
        elif lua_chon == '7':
            thong_ke_thu_nhap()
            input("\nNhấn Enter để tiếp tục...")
        elif lua_chon == '8':
            sua_thong_tin()
            input("\nNhấn Enter để tiếp tục...")
        elif lua_chon == '9':
            xuat_ra_file()
            input("\nNhấn Enter để tiếp tục...")
        elif lua_chon == '10':
            doc_tu_file()
            input("\nNhấn Enter để tiếp tục...")
        elif lua_chon == '11':
            dem_so_nguoi()
            input("\nNhấn Enter để tiếp tục...")
        elif lua_chon == '12':
            tim_nguoi_co_thue_cao_nhat()
            input("\nNhấn Enter để tiếp tục...")
        elif lua_chon == '13':
            tim_nguoi_co_thue_thap_nhat()
            input("\nNhấn Enter để tiếp tục...")
        elif lua_chon == '14':
            xoa_toan_bo_danh_sach()
            input("\nNhấn Enter để tiếp tục...")
        elif lua_chon == '0':
            print("\nĐã thoát chương trình!")
            break
        else:
            print("\nLựa chọn không hợp lệ!")
            input("\nNhấn Enter để tiếp tục...")

if __name__ == "__main__":
    menu()