#===== MENU ====
def hien_MENU():
    print( "*" * 49)
    print("*" * 10, "CHUONG TRINH HOC THONG MINH","*" * 10 )
    print("*" * 49)
    print("=" *21, "MENU", "=" * 22)
    print("1. Xem lịch")
    print("2. Tính Lương")
    print("3. Xem lương")
    print("4. Xem thông tin nhân viên")
    print("5. Tính điểm của học sinh")
    print("6. Thoát chương trình")
    print("=" *49)

#=======XEM LỊCH =====
def xem_lich(thang):
    if thang in [1,3,5,7,8,10,12]:
        return (f"Tháng {thang} có 31 ngày")
    elif thang in [4,6,9,11]:
        return (f"Tháng {thang} có 30 ngày")
    elif thang == 2:
        nam = int(input("Vui lòng cho biết năm: "))
        if ( nam % 4 == 0 and nam % 100 != 0) or ( nam % 400 == 0):
            return (f"Tháng{thang} có 29 ngày (Năm Nhuận)")
        else:   
            return (f"Tháng {thang} có 28 ngày (Năm Không Nhuận )")  
        
#===== TÍNH LƯƠNG=====
def tinh_luong(luong, gio_lam):
    if gio_lam > 40:
        gio_thuong = 40
        gio_tang_ca = gio_lam -40
    else:
        gio_thuong = gio_lam
        gio_tang_ca = 0
    tien_luong = gio_thuong * luong
    luong_tang_ca = gio_tang_ca * luong *1.5
    return (f"Tiền lương của bạn là: {tien_luong + luong_tang_ca:,.2f} VNĐ")

#===== TÍNH ĐIỂM====
def tinh_diem(diem, he_so, so_mon):  # Cần chỉnh sửa lại 
    tong_diem = 0
    tong_he_so = 0
    tong_diem += diem
    tong_he_so += he_so
    return (f"Điểm trung bình của {so_mon} môn là: {tong_diem/tong_he_so:.2f} điểm.")

def tong_he_so(he_so, so_mon):
    tong_he_so = 0
    tong_he_so+= he_so
    return (f"Tổng hệ số của {so_mon} môn là: {tong_he_so}")

#======XỬ LÝ TÊN NHÂN VIÊN====
def xu_ly_ho_va_ten_lot(ten_nv):
    ds_ten = ten_nv.split()
    # ho_va_ten_lot = ds_ten[:-1]
   # return (f"Họ và tên lót của nhân viên là: {ho_va_ten_lot}")
    # c = ho_va_ten_lot[0] + " " + ho_va_ten_lot[1]
    c = " ".join(ds_ten[:-1])
    return (f"Họ và tên lót của nhân viên là: {c}")

def xu_ly_ten(ten_nv):
    ds_ten = ten_nv.split()
    first_name = ds_ten[-1].title()
    return (f"Tên của nhân viên là: {first_name}")

#====XEM LƯƠNG====
def xem_luong():
    while True:
        danh_sach_luong = []
        danh_sach_nhan_vien = []
        while True:
            try:
                so_luong_nhan_vien = int(input("Nhập số lượng nhân viên: "))
                if so_luong_nhan_vien <0 :
                    print("Bạn phải nhập số lớn hơn 0")
                    continue
                break
            except:
                print("Bạn phải nhập số")
        for i in range(1,so_luong_nhan_vien+1):
            print(f"Nhân viên {i}")
            ten_nhan_vien = input("Nhập tên nhân viên: ").title()
            luong = float(input("Nhập lương nhân viên: "))
            danh_sach_nhan_vien.append(ten_nhan_vien)
            danh_sach_luong.append(luong)
        print("Danh sách nhân viên:")
        print(danh_sach_nhan_vien)
        print("Danh sách lương")
        for dsl in range(len(danh_sach_luong)):
            print(danh_sach_luong[dsl])
        ds_nv_luong = []
        for nvl in range(so_luong_nhan_vien):
            ds_nv_luong.append((danh_sach_nhan_vien[nvl], danh_sach_luong[nvl]))
        ds_nv_luong.sort(key=lambda x: x[1]) # Sắp xếp tên theo thứ tự lương tăng dần
        print("Danh sách tên và lương của nhân viên")
        for ten, luong in ds_nv_luong:
            print(f"{ten}: {luong:,.2f} VNĐ")
        return


