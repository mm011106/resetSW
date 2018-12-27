# Shut down switch
## 機能
- RaspberryPiにシャットダウンスイッチの機能をつけます。
- スイッチを3秒程度押し続けると、シャットダウンコマンドが発行され、電源が切れます。

## 使うもの
- GPIO 17 プルアップ：　シャットダウンスイッチ入力　スイッチをこことGNDの間に接続します。
  - できれば、0.1uF程度のコンデンサをGNDに対して入れるといい。
- GPIO 21 ：シャットダウンプロセスが起動したことを示すLEDのための出力　アクティブHi

## ログファイル
- `/var/log/shutdwnSwitch.log`
- `sudo tailf /var/log/shutdwnSwitch.log` で表示すると動作確認に便利

## サービス設定ファイル
- `/lib/systemd/system/shutdwnSw.service`
- `sudo systemctl status shutdwnSw.service` で確認
- `sudo systemctl stop|start shutdwnSw.service`で、手動で 停止｜起動
