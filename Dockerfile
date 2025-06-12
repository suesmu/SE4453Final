# Temel Python imajı
FROM python:3.11-slim

# SSH için gerekli paketleri yükle
RUN apt-get update && apt-get install -y openssh-server

# SSH servisi için klasör oluştur
RUN mkdir /var/run/sshd

# root kullanıcısı için şifre belirle
RUN echo 'root:Docker1234' | chpasswd

# Root login'a izin ver
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Proje klasörüne geç
WORKDIR /app

# Kodları konteynıra kopyala
COPY . /app

# Gerekli Python paketlerini yükle
RUN pip install --no-cache-dir -r requirements.txt

# SSH ve Flask için portları aç
EXPOSE 22 80

# Uygulamayı ve SSH servisini başlat
CMD service ssh start && python app.py
