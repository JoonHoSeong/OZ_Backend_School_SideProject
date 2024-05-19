from faker import Faker #더미데이터만들기 위해 사용


#각 테이블별 제약 조건을 가져오는 함수
def get_table_detail(tables, inspector): 
    table_detail = dict()
    #정보 및 제약조건 가져오기
    for table in tables :
        if table not in table_detail.keys() : 
            table_detail.update({table : {}})
        columns = inspector.get_columns(table)
        temp = []
        for column in columns:
            # Unique 제약 확인
            unique_constraints = inspector.get_unique_constraints(table)
            if any(column['name'] in uc['column_names'] for uc in unique_constraints) :
                column['unique'] = True
            else :
                column['unique'] = False
            temp.append(column)
        table_detail.update({table : {'details' : temp}})
        del temp
    return table_detail

# MySQL 자료형별 더미 데이터 생성 함수
def generate_dummy_data(data_dict, fake):
    if data_dict['unique'] :
        fake = fake.unique
    try :        
        if data_dict['data_type'] == 'VARCHAR':
            return fake.pystr(max_chars=data_dict['data_length'])
        elif data_dict['data_type'] =='CHAR':
            return fake.pystr(max_chars=data_dict['data_length'])
        elif data_dict['data_type'] =='TEXT':
            return fake.paragraph()
        elif data_dict['data_type'] =='INTEGER'or data_dict['data_type'] =='MEDIUMINT' or data_dict['data_type'] =='SMALLINT':
            return fake.pyint()
        elif data_dict['data_type'] =='FLOAT' or data_dict['data_type'] =='DOUBLE':
            return fake.pyfloat(left_digits=2, right_digits=2, positive=True)
        elif data_dict['data_type'] =='DECIMAL':
            return fake.pydecimal(left_digits=data_dict['data_left_digits'], right_digits=data_dict['data_right_digits'], positive=True)
        elif data_dict['data_type'] =='DATE':
            return fake.date()
        elif data_dict['data_type'] =='TIME':
            return fake.time()
        elif data_dict['data_type'] =='DATETIME' or data_dict['data_type'] =='TIMESTAMP':
            return fake.date_time()
        elif data_dict['data_type'] =='YEAR':
            return fake.year()
        elif data_dict['data_type'] =='BOOLEAN':
            return fake.boolean()
        elif data_dict['data_type'] =='ENUM':
            return fake.random_element(elements=data_dict['data_options'])
    # elif data_dict['data_type'] =='SET':
    #     return fake.random_elements(elements=('Value 1', 'Value 2', 'Value 3'), unique=True)
        elif data_dict['data_type'] =='BLOB' or data_dict['data_type'] =='BINARY':
            return fake.binary(length=10)
        else:
            return None
    except :
        return 'unique_constraints'
    
# 더미데이터 생성 함수
# 각 컬럼의 속성 값들을 이용해서 더미데이터를 생성할수 있는 정보 딕셔너리를 만들고 이를 기반으로 더미데이터 생성
def create_dummy_data_list(table_name, dummy_num, table_detail) :
    datas = []
    fake = Faker()
    for _ in range(dummy_num) :
        temp = {}
        for row in table_detail[table_name]['details'] :
            data_dict = row.copy()
            try :
                if data_dict['autoincrement'] :
                    continue
            except :
                pass
            data = row['type']
            data_dict['data_type'] = data.__class__.__name__
            if data_dict['data_type'] == 'CHAR' or data_dict['data_type'] == 'VARCHAR' :
                # data_dict['data_charset'] = data.charset
                # data_dict['data_collation'] = data.collation
                data_dict['data_length'] = data.length
            elif data_dict['data_type'] == 'DECIMAL' :
                data_dict['data_left_digits'] = data.precision - data.scale
                data_dict['data_right_digits'] = data.scale
            elif data_dict['data_type'] == 'ENUM' :
                data_dict['data_options'] = data.enums
            # elif data_type == 'INTEGER' or data_type == 'MEDIUMINT':
            #     data_dict['data_unsigned'] = data.unsigned
            elif data_dict['data_type'] == 'TINYINT':
                data_dict['data_display_width'] = data.display_width
            # elif data_type == 'TEXT' :
            #     data_dict['data_charset'] = data.charset
            #     data_dict['data_collation'] = data.collation
            del data_dict['type']
            dummy_data =generate_dummy_data(data_dict, fake)
            if dummy_data == 'unique_constraints' :
                return datas
            temp[data_dict['name']] =  dummy_data
        datas.append(temp)
    del temp
    return datas
    
    