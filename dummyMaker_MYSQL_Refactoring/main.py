import json
import os
from sqlalchemy import create_engine #데이터 베이스와 연결하기 위한 라이브러리
from sqlalchemy import MetaData #메타데이터를 받아오기 위한 라이브러리
from sqlalchemy.engine import reflection #데이터 베이스 내의 정보를 가져오기 위한 라이브러리
from faker import Faker #더미데이터만들기 위해 사용

from tools.control_table import * #데이터를 DB에 적용
from tools.create_dummy_data import * #더미데이터 생성


def main() :
    with open('setting/config.json') as json_file: #연결 정보 가져오기
        connectData = json.load(json_file)
    del json_file

    with open('command.json') as json_file: #연결 정보 가져오기
        commandData = json.load(json_file)
    del json_file

    connection_string = f'{connectData['mysql-login']['db_type']}://{connectData['mysql-login']['user_name']}:{connectData['mysql-login']['user_pw']}@{connectData['mysql-login']['db_server']}:{connectData['mysql-login']['db_port']}/{connectData['mysql-login']['db_name']}?charset={connectData['mysql-login']['charset']}'
    #데이터 베이스와 연결하기
    engine = create_engine(connection_string, echo=False)
    #메타데이터 가져오기
    metadata = MetaData()
    # 데이터베이스에서 테이블 정보 반영
    metadata.reflect(bind=engine)
    # 터미널 내용 삭제
    # os.system('clear')
    # 데이터베이스 인스펙터 객체 생성
    inspector = reflection.Inspector.from_engine(engine)

    #테이블 이름 가져오기
    tables = inspector.get_table_names()

    table_detail = get_table_detail(tables, inspector)
    for table_name in commandData['table_names'].split(', ') :
    # for table_name in tables : #For Test
        if table_name not in tables :
            print(f'{table_name}테이블은 데이터 베이스에 존재하지 않는 테이블 이름 입니다.')
            continue
        
        if commandData['command'] == 'insert' :
            print(f'{table_name}테이블 더미데이터 생성을 시작합니다.')
            dummy_data = create_dummy_data_list(table_name,commandData['dummy_num'], table_detail)
            print(f'더미데이터 {len(dummy_data)}건 생성 완료')
            insert_dummy_data(selected_table=table_name, engine=engine, metadata=metadata, data=dummy_data)
        elif commandData['command'] == 'new_insert' :
            truncate_table(selected_table=table_name, engine=engine)
            print(f'{table_name}테이블 초기화 완료.')
            print(f'{table_name}테이블 더미데이터 생성을 시작합니다.')
            dummy_data = create_dummy_data_list(table_name,commandData['dummy_num'], table_detail)
            insert_dummy_data(selected_table=table_name, engine=engine, metadata=metadata, data=dummy_data)
            print(f'더미데이터 {len(dummy_data)}건 생성 완료')
        elif commandData['command'] == 'view' :
            select_all_data(selected_table=table_name, engine=engine)
        else :
            print('정해진 실행 방식외 작동을 시도했습니다.\n프로그램을 종료합니다.')
            
if __name__ == '__main__' :
    main()
