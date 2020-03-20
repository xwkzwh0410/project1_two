#在一个二维数组中（每个一维数组的长度相同），
# 每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


def find_num(data,list):
    if len(list) == 0 and len(list[0]) == 0:
        return False
    for i in range(len(list)):
        if  list[i][0]<= data <= list[i][-1]:
            first_index = 0
            end_index = len(list[0])-1
            while first_index <= end_index:
                mid_index = (first_index + end_index) // 2
                if list[i][mid_index] > data:
                    end_index -= 1
                elif list[i][mid_index] < data:
                    first_index += 1
                elif list[i][mid_index] == data :
                    return True
    return False

print(find_num(7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))



