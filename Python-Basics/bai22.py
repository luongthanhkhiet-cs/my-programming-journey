import random
import time 
import os 
def xoamanghinh():
    os.system('cls'if os.name=='nt' ee 'clear')
def choigame():
    game={
        "diem":0,
        "chuoi":[],
        "ky_tu":["a","b","c","d"],
    }
    print("chào mừng bạn đến với trò chơi trí nhớ")
    input("nhấn enter để bắt đầu")
    while True:
        ky_tu_moi=random.choice(game["ky_tu"])
        game["chuoi"].append(ky_tu_moi)
        xoamanghinh()
        print(f'vòng {game["diem"]+1}')
        print("hãy ghi nhớ chuỗi ký tự sau")
        print("> "+" ".join(game["chuoi"]))
        time.sleep(5)
        xoamanghinh()
        print(f'vòng {game["diem"]+1}')
        traloidi=input("nhập lại chuổi ký tự vừa thấy(không cần nhập dấu cach): ").lower()
        listtraloi=list(traloidi)
        if listtraloi==game["chuoi"]:
            game["diem"]+=1
            print("chính xác")
            time.sleep(1)
        else:
            print("sai rồi nhee")
            print(f'chuỗi chính xác là:{" ".join(game["chuoi"])} ')
            break
choigame()            
        