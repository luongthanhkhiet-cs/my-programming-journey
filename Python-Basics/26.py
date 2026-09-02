import random
import time 
def khoitaonganhang():
    return {
        "Két Sắt A": {"noi_dung": "Vàng", "gia_tri": 500, "do_kho": 3, "đã mở": False},
        "Két Sắt B": {"noi_dung": "Bẫy Báo Động", "gia_tri": 0, "do_kho": 5, "đã mở": False},
        "Két Sắt C": {"noi_dung": "Kim Cương", "gia_tri": 1000, "do_kho": 6, "đã mở": False},
        "Két Sắt D": {"noi_dung": "Tài Liệu Mật", "gia_tri": 300, "do_kho": 4, "đã mở": False},
        "Két Sắt E": {"noi_dung": "Két Trống", "gia_tri": 0, "do_kho": 2, "đã mở": False}
    }
def bekhoa(tenketsat,tuido):
    print(f"bạn đang mở khóa{tenketsat if tenketsat["đã mở"] else "két sắt"} ")
    time.sleep(1)
    diemmayman=random.randint(1,10)
    if tuido["bocaykhoa"]>0:
        print("sử dụng bộ cậy khóa")
        diemmayman+=2
        tuido["bocaykhoa"]-=1
    print(f"điểm cậy khóa của bạn{diemmayman} (độ khó yêu cầu{tenketsat["do_kho"]}")
    return diemmayman >= tenketsat["do_kho"]
    
def choigame():
    ketsat=khoitaonganhang()
    tuido={"bocaykhoa":2}
    tongtien=0
    canhbao=0
    print("chào mừng đến với trò chơi két sắt")
    print("nhiệm vụ là mở sắt nhiều két sắt nhất có thể khi báo động vang lên")
    while canhbao<3:
        ketsatchuamo=[ten for ten,infor in ketsat.items()if not infor["đã mở"]]
        if not ketsatchuamo:
            print("bạn đã mở hết két sắt")
            break 
        print(f"tài sản:{tongtien}/ số lần cảnh báo: {canhbao}/ số công cụ hỗ trợ: {tuido}") 
        print("danh sách két sắt hiện có")
        for ten ,infor in ketsat.items() :
            trangthai=f"đã mở {infor["noi_dung"]}" if infor["đã mở"] else "đang khóa"
            print(f"> {ten}: {trangthai}- độ khó: {infor["do_kho"]}")
        print("\n bạn muosn làm gì tiếp theo")    
        print("1.chọn một két để mở khóa")
        print("2. rút lui an toàn")
        luachon=int(input("nhập lựa chọn(1 hoặc 2) "))
        if luachon==1:
            tenketsat =input("nhập tên két sắt muốn mở ").strip()
            if tenketsat not in ketsat:
                print("tên két không tồn tại")
                continue 
            if ketsat[tenketsat]["đã mở"] :
                print("két sắt này đã mở")
                continue 
            thanhcong=bekhoa(ketsat[tenketsat],tuido)    
            ketsat[tenketsat]["đã mở"]=True
            if thanhcong:
                noidung=ketsat[tenketsat]["noi_dung"]
                giatri=ketsat[tenketsat]["gia_tri"]
                if noidung=="báo động":
                    print("két sắt đã kích hoạt báo động")
                    canhbao+=1
                elif giatri>0:
                    print(f"bạn đã có giá trị là {giatri} ")
                    tongtien+=giatri
                else:
                    print("két sắt này trống rổng")
            else:
                print("mở khóa thất bại, đã kích hoạt báo động")
                canhbao+=1
            time.sleep(1)
        elif luachon==2:
            print("bạn đã dừng cuộc chơi")
            break 
        else:
            print("lựa chọn không hợp ")
    if canhbao>=3:
        print("cảnh báo vang lên, phi vụ thất bại")
choigame()        