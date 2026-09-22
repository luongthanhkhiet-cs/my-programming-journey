import time 
import datetime
import random
danhsachbaothuc=[]
def xemdanhsach():
    print("\n danh sách báo thức")
    if not danhsachbaothuc:
        print("chưa có bao thức được cài đặt")
        return
    for baothuc in danhsachbaothuc:
        if baothuc["kichhoat"] :
            trangthai='đang bật'
        else:
            trangthai='đã tắt'
        print(f"ID: {baothuc['id']} | ⏰ {baothuc['gio']} | 📌 {baothuc['nhan']} | {trangthai}")    
def thembaothuc():
    print("\n thêm báo thức mới")
    try:
        gio=int(input("nhập giờ: "))
        phut=int(input("nhập phút: "))
        giay=int(input("nhập giây: "))
        note=input("nhập thêm ghi chú cho báo thức: ")
        if not note:
            note=" báo thức"
    except ValueError:
        print("số không hợp lệ")
        return
    giof= f"{gio:02d}:{phut:02d}:{giay:02d}"
    id= len(danhsachbaothuc)+1
    danhsachbaothuc.append({
        "id":id,
        "gio":giof,
        "nhan":note,
        "kichhoat":True
    })
    print("đã thêm báo thức")
def theodoibaothuc():
    print("\n đang bật chế độ theo dõi báo thức")
    try:
        while True:
            bayh=datetime.datetime.now().strftime("%H:%M:%S")
            sys_time=f"giờ hệ thống: {bayh}| đang theo dõi {len(danhsachbaothuc)} báo thức "
            print(sys_time,end="",flush=True)
            for baothuc in danhsachbaothuc:
                if baothuc["kichhoat"] and baothuc["gio"]==bayh:
                    xulybaothuc(baothuc)
                    return
            time.sleep(1)        
    except KeyboardInterrupt:
        print("\n đã tạp dừng chế độ theo dõi")
def xulybaothuc(baothuc):
    print("\n =============================================================================")
    print(f"báo thức báo thức | {baothuc["nhan"]} - {baothuc["gio"]}")
    print("=============================================================================")
    print("\n bạn muốn làm gì")
    print("1.giải toán để tắt báo thức")
    print("2.hoản báo thức")
    luachon=input("chọn 1 hoặc 2").strip()
    if luachon=="1":
        cauhoi,dapandung=taocauhoi()
        print(f"giải bài toán sau để tắt báo thức: {cauhoi}")
        while True:
            try:
                dapan=int(input("câu trl của bạn là: "))
                if dapan==dapandung:
                    print("báo thức đã được tắt")
                    baothuc["kichhoat"]=False
                    break        
                else:
                    print("sai rồi,thử lại")
            except ValueError:
                print("số ko hợp lệ , thử lại")
    elif luachon=="2":
        bayh=datetime.datetime.now()+datetime.timedelta(minutes=0.5)
        baothuc["gio"]=bayh.strftime("%H:%M:%S")
        print("đã hoản báo thức")
         
def taocauhoi():
    number1=random.randint(0,20)
    number2=random.randint(10,30)
    pheptinh=random.choice(["+","-","*"])
    if pheptinh=="+":
        kqua= number1+number2
    elif pheptinh=="-":   
        kqua=  number1-number2
    elif  pheptinh=="*": 
        kqua= number1* number2
    return f"{number1} {pheptinh} {number2} =?",kqua
def chuongtrinhchinh():
    while True:
        print("ứng dụng đồng hồ báo thức")
        print("1. xem danh sách báo thức")
        print("2. thêm báo thức mới")
        print("3. bắt đầu theo dõi báo thức")
        print("4.thoát")
        luachon=int(input("chọn 1trong4: "))
        if luachon==1:
            xemdanhsach()
        elif luachon==2:
            thembaothuc()
        elif luachon==3:
            if not danhsachbaothuc:
                print("chưa có báo thức nào, hãy thêm báo thức")
            else:
                theodoibaothuc()
        elif luachon==4:
            print("thoát ứng dụng")
            break 
        else:
            print("lựa chọn không hợp lệ")
chuongtrinhchinh()           
            
            
        