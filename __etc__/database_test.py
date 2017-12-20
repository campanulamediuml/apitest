def sqrt(left_point,right_point,num):
    mid_point = right_point/2
    if ((right_point/2)**2)-num > 1:
        left_point = 0
        right_point = right_point/2
        return sqrt(left_point,right_point,num)
    elif ((right_point/2)**2)-num < 1:
        left_point = right_point/2
        right_point = right_point
        return sqrt(left_point,right_point,num)

print sqrt(0,9,9)