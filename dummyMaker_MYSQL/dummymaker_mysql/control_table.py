import sqlalchemy as db
from sqlalchemy import text
import os

def insert_dummy_data(selected_table, metadata, engine, data) :
    table = db.Table(selected_table, metadata, autoload=True, autoload_with=engine)
    insert_num = 0
    for d in data :
        try :
            qurey = table.insert().values(d)
            conn = engine.connect()
            conn.execute(qurey)
            conn.commit()
            insert_num += 1
        except :
            continue
    os.system('clear') # 터미널 내용 삭제
    if insert_num == 0 :
        return print("제약조건으로 인해 데이터를 더 추가 할 수 없습니다.")
    return print(f"{insert_num}개의 데이터를 {selected_table} 넣었습니다.")

def truncate_table(selected_table, engine) :
    conn = engine.connect()
    conn.execute(text(f"delete from {selected_table};"))
    conn.execute(text(f"alter table {selected_table} AUTO_INCREMENT = 1;"))
    conn.commit()
    os.system('clear') # 터미널 내용 삭제
    print(f"{selected_table} 내 데이터들을 삭제했습니다.")
        
        
def select_all_data(selected_table, engine) :
    with engine.begin() as conn :
        print(text(f"select * from {selected_table};"))
        result = conn.execute(text(f"select * from {selected_table};"))
    os.system('clear') # 터미널 내용 삭제
    print(f"{selected_table}의 데이터")
    for i in result :
        print(i)
        
def get_table_list(meta_data) :
    table_list = []
    for t in meta_data.sorted_tables :
        table_list.append(t.name)
    return table_list


