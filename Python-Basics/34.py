import os
class Task:
    def __init__(self,taskid,title,priority="trung bình"):
        self.id=taskid
        self.title=title
        self.priority=priority
        self.completed=False
    def mark_done(self):
        self.completed= True
    def __str__(self):
        status="hoàn thành " if self.completed else " chưa xong"
        return f"{self.id} {self.title} | độ ưu tiên: {self.priority} | trạng thái: {self.completed} " 
class Taskmanager:
    def __init__(self):
        self.tasks=[]
        self.nextid=1
    def add_task(self,title,priority="trung bình"):
        newtask=Task(self.nextid,title,priority)
        self.tasks.append(newtask)
        self.nextid+=1
        print(f"đã thêm nhiệm vụ {title}")
    def listtask(self):
        print("\n danh sách nhiệm vụ ")
        if not self.tasks:
            print("chưa có nhiệm vụ nào trong danh sách")
            return
        for task in self.tasks:
            print(task)
    def completed_task(self, taskid):
        for task in self.tasks:
            if task.id ==taskid:
                task.mark_done()
                print(f"đã hoàn thành nhiệm vụ {task.title}")
                return
        print("không tìm thấy nhiệm vụ ")         
    def show_state(self):
        if not self.tasks:
            print("chưa có dữ liệu về thống kê")
            return
        total=len(self.tasks)
        completed=sum(1 for t in self.tasks if t.completed)
        percent=(completed/total)*100
        print("\n thống kê tiến độ")
        print(f" tổng số nhiệm vụ: {total}")
        print(f"tổng số nhiệm vụ đã hoàn thành : {completed}")
        print(f" số nhiệm vụ còn lại {total-completed}")
        print(f" tiến độ : { percent}")

def chuongtrinhchinh():
    manager=Taskmanager()
    while True:
        print("\n ============================================")
        print("chương trình quản lý nhiệm vụ cá nhân")
        print(" ============================================")
        print("1. xem danh sách nhiệm vụ")
        print("2. thêm nhiệm vụ mới ")
        print("3. đánh dấu hoàn thành nhiệm vụ")
        print("4. xem thống kê tiến độ")
        print("5.thoát chương trình")
        luachon= int(input("chọn 1 trong 5 chức năng: "))
        if luachon==1:
            manager.listtask()
        elif luachon==2:
            title=input("nhập tên nhiệm vụ: ").strip()
            if not title :
                print("tên nhiệm vụ ko dc trống")
                continue 
            print("mức độ ưu tiên: 1. thấp | 2.trung bình | 3.cao")
            douutien=input("chọn độ ưu tiên(1,2,3)").strip()
            list_douutien={"1":"thấp", "2":"trung bình" , "3": "cao"}
            choice= list_douutien.get(douutien,"trung bình")
            manager.add_task(title,choice)
        elif luachon==3:
            manager.listtask()
            if manager.tasks:
                try:
                    taskid=int(input("nhập id nhiệm vụ đã hoàn thành:  "))
                    manager.completed_task(taskid)
                except ValueError:
                    print("vui lòng nhập số nguyên hợp lệ")
        elif luachon==4:
            manager.show_state()
        elif luachon==5:
            print("thoát chương trình")
            break 
        else:
            print("lựa chọn không hợp lệ")
chuongtrinhchinh()
            
            
            
            
        
        
        
        
        
    