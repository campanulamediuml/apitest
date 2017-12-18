package main

import (
    "fmt"
    "strconv"
    )


// func cal_sell(day_list [int]int){


// }

func main(){
    day_list := [][]int {{}}
    var day string
    var sell string
    fmt.Println("输入日期与销量")
    for i:=0;i>=0;i++{
        fmt.Scanln(&day,&sell)
        if day == "done" || sell == "done"{
            break
        }
        day_num,_:=strconv.Atoi(day)
        sell_num,_:=strconv.Atoi(sell)
        day_list[i][day_num] = sell_num
    }
    for i,j:= range day_list{
        fmt.Println(i,j)
    }
}