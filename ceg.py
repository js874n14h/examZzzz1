# -*- coding:utf-8 -*-

import apache_log_parser
import datetime as dt
import glob
import os

u1="1"
j1="1"
n1=1
n2=1
from_dt=0
to_dt=0
cc=0
file1=""
dd=False

print("ログファイルが複数の場合ある場合は１を、ない場合は１以外を入力せよ")
j1 = input()

print(j1)
if j1 == "1":
    while u1 == "1" :
    
        print("拡張子含むファイル名とそのファイルの絶対パスを入力せよ")
        print("例:HHH/FFF/pass/xxx.log")
        file1 = input("ファイル名:")
        
        #print(os.path.exists(file1))
        
        # 入力されたパスが存在しているか確認する
        dd=os.path.exists(file1)

        print("変更がある場合は１,ない場合は1以外を入力せよ")
        u1 = input()



#期間指定がある場合のオプション ２つ年月日を入力してその範囲を決定。


print("期間指定")
print("期間指定がある場合1を、ない場合は１以外を入力せよ")
x1 = input()

#print(x1)

#期間指定がある場合 x1==1。
if x1 == "1":
    cc=1
    print("指定範囲１")
    print("year/month/day(2000/04/08)形式で入力せよ")
    while n1 == 1:
        n1=0
        
        #例外処理y ear/month/day(2000/04/08)形式でないなら弾く
        
        try:
            day1 = input()
            dt1=dt.datetime.strptime(day1, '%Y/%m/%d')
        except ValueError:
            print("year/month/day(2000/04/08)形式で入力せよ")
            n1=1
            
    
    print("指定範囲２")
    print("year/month/day(2000/06/09)形式で入力せよ")
    while n2 == 1:
        n2=0
        
        #例外処理 year/month/day(2000/04/08)形式でないなら弾く
        
        try:
            day2 = input()
            dt2=dt.datetime.strptime(day2, '%Y/%m/%d')
        except ValueError:
            print("year/month/day(2000/04/08)形式で入力せよ")
            n2=1
    
    
    #from_dtが開始,to_dtが終了
    if dt2<=dt1:    
        from_dt = dt2
        to_dt = dt1
    else:
        from_dt = dt1
        to_dt = dt2    

#print(from_dt)
#print(to_dt)



a=1
listd = {}
parser = apache_log_parser.make_parser('%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"')



 #絶対パス 任意で変えてください。
#file_list = glob.glob('/Users/yuuyaa/Csd/pyS/*_log')

file_list = glob.glob('/var/log/httpd/access_log')



#入力したファイルが存在するならfile_listの配列に加える。

if dd==True:
    file_list.append(file1)
    
for filename in file_list:
  
  
   
    f = open(filename, 'r')
   
        
        
        
    #readline()を使って一行ごとにファイルを読む。おそらくメモリの問題は解決したと思われるが検証できなかった。
    
    line=f.readline()
    while line:
   
   
        log_data = parser(line)
        
        #期間指定がある場合は指定範囲内かどうかチェックする
        
        if cc==1:
            rr=log_data['time_received_datetimeobj']
            #print(rr)
            if from_dt <= rr <= to_dt:
                ee=log_data['remote_host']
                for src in listd.keys():
                    if ee == src:
                
                        listd[ee]+=1
                        a=0
                        break
              
               
                if a == 1:
                    listd[ee] =1
        
    
                a=1
            
        #期間指定がない場合    
        else:    
            ee=log_data['remote_host']
            for src in listd.keys():
                if ee == src:
                
                    listd[ee]+=1
                    a=0
                    break
              
               
            if a == 1:
                listd[ee] =1
        
    
            a=1
            
        line = f.readline()
       
    
   # print("ddd")    

    
    f.close()
    
    
    
    

#降順にソート
for key, value in sorted(listd.items(), key=lambda x: -x[1]):
    print('{0:<15}: {1:>7}'.format(key, value))
