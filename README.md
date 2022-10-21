# Visual-Service
Python flask ile oluşturulmuş proje yönetim uygulaması
sudo service postgresql stop

## Api Nasıl çalışır 
İlk olarak api ve veritabanı servislerini oluşturalım.

sudo docker-compose build db
sudo docker-compose up db

Ardından olarak api ve veritabanı servislerini oluşturalım.

sudo docker-compose build api
sudo docker-compose up api

## Web uygulaması nasıl çalışır
sudo docker-compose build api
sudo docker-compose up api

## APİ için çalışan requestler
### Users (Kullanıcılar için requestler)
-----------------------------------------
```
curl --location --request GET 'http://0.0.0.0:5001/users/'


curl --location --request GET 'http://0.0.0.0:5001/users/1'


curl --location --request POST 'http://0.0.0.0:5001/users/add' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "username":"admin",
    "password":"admin"
}'

curl --location --request PUT 'http://0.0.0.0:5001/users/update/1' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "username":"admin",
    "password":"admin123"
}'



curl --location --request DELETE 'http://0.0.0.0:5001/users/delete/2'

# MİMARİ YAPI

1. Api
    * Lib  Folder
        - mail2.py
        - model.py
    * Routers Folder
         - jobs.py
         - users.py
    * Dockerfile
    * main.py
    * requirements.txt
3. docker-compose.yml



 



