from sqlalchemy import create_engine
from sqlalchemy import MetaData

from tools.control_table import *
from tools.dummy_generator import *

def run_create_dummy(select_table, fake_data_num, method, engine, metadata) :
    if  method :
        truncate_table(selected_table=select_table, engine=engine)
    if select_table == 'airline' :
        data = create_airline_dummy_data(fake_data_num=fake_data_num)
        insert_dummy_data(selected_table=select_table, engine=engine, metadata=metadata, data=data)
    elif select_table == 'airport' :
        data = create_airport_dummy_data(fake_data_num=fake_data_num)
        insert_dummy_data(selected_table=select_table, engine=engine, metadata=metadata, data=data)
    elif select_table == 'airplane_type' :
        data = create_airplanetype_dummy_data(fake_data_num=fake_data_num)
        insert_dummy_data(selected_table=select_table, engine=engine, metadata=metadata, data=data)
    elif select_table == 'airplane' :
        data = create_airplane_dummy_data(fake_data_num=fake_data_num)
        insert_dummy_data(selected_table=select_table, engine=engine, metadata=metadata, data=data)
    elif select_table == 'airport_geo' :
        data = create_airportgeo_dummy_data(fake_data_num=fake_data_num)
        insert_dummy_data(selected_table=select_table, engine=engine, metadata=metadata, data=data)
    elif select_table == 'airport_reachable' :
        data = create_airport_reachable_dummy_data(fake_data_num=fake_data_num)
        insert_dummy_data(selected_table=select_table, engine=engine, metadata=metadata, data=data)
    elif select_table == 'employee' :
        data = create_employee_data(fake_data_num=fake_data_num)
        insert_dummy_data(selected_table=select_table, engine=engine, metadata=metadata, data=data)
    elif select_table == 'flight_log' :
        data = create_flight_log_data(fake_data_num=fake_data_num)
        insert_dummy_data(selected_table=select_table, engine=engine, metadata=metadata, data=data)
    elif select_table == 'flight' :
        data = create_flight_data(fake_data_num=fake_data_num)
        insert_dummy_data(selected_table=select_table, engine=engine, metadata=metadata, data=data)
    elif select_table == 'flightschedule' :
        data = create_flightschedule_data(fake_data_num=fake_data_num)
        insert_dummy_data(selected_table=select_table, engine=engine, metadata=metadata, data=data)
    elif select_table == 'passenger' :
        data = create_passenger_data(fake_data_num=fake_data_num)
        insert_dummy_data(selected_table=select_table, engine=engine, metadata=metadata, data=data)
    elif select_table == 'weatherdata' :
        data = create_weatherdata_data(fake_data_num=fake_data_num)
        insert_dummy_data(selected_table=select_table, engine=engine, metadata=metadata, data=data)
    elif select_table == 'passengerdetails' :
        data = create_passengerdetails_data(fake_data_num=fake_data_num)
        insert_dummy_data(selected_table=select_table, engine=engine, metadata=metadata, data=data)
    elif select_table == 'booking' :
        data = create_booking_dummy_data(fake_data_num=fake_data_num)
        insert_dummy_data(selected_table=select_table, engine=engine, metadata=metadata, data=data)
    
def run() :
    engine = create_engine(f'mysql+pymysql://root:root@localhost:3306/airportdb?charset=utf8mb4', echo=True)
    metadata = MetaData()
    metadata.reflect(engine)
    os.system('clear') # 터미널 내용 삭제
    ## 입력관련 만들기
    while True :
        table_list = get_table_list(meta_data = metadata)
        ## 실행, 종료 여부 확인 문
        try  :
            do_signal = int(input('더미데이터 생성 프로그램 실행 여부를 선택해 주세요(종료 : 0, 생성 : 1, 조회 : 2) : '))
            if do_signal != 0 and do_signal != 1 and do_signal != 2 :
                raise
            if do_signal == 1 or do_signal == 2:
                print("프로그램을 실행 합니다.")
                pass
            else :
                print("프로그램을 종료 합니다.")
                break
        except :
            print('잘못된 값을 입력하셨습니다. 다시 입력하세요.')
        
        ## 테이블 선택
        while True :
            print(table_list)
            select_table = input('실행을 원하는 테이블 이름을 입력해 주세요. : ')
            if select_table in table_list :
                break
            print('없는 테이블을 입력하셨습니다. 다시 입력해주세요')
        
        if do_signal == 2 :
            select_all_data(selected_table=select_table, engine=engine)
            continue
        
        ## 더미 데이터 수 입력
        while True :
            try :
                fake_data_num = int(input('생성할 더미데이트의 수를 입력해주세요(1000~2만 사이의 값) : '))
                if fake_data_num >= 1000 and fake_data_num <= 20000 :
                    break
                raise
            except :
                print('잘못된 입력입니다. 다시 입력해주세요')
                continue
        
        ## 실행 방식 설정
        while True :
            try :
                method = int(input('원하는 생성 방식을 선택하세요(더미데이터 추가 : 0, 테이블 삭제후 생성:1) : '))
                if method != 0 and method != 1 :
                    raise
                if method == 1 :
                    truncate_table(selected_table=select_table, engine=engine)
                print("프로그램을 실행 합니다.")
                run_create_dummy(select_table, fake_data_num, method, engine, metadata)
                break
            except :
                print('잘못된 입력입니다. 다시 입력해주세요')
                continue

    
if __name__== "__main__" :
    run()