#====== CHƯƠNG TRÌNH CHÍNH=====
while True:
    hien_MENU()
    lua_chon = int(input("Mời chọn chức năng của bạn ( 1 - 6): "))
    if lua_chon == 1:   # XEM LỊCH
        while True:
            print("Bạn đã chọn chức năng 1: XEM THÁNG")
            thang = int(input("Nhập tháng muốn xem: "))
            print(xem_lich(thang))
            while True:
                chose = (input("Bạn có muốn tiếp tục chức năng không?( Y/N): ")).upper().strip()
                if chose == "Y":
                    break
                elif chose == "N":
                    print("Bạn đã dừng chức năng")
                    break
                else:
                    print("Chỉ được nhập Y hoặc N") #Chỉnh lại rằng nhập bất kì thứ gì cũng có thể thoát
            if chose == "N":
                break      

    elif lua_chon == 2:    #TÍNH LƯƠNG
        while True:
            print("Bạn đã chọn chức năng 2: TÍNH LƯƠNG")
            luong = float(input("Vui lòng cho biết mức lương của bạn trong 1 giờ: "))
            gio_lam = int(input("Cho biết số giờ làm việc của bạn: "))
            print(tinh_luong(luong, gio_lam))
            while True:
                chose = input("Bạn có muốn tiếp tục không? (Y/N): ").upper().strip()
                if chose == "Y":
                    break
                elif chose == "N":
                    break
                else:
                    print("Chỉ được nhập Y hoặc N")
            if chose == "N":
                break
            
    elif lua_chon == 3:   # XEM LƯƠNG
        while True:
            print("Bạn đã chọn chức năng 3: XEM LƯƠNG")
            xem_luong()
            while True:
                chose = input("Bạn có muốn tiếp tục không? (Y/N): ").upper().strip()
                if chose == "Y":
                    break
                elif chose == "N":
                    break
                else:
                    print("Chỉ được nhập Y hoặc N")
            if chose == "N":
                break
            

    elif lua_chon == 4:   # XEM THÔNG TIN NV
        while True:
            print("Bạn đã lựa chọn chức năng thứ 4: XEM THÔNG TIN NHÂN VIÊN")
            ten_nv = input("Vui lòng nhập tên nhân viên cần xử lý: ").title()
            print(xu_ly_ho_va_ten_lot(ten_nv))
            print(xu_ly_ten(ten_nv))
            print(f"Họ và tên đầy đủ của nhân viên là: {ten_nv}")
            while True:
                chose = input("Bạn có muốn tiếp tục không? (Y/N): ").upper().strip()
                if chose == "Y":
                    break
                elif chose == "N":
                    break
                else:
                    print("Chỉ được nhập Y hoặc N")
            if chose == "N":
                break

    elif lua_chon == 5:    # TÍNH ĐIỂM TRUNG BÌNH
        while True:
            print("Bạn đã chọn chức năng thứ 5: TÍNH ĐIỂM")
            so_mon = int(input("Nhập số môn cần tính điểm trung bình: "))
            for i in range(1, so_mon +1):
                print(f"Môn học thứ {i}")
                diem = float(input("Nhập điểm: "))
                he_so = float(input("Nhập hệ số (1, 1.5, ... 3): "))
            print(tinh_diem(diem, he_so, so_mon))
            print(tong_he_so(diem, he_so))
            print(f"Tổng số môn học là {so_mon} môn ")
            while True:
                chose = input("Bạn có muốn tiếp tục không? (Y/N): ").upper().strip()
                if chose == "Y":
                    break
                elif chose == "N":
                    break
                else:
                    print("Chỉ được nhập Y hoặc N")
            if chose == "N":
                break

    elif lua_chon == 6:  # THOÁT CHƯƠNG TRÌNH
        while True:
            chose = input("Bạn chọn thoát? (Y/N): ").upper().strip()
            if chose == "Y":
                print("TẠM BIỆT")
                exit()
            elif chose == "N":
                break
            break
        continue
    else:
        print("Chỉ được nhập số từ ( 1 - 6)")
        continue

