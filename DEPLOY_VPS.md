# 🚀 VPS Deployment Guide (24/7 AI Trading System)

## 1. เตรียม VPS
- แนะนำ Ubuntu 22.04
- RAM อย่างน้อย 2GB

## 2. ติดตั้ง Docker
```
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
```

## 3. ติดตั้ง Docker Compose
```
sudo apt install docker-compose -y
```

## 4. Clone โปรเจค
```
git clone https://github.com/lnwwinner/AI_Multi_-learnexperience.git
cd AI_Multi_-learnexperience
```

## 5. ตั้งค่า .env
```
nano .env
```
ใส่:
```
IQ_EMAIL=your_email
IQ_PASSWORD=your_password
```

## 6. Run ระบบ
```
docker-compose up -d --build
```

## 7. ตรวจสอบ
```
docker ps
```

## 8. เปิด Dashboard
```
http://YOUR_SERVER_IP:5000
```

---

## 🔁 Auto Restart
ระบบจะ restart อัตโนมัติถ้ามีปัญหา

## 🛑 Stop
```
docker-compose down
```

---

## ✅ Ready
ระบบจะรัน 24/7 อัตโนมัติ
