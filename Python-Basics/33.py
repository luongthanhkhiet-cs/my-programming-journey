import time 
import datetime
import random
class Alarm: 
    def __init__(self,alarmID,timestr,label="báo thức"):
        self.id=alarmID
        self.timestr=timestr
        self.label=label
        self.isActive=True
    def snooze(self,minutes=1):    
        now=datetime.datetime.now()
        newTime=now+datetime.timedelta(minutes=minutes)
        self.timestr=newTime.strftime("%H:%M:%S")
        print(f"đã hoãn báo thức, sẽ báo lại vào lúc: {self.timestr}")
    def deactivate(self):
        self.isActive=False
    def __str__(self):
        if self.isActive:
            status="bật"
        else:
            status="tắt"
        return f"id: {self.id} | {self.timestr} | {self.label} | {status}"
class AlarmManager:
    def __init__(self):
        self.alarms=[]
        self.nextID=1
    def addAlarm(self,timestr,label): 
        alarm=Alarm(self.nextID, timestr,label)
        self.alarms.append(alarm)
        self.nextID+=1
        print(f"đã tạo báo thức thành công {alarm}")
    def showall(self):
        print("\n danh sách các báo thức")
        if not self.alarms:
            print("chưa có báo thức được cài đặt")
            return
        for alarm in self.alarms:
            print(alarm)
    def generatemathquiz(self):
       a=random.randint(1,20)
       b=random.randint(10,30)
       operator=random.choice(["+","-","*"])
       if operator=="+":
           result=a+b
       elif operator=="-":
           result=a-b
       elif operator=="*"  :
           result=a*b
       return f"{a} {operator} {b}",result
    def triggeralarm(self,alarm):
       print("\n =====================================================")
       print(f"BAOTHUC {alarm.label} {alarm.timestr}" )
       print(" =====================================================")
       time.sleep(1)
       print("\n lựa chọn của bạn là")
       print("1.giải toán để tắt báo thức")
       print("2. hoản báo thức")
       choice=input("nhập lựa chọn của bạn : ").strip()
       if choice ==2:
           alarm.snooze(1)
       else:
           quiz,correctanswer==self.generatemathquiz()
           print(f"giải toán để tắt chuông {quiz} =?")
           while True:
               try:
                   answer=int(input("câu trả lời :"))
                   if answer==correctanwser:
                       print("chính xác, báo thức đã được tắt")
                       alarm.deactivate()
                       break 
                   else:
                       print("sai rồi, thử lại")
               except ValueError:
                   print("vui lòng nhập số hợp lệ")
    def startmonitor(self):
        active_alarm=[a for a in self.alarms if a.isActive]
        if not active_alarm:
            print("không có báo thức nào để bật")
            return
        print("hệ thống đang theo dõi báo thứuc")    
        try:
            while True:
                nowtime= datetime.datetime.now().strftime("%H:%M:%S")
                print(f"giờ hiện tại: {nowtime} |  đang theo dõi {len(active_alarm)} báo thức",flush= True)
                for alarm in self.alarms:
                    if alarm.isctive and alarm.timestr==nowtime:
                        self.triggeralarm(alarm)
                        return
                time.sleep(1)
        except KeyboardInterrupt:
            print("đã tạm dừng chế độ theo dõi")

def chuongtrinhchinh ():
    alarm_manager=AlarmManager()
    while True:
        print("\n==========================================================================")
        print("chương trình báo thức")
        print("1. xem danh sách báo thức")
        print("2. thêm báo thức mới")
        print("3. theo dõi báo thức")
        print("4. thoát chương trình")
        choice= int(input("chọn 1 trong các chức năng trên : "))
        if choice == 1:
            alarm_manager.showall()
        elif choice ==2:
            try:
                hour=int(input("nhập vào giờ : "))
                min=int(input("nhập vào phút: "))
                sec=int(input("nhập vào giây: "))
                label=input("nhập vào ghi chú : ")
                timestr=f"{hour:02d}:{min:02d}:{sec:02d} "
                alarm_manager.addAlarm(timestr,label)
            except ValueError :
                print("giờ phút giây phải là số nguyên")
        elif choice== 3:
            alarm_manager.startmonitor()
        elif choice==4:
            print("thoát chương trình")
            break 
        else:
            print("lựa chọn không hợp lệ")
chuongtrinhchinh()            

                
        
    
            
                
                   
       
       
        
        
        

    
