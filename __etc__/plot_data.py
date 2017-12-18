#coding=utf-8
dic = {3.0:30.0,7.0:65.0,14.0:130.0,30.0:240.0}
result = sorted(dic.iteritems(), key=lambda d:d[0])
rest = 100
print result
def get_i_30(day_list):
    increase_expect = 0
    for i in range(0,len(day_list)-2):
        increase_expect += ((day_list[i][1]/day_list[i][0])*30.0) - ((day_list[i+1][1]/day_list[i+1][0])*30.0)
    #计算增长率的增长率
    other_expect = 0
    count = 0
    for i in range(0,len(day_list)-2):
        count += 1
        other_expect += (((day_list[i][1]/day_list[i][0])*30.0) - ((day_list[i+1][1]/day_list[i+1][0])*30.0))/(day_list[i+1][0]-day_list[i][0])
    #计算每个周期的增长率的平均数
    day_avg = 0
    for i in day_list:
        day_avg += i[0]
    day_avg = day_avg/count
    #计算平均增长率
    sell_expect = (increase_expect * other_expect)/day_avg

    result_list = []
    result_list = []
    for i in range(1,31):
        result = sell_expect *(i-day_list[0][0]+1) + day_list[0][1]
        result_list.append((i,result))

    return result_list

sel_nextmonth = get_i_30(result)
print sel_nextmonth
for i in sel_nextmonth:
    if i[1]>rest:
        print sel_nextmonth[sel_nextmonth.index(i)-1][0]
        break

# print increase_sell_one_unit