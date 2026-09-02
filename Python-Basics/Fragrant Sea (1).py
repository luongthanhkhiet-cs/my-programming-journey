print("phần mềm tính điểm trung bình")
anh = float(input("nhập điểm tiếng anh: "))
toán = float(input("nhập điểm toán: "))
văn = float(input("nhập điểm văn: "))
avg = (toán+anh+văn)/3
print("điểm trung bình của bạn là ",avg)
if avg > 8:
    print("bạn là hsg")
elif avg >= 6.5 and avg < 8:
    print("bạn là hs khá")
elif avg >=5 and avg < 6.5:
    print("bạn là hs trung bình")
else:
    print("bạn là học sinh yếu")
