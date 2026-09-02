import time 
def khoitaothucung(tenthu):
    return{
        "ten":tenthu,
        "suckhoe":100,
        "bungdoi":30, #0 là no,100 la cực đói
        "tamtrang":50,#0 là bùn,100 là vui
        "nangluong":80,#0 la kiet sức ,100 tràn đầy năng lượng
    }
def hienthitrangthai(pet):
    print(f"\n trạng thái của {pet} ")
    print(f"sức khỏe :{pet["suckhoe"]}")
    print(f" mức độ đói {pet["bungdoi"]} ")
    print(f" tâm trạng {pet["tamtrang"]}")
    print(f" năng lượng {pet["nangluong"]}")
def choan(pet):
    print(f"bạn  cho {pet["ten"]} ăn cái đùi gà")
    pet["bungdoi"]-=20
    if pet["bungdoi"]<0:
        pet["bungdoi"]=0
def choidua(pet):
    if pet["nangluong"]<20:
        print("thú cưng của bạn đang mệt")
        return 
    pet["tamtrang"]+=15 
    pet["nangluong"]-=20
def dingu(pet):
    print("thú cưng của bạn đang đi ngủ")
    time.sleep(1)
    pet["nangluong"]+=50
    pet["bungdoi"]+=20
def tgiantroiqua(pet)  :
    pet["bungdoi"]+=10
    pet["tamtrang"]-=5
    if pet["bungdoi"]>=100 or pet["nangluong"]>0 :
        pet["suckhoe"]-=20 
        print("cảnh báo: thú cưng của bạn đang suy kiệt")
    else:
        if  pet["bungdoi"]<50 and pet["nangluong"]>50:
            pet["suckhoe"]+5
            if pet["suckhoe"]>100:
                 pet["suckhoe"]=100
def choigame():
    print("chào mừng bạn đến với trog chơi chăm sóc thú cưng")
    tenthu=input("hãy nhập tên thú cưng: ")
    pet=khoitaothucung(tenthu)
    songay=1
    while pet["suckhoe"]>0:
        hienthitrangthai(pet)
        print(f"\n ngày thứ {songay}")
        print("1. cho ăn")
        print("2. chơi đùa")
        print("3. cho ngủ ")
        print("4. không làm gì cả")
        print("5. rời trò chơi")
        luachon= int(input("bạn chọn hành động nào(1-5)"))
        if luachon==1:
            choan(pet)
        elif luachon==2:
            choidua(pet)
        elif luachon==3:
            dingu(pet)
        elif luachon==4:
            print(f"bạn ngồi ngắm {tenthu} chạy loanh quanh trong nhà")
        elif luachon==5:
            print("bạn đã thoát khỏi trò chơi")
            break 
        else:
            print("lựa chọn không hợp lệ")
            continue 
        tgiantroiqua(pet)
        songay+=1
        time.sleep(1)
    if pet["suckhoe"]<=0:
        print("thú cưng của bạn đã kiệt sức")
        print(f"bạn đã nuôi thú cưng được {songay} ngày ")
choigame()        
        
            