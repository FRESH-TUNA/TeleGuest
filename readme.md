# TeleGuest
![](./teleguest.jpg)
같은 관심사를 가진 사람들을 위한 게스트하우스 예약 서비스
<br>2019 Newbieton
<br>[teleguest.herokuapp.com](teleguest.herokuapp.com)

## 1. 만든사람
김동원, 김수진, 김영국, 유혜지, 최찬미
<br><br>

## 2. 로컬에서의 구동 방법

### 2.1 가상환경 설치 및 활성화
```
python3 -m venv myvenv
source myvenv/bin/activate
```

### 2.2 Django 설치 및 마이그레이션
```
pip3 install django
python3 manage.py makemigrations --settings=TeleGuest.local_settings
python3 manage.py migrate --settings=TeleGuest.local_settings
```

### 2.3 Django 설치 및 마이그레이션
```
python3 manage.py runserver --settings=TeleGuest.local_settings
```



