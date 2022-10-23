# Visual-Service
Python flask ile oluşturulmuş Video/Resim yükleme uygulaması 


not:sudo service postgresql stop ,çalışan postgresql veritabanlarını kapatalım.(Docker composedanda portu değiştirebilirsiniz.)

## Api Nasıl çalışır 
İlk olarak api ve veritabanı servislerini oluşturalım.

sudo docker-compose build db
sudo docker-compose up db

Ardından olarak api ve veritabanı servislerini oluşturalım.

sudo docker-compose build api
sudo docker-compose up api

## Apiyi nasıl manuel kullanılır.
http://0.0.0.0:5001/docs  adresine tıklayınız.

Fastapiye bağlı olarak  swagger ile oluşturulmuş ekran karşınıza çıkacaktır.
## Apideki dosyalara nasıl erişilir
Konsoldan "sudo docker exec -t -i api /bin/bash" yazarak erişebilirsiniz.
## Web(React) uygulaması nasıl çalışır
sudo docker-compose build webappp
sudo docker-compose up webappp

# NOT:TAMEMEN YETİŞMEDİ WEB UYGULAMASINI SADECE MİMARİYE DAHİL EDEBİLDİM.

## KULLANILAN ARAÇLAR  VE SEBEPLERİ
1. Fastapi:APİ geliştirme konusunda oldukça yetenekli bir framework.

2. Docker-Compose:Servisleri ayrı ayrı yönetip ölçeklendirmek için düzenlenmiş bir araç

3. Celery:Asenkron kuyruk düzeni ,örneğin kullanıcı büyük bir dosya yüklediğinde kuyruğa aktarıp diğer işlemleri devam etmek için kullandım.

4. Redis:celery için kullandığım veritabanıdır.Ayrı veritabanı kullanma sebebim ise broker vb yapıların kayıtları ayrı ,yazılımın veritabanı ayrı kalmasını istediğim için