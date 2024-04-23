# Make MySQL Dummy Data for Test

## 사용한 기술 스택
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)![sqlalchemy](https://img.shields.io/badge/sqlalchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)![poetry](https://img.shields.io/badge/poetry-60A5FA?style=for-the-badge&logo=poetry&logoColor=white)![python](https://img.shields.io/badge/python-1D9FD7?style=for-the-badge&logo=python&logoColor=white)
![Faker](https://img.shields.io/badge/Faker-3B66BC?style=for-the-badge&logo=&logoColor=white)
## 👤멤버 구성
[JoonHoSeong](https://github.com/JoonHoSeong)

## Case
1. MySQL의 Database에 14개의 테이블을 생성함.
2. Table만 만든 상태라서 테스트를 위해 더미데이터를 테이블 별로 1000개~2만개 사이로 세팅해달라는 요청을 받음
3. 테이블 별로 데이터를 몇 건 씩 세팅할지 지정할 수 있어야함.
4. 더미데이터 생성시마다 데이터를 전부 삭제하고 새로 세팅할지, 추가할지를 지정할 수 있어야함.

## Usages
1. Clone the project into your local repository.
2. Install poetry
3. Install Dependancy  
`
poetry install
`  
4. Run Program  
`
poetry run python tests/main.py
`  
## Tree
![title](http://)   


## ERD
![title](http://)   
