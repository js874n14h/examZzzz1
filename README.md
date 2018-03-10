# examZzzz1
apacheアクセスログ簡易解析ツール(python３系)

apache_log_parserは標準モジュールではないから

sudo easy_install apache-log-parser

でインポート。

datetime,glob,osは標準モジュール

起動方法

python ceg.py

コマンドラインツール

指定ファイルや期間指定が特にない場合は全て0(１以外)を入力すれば、

/var/log/httpd/access_logのアクセスログから各リモートホストのごとのアクセス数を降順で表示。

他に読み込みたいファイルがある場合（１つのみだが）指定できる。存在しなければそのファイルの解析は無視する。

"例:HHH/FFF/pass/xxx.log"

一応ファイル名とパスが正しいか確認しているので正しければ１以外を入力

期間指定

期間を指定したければ年月日を順序関係なく入力

year/month/day(2000/04/08)形式

大小比較で範囲を決定


