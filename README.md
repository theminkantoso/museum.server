# museum.server
2122I_INT3120_1

## Install
* Install ```python3```
* Then install required modules with this command
```bash
pip install -r requirements.txt
```

## Setup
* Change ```app.config['SQLALCHEMY_DATABASE_URI']``` to your local MySQL connection URI in ```citizenV.py```

* Enable IMAP and allow less secure app in your Gmail account 

* Setup your OS environment variable, ```MAIL``` is your email and ```PASS``` is your Gmail password

* Setup your Google GCP Console Credentials, with ```'/'``` route as default and ```'/authorize'``` as redirect, then setup your OS environment variable ```'GOOGLE_CLIENT_ID``` as your client_id and ```GOOGLE_CLIENT_SECRET``` as your client_secret

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

