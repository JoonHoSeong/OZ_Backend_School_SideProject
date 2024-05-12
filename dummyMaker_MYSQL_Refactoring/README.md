# Make MySQL Dummy Data for Test

## 사용한 기술 스택
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)![sqlalchemy](https://img.shields.io/badge/sqlalchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)![poetry](https://img.shields.io/badge/poetry-60A5FA?style=for-the-badge&logo=poetry&logoColor=white)![python](https://img.shields.io/badge/python-1D9FD7?style=for-the-badge&logo=python&logoColor=white)
![Faker](https://img.shields.io/badge/Faker-3B66BC?style=for-the-badge&logo=&logoColor=white)
## 👤멤버 구성
[JoonHoSeong](https://github.com/JoonHoSeong)(support by GPT4)

## Case
1. MySQL의 Database에 14개의 테이블을 생성함.
2. Table만 만든 상태라서 테스트를 위해 더미데이터를 테이블 별로 1000개~2만개 사이로 세팅해달라는 요청을 받음
3. 테이블 별로 데이터를 몇 건 씩 세팅할지 지정할 수 있어야함.
4. 더미데이터 생성시마다 데이터를 전부 삭제하고 새로 세팅할지, 추가할지를 지정할 수 있어야함.
5. 하드코딩이 아닌 SQLAlchemy를 통해 각 테이블과 컬럼의 조건 및 이름을 받아서 생성 할 수 있어야함


## Usages
1. Clone the project into your local repository.
2. Install poetry
3. Install Dependancy  
`
poetry install
`  
4. Enter the desired command in command.json  
5. Run Program  
`
poetry run python tests/main.py
`  
## [제작과정 Blog](https://slowprogramer.tistory.com/entry/dummyDataMkaer-SQLAlcehmy%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EB%8D%94%EB%AF%B8%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%83%9D%EC%84%B1-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8-%EB%A7%8C%EB%93%A4%EA%B8%B0-with-MySQL)(작성중)

## Tree
![title](https://github.com/JoonHoSeong/OZ_Backend_School_SideProject/blob/main/dummyMaker_MYSQL_Refactoring/images/tree.png)   


## ERD
![title](https://github.com/JoonHoSeong/OZ_Backend_School_SideProject/blob/main/dummyMaker_MYSQL/image/ERD.png)   
