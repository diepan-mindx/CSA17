# nguoi dung nhap tu console so nguyen duong n 
# in ra tam giac vuong voi n dong + so luong * = so thu tu dong

#vd: n = 3
#*
#**
#***

while True:
    n = input("Nhap so nguyen duong n: ")
    if n == "exit":
        print("Tam biet!")
        break
    try:
        n = int(n)
        if n <= 1:
            print("Vui long nhap so nguyen duong!")
            continue
    except Exception as e:
        print("Loi: ", e)
        continue
        
    for i in range (n):
        print("*" * (i + 1))
