# Shutdown switch for RaspberryPi
## 機能
- RaspberryPiにシャットダウンスイッチの機能をつけます。
- スイッチを3秒程度押し続けると、シャットダウンコマンドが発行され、電源が切れます。

## 使うもの
- __GPIO 17__ プルアップ：　シャットダウンスイッチ入力　スイッチをこことGNDの間に接続します。
  - できれば、0.1uF程度のコンデンサをGNDに対して入れるといい。
- __GPIO 21__ ：シャットダウンプロセスが起動したことを示すLEDのための出力　アクティブHi

## ログファイル
- `/var/log/shutdwnSwitch.log`
- `sudo tailf /var/log/shutdwnSwitch.log` で表示すると動作確認に便利

## サービス設定ファイル
- `/lib/systemd/system/shutdwnSw.service`
- `sudo systemctl status shutdwnSw.service` で確認
- `sudo systemctl stop|start shutdwnSw.service`で、手動で 停止｜起動
- `sudo systemctl enable shutdwnSw.service`で、永続化


## 動作確認例
```
$ sudo systemctl status shutdwnSw.service 
● shutdwnSw.service - Shutdown Switch watcher
   Loaded: loaded (/lib/systemd/system/shutdwnSw.service; enabled; vendor preset
   Active: active (running) since Sun 2019-03-31 02:39:17 BST; 5min ago
 Main PID: 215 (python2.7)
   CGroup: /system.slice/shutdwnSw.service
           └─215 /usr/bin/python2.7 /home/pi/documents/resetSW/shutdwnSwitch.py

Mar 31 02:39:17 raspberrypi systemd[1]: Started Shutdown Switch watcher.
```

[systemctl](https://qiita.com/sinsengumi/items/24d726ec6c761fc75cc9)コマンドについて
