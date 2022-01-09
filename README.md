# museum.server
2122I_INT3120_1

## Install
* Install ```python3```
* Then install required modules with this command
```bash
pip install -r requirements.txt
```

## Setup
* Change ```app.config['SQLALCHEMY_DATABASE_URI']``` to your local MySQL connection URI in ```Museum.py```

* Enable IMAP and allow less secure app in your Gmail account 

* Setup your OS environment variable, ```MAIL``` is your email and ```PASS``` is your Gmail password

* Create a ```museum``` database in your MySQL server, then import schema file ```museum.sql``` and data file ```data.sql```

## Run
``` python Museum.py```

## Project structure
```
src---
  |  |- controllers // routes
  |  |- services // validate datas and interact with model layer
  |  |- models // interact with database, query and return query result, insert, update, delete
  |  |- core // core config of this app, including authorization module and secret keys
  |- Museum.py // main running file
  |- database.py // connecting flask to MySQL database
```

## Testing account
Hệ thống có sẵn tài khoản ```teammuseummobile@gmail.com``` với mật khẩu ```Museummobile123``` là tài khoản admin

Tài khoản ```phucpb.hrt@gmail.com``` với mật khẩu ```123456``` là tài khoản user 

## IP change
Khi chạy chỉ BE để test API thì config trong ```Museum.py``` với IP là 127.0.0.1 port 5000 (config mặc định) ở hàm ```main```. Còn nếu kết nối React Native để chạy mobile thì chỉnh ```main``` thành thành IP mạng đang sử dụng, ví dụ như ```app.run(host='192.168.1.103', port=5000, threaded=True, debug=True)```

## Link repository cũ
Vì lý do lỗi file dịch pyc không đưa vào gitignore, nhóm server đã phải đổi repository mới. Thầy có thể xem tiến độ repository cũ tại [đây](https://github.com/tuyenshin2004/MuseumBackend)

