import json
from sqlalchemy import create_engine #데이터 베이스와 연결하기 위한 라이브러리
from sqlalchemy import MetaData #메타데이터를 받아오기 위한 라이브러리
from sqlalchemy.engine import reflection #데이터 베이스 내의 정보를 가져오기 위한 라이브러리

def get_connectData(jsonFilePath : str) :
    with open(jsonFilePath) as json_file: #연결 정보 가져오기
        connectData = json.load(json_file)
    del json_file
    return connectData

def connect_DB(connectData : dict) :
    connection_string = f'{connectData['mysql-login']['db_type']}://{connectData['mysql-login']['user_name']}:{connectData['mysql-login']['user_pw']}@{connectData['mysql-login']['db_server']}:{connectData['mysql-login']['db_port']}/{connectData['mysql-login']['db_name']}?charset={connectData['mysql-login']['charset']}'
    engine = create_engine(connection_string, echo=False)
    #메타데이터 가져오기
    metadata = MetaData()
    # 데이터베이스에서 테이블 정보 반영
    metadata.reflect(bind=engine)
    # 터미널 내용 삭제
    # os.system('clear')
    # 데이터베이스 인스펙터 객체 생성
    inspector = reflection.Inspector.from_engine(engine)
    return engine, metadata, inspector

#각 테이블별 제약 조건을 가져오는 함수
def get_tables_detail(tables, inspector): 
    tables_detail = dict()
    #정보 및 제약조건 가져오기
    for table in tables :
        if table not in tables_detail.keys() : 
            tables_detail.update({table : {}})
        columns = inspector.get_columns(table)
        temp = []
        # temp['constrained_columns'] = inspector.get_pk_constraint(table)['constrained_columns']
        for column in columns:
            # Unique 제약 확인
            unique_constraints = inspector.get_unique_constraints(table)
            if any(column['name'] in uc['column_names'] for uc in unique_constraints) :
                column['unique'] = True
            else :
                column['unique'] = False
            temp.append(column)
        #PK 제약조건 가져오기
        temp.append({'table_pk_details' :inspector.get_pk_constraint(table)['constrained_columns']})
        tables_detail.update({table : {'details' : temp}})
        
    # del temp
        del temp
    return tables_detail

#View Detail을 가져오는 함수
def get_view_detail(view_list, inspector) : 
    view_detail = dict()
    #정보 및 제약조건 가져오기
    for view in view_list :
        if view not in view_detail.keys() : 
            view_detail.update({view : {}})
        columns = inspector.get_columns(view)
        temp = []
        # temp['constrained_columns'] = inspector.get_pk_constraint(table)['constrained_columns']
        for column in columns:
            # Unique 제약 확인
            unique_constraints = inspector.get_unique_constraints(view)
            if any(column['name'] in uc['column_names'] for uc in unique_constraints) :
                column['unique'] = True
            else :
                column['unique'] = False
            temp.append(column)
        #PK 제약조건 가져오기
        temp.append({'table_pk_details' :inspector.get_pk_constraint(view)['constrained_columns']})
        view_detail.update({view : {'details' : temp}})
        
    # del temp
        del temp
    return view_detail

#테이블 이름을 가져오는 함수
def get_table_lists(inspector, table_name:str) :
    #테이블 이름 가져오기, 리스트 형식
    return inspector.get_table_names(table_name)
    
#스키마 이름을 가져오는 함수
def get_schema_list(inspector) :
    #리스트 형식으로 스키마 이름 가져오기
    return inspector.get_schema_names()

#뷰 리스트를 가져오는 함수
def get_view_list(inspector) :
    return inspector.get_view_names()
    