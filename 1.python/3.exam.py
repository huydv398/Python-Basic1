hoaqua = [ "bơ", "táo", "cam", "chuối", "nho", "bưởi", "khế", "xoài", "quýt", "đào", "mít", "dưa hấu", "lê", "ổi", "dừa"] 
count = len(hoaqua)
print( '- Số lượng hoa quả:', count)

def add_item(value_input):
    if value_input == 1:
        for (i, item) in enumerate(hoaqua, start=1):
            print(i, item)     
        # for x in hoaqua:
        #     print(x)
    elif value_input == 2:
        y = input('Nhập tên quả: ')
        if y in hoaqua:
            print('Quả:', y, '- vị trí: [', hoaqua.index(y) , ']')
        else:
            print('Không có có quả vừa nhập')
        
    elif value_input == 3:
        z = input('Nhập tên quả muốn thêm: ')
        hoaqua.append(z)
        print(hoaqua)
    elif value_input == 4:
        for x in hoaqua:
            print(hoaqua.index(x),'-', x)
        xoa = int(input('Nhập số quả mà bạn muốn xóa: '))
        print(hoaqua[xoa])
        if hoaqua[xoa] in hoaqua:
            hoaqua.pop(xoa)
            print(hoaqua)
            # print(hoaqua[xoa])
        else:
            print('Giá trị nhập không đúng!')
    else :
        print("Nhập giá trị không đúng")
        

print("\n[1] - list ra danh sách quả.")
print("[2] - In tên quả theo vị trí ")
print("[3] - Thêm quả vào List ")
print("[4] - Xóa quả khỏi list \n")
# value_input = input('Nhập số của hành động: ')
value_input = int(input('Nhập số của hành động: '))

add_item(value_input)