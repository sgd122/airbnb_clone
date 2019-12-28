# airbnb_clone
에어비앤비 클론 코딩

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

    6. flake8(개발할때만사용 --dev)
        pipenv install flake8 --dev
        python3 -m pipenv install flake8 --dev