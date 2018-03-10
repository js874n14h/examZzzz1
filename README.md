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
