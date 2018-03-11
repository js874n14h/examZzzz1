# examZzzz1



## apacheアクセスログ簡易解析ツール(python３系)

リモートホストごとのアクセス数を表示する

apache_log_parserは標準モジュールではないから

`sudo easy_install apache-log-parser`

でインストール。

datetime,glob,osは標準モジュール         

### ソースの解説
apache_log_parserで要素ごとのkeyとvalueに分けている。

`parser = apache_log_parser.make_parser('%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"')`

`log_data = parser(line)`

logの形式を指定して各要素をディクショナリ型の配列にしている。

リモートホストのアドレスと日時のkey

`log_data['remote_host']`

`log_data['time_received_datetimeobj']`

年日時はdatetime型であり、比較可能

リモートホストがkeyにカウントしてあればvalueに+1、していなければkeyに登録してvalueに1を代入する。
```
 ee=log_data['remote_host']
                for src in listd.keys():
                    if ee == src:
                
                        listd[ee]+=1
                        a=0
                        break
              
               
                if a == 1:
                    listd[ee] =1
        
    
                a=1

```


## 起動方法

`python ceg.py`で起動


コマンドラインツール

指定ファイルや期間指定が特にない場合は全て0(１以外)を入力すれば、

/var/log/httpd/access_logのアクセスログから各リモートホストのごとのアクセス数を降順で表示。 

デフォルトでは/var/log/httpd/access_logのアクセスログを解析



## 複数ファイル


ある場合は１を入力、ない場合は１以外を入力


他に読み込みたいファイルがある場合（１つのみだが）指定できる。存在しなければそのファイルの解析は無視する。


"例:HHH/FFF/pass/xxx.log"(絶対パス)


一応ファイル名とパスが正しいか確認しているので正しければ１以外を入力       




## 期間指定


ある場合は１を入力、ない場合は１以外を入力           



期間を指定したければ年月日を順序関係なく入力

year/month/day(2000/04/08)形式

大小比較で範囲を決定           

半端なエラー処理のため正しい形式の入力がなければ終わらない。(要改良)




## メモリ不足


readline()でファイルを一行ずつ読んでいるのでメモリ不足は起こらないと考えられるが未検証。




