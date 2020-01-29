# airbnb_clone

에어비앤비 클론 코딩

# branch

    master
    develop
    https://gmlwjd9405.github.io/2018/05/11/types-of-git-branch.html

## wsl path

    cd /mnt/c/Users/Seong\ Gi\ Dong/Documents/GitHub/airbnb_clone/

## error

    sudo python3 -m pip uninstall pip && sudo apt-get install python3-pip --reinstall

## setting

    1. pip3 install --user pipenv   or brew install pipenv

    2. pipenv
        window : pipenv install
        mac : pipenv --three

    3. 가상환경시작
        pipenv shell
        python3 -m pipenv shell

    4. Django 설치
        pipenv install Django==2.2.5

    5. django-admin
        djang-admin startporject config
        python manage.py createsuperuser

    6. flake8(개발할때만사용 --dev)
        pipenv install flake8 --dev
        python3 -m pipenv install flake8 --dev

    7. django-admin 생성
        django-admin startapp converstations
        django-admin startapp lists
        django-admin startapp reservations
        django-admin startapp reviews
        django-admin startapp rooms
        django-admin startapp users

    8. models 수정시
        python manage.py makemigrations
        python manage.py migrate

    9. 나라리스트
        pipenv install django-countries

## 데이터 생성

### 1. django-seed 이용

        management / commands 폴더생성
        __init__.py 폴더 필수

### 2. 파일을 생성 후 커맨드입력

        python manage.py seed_amenities
        python manage.py seed_facilities
        python manage.py seed_users --number 50
        python manage.py seed_rooms --number 100
        python manage.py seed_reviews --number 200
        python manage.py seed_lists --number 50
        python manage.py seed_reservations --number 200

### 3. seed 에러

        File "/Users/seong-gidong/.local/share/virtualenvs/airbnb_clone-mj4RvmWF/lib/python3.7/site-packages/django_seed/__init__.py", line 35, in faker
        cls.fakers[code].seed(random.randint(1, 10000))
        => cls.fakers[code].seed_instance(random.randint(1, 10000))

### scss 수정후

    npm run css

### 맥북 mysqlclient 에러시(ssl에러시)

    sudo env LDFLAGS="-I/usr/local/opt/openssl@1.1/include -L/usr/local/opt/openssl@1.1/lib" python3 -m pipenv install Mysqlclient

### Docker

    docker build -t airbnb .
    docker run -p 9000:8000 --rm -it --volume `pwd`:/code/ airbnb

#### Docker 빌드 및 Push

    호스트머신> docker build -t sgd122/airbnb:0.1 .
    호스트머신> docker push sgd122/airbnb:0.1
