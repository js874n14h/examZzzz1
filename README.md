# examZzzz1
apacheアクセスログ簡易解析ツール(python３系)\n
apache_log_parserは標準モジュールではないから\n
sudo easy_install apache-log-parser\n
でインポート。\n
datetime,glob,osは標準モジュール

起動方法\n
python ceg.py\n
コマンドラインツール\n
指定ファイルや期間指定が特にない場合は全て0(１以外)を入力すれば、
/var/log/httpd/access_logのアクセスログから各リモートホストのごとのアクセス数を降順で表示。
