import random
from faker import Faker
from faker_airtravel import AirTravelProvider

def create_airline_dummy_data(fake_data_num) :
    Faker.seed(random.random())
    faker = Faker()
    faker.add_provider(AirTravelProvider)
    data = []
    for _ in range(fake_data_num) :
        try :
            iata = faker.unique.hexify(text='^^', upper=True)
            airlineName = faker.airline()
            base_airport = faker.random_int(1,2**15-1)
            data.append({'iata' : iata, 'airlinename' : airlineName, 'base_airport' : base_airport})
        except :
            print(f"{len(data)}개의 데이터를 생성 했습니다. 제약조건으로 인해 더이상 생성 할 수 없습니다.")
            return data
    print(f"{len(data)}개의 데이터를 생성 했습니다.")
    return data

def create_airport_dummy_data(fake_data_num) :
    Faker.seed(random.random())
    faker = Faker()
    faker.add_provider(AirTravelProvider)
    data = []
    for _ in range(fake_data_num) :
        try :
            iata = faker.airport_iata()
            icao = faker.unique.lexify(text='???')
            name = faker.airport_name()
            data.append({'iata' : iata, 'icao' : icao, 'name' : name})
        except :
            print(f"{len(data)}개의 데이터를 생성 했습니다. 제약조건으로 인해 더이상 생성 할 수 없습니다.")
            return data
    print(f"{len(data)}개의 데이터를 생성 했습니다.")
    return data

def create_airplanetype_dummy_data(fake_data_num) :
    Faker.seed(random.random())
    faker = Faker()
    data = []
    for _ in range(fake_data_num) :
        try :
            identifier = faker.unique.bothify(text='??####')
            description = faker.text()
            data.append({'identifier' : identifier, 'description' : description})
        except :
            print(f"{len(data)}개의 데이터를 생성 했습니다. 제약조건으로 인해 더이상 생성 할 수 없습니다.")
            return data
    print(f"{len(data)}개의 데이터를 생성 했습니다.")
    return data

def create_airplane_dummy_data(fake_data_num) :
    Faker.seed(random.random())
    faker = Faker()
    data = []
    for _ in range(fake_data_num) :
        try :
            capacity = faker.random_int(1,2**23-1)
            type_id = faker.random_int(1,2**31-1)
            airline_id = faker.random_int(1,2**31-1)
            data.append({'capacity' : capacity, 'type_id' : type_id, 'airline_id' : airline_id})
        except :
            print(f"{len(data)}개의 데이터를 생성 했습니다. 제약조건으로 인해 더이상 생성 할 수 없습니다.")
            return data
    print(f"{len(data)}개의 데이터를 생성 했습니다.")
    return data

def create_airportgeo_dummy_data(fake_data_num) :
    Faker.seed(random.random())
    faker = Faker()
    faker.add_provider(AirTravelProvider)
    data = []
    for _ in range(fake_data_num) :
        try :
            airport_id = faker.random_int(1,2**15-1)
            name = faker.airport_name()
            city = faker.city()
            country = faker.country()
            latitude = faker.latitude()
            longitude = faker.longitude()
            data.append({'airport_id' : airport_id, 'name' : name, 'city' : city,'country' : country, 'latitude' : latitude, 'longitude' : longitude})
        except :
            print(f"{len(data)}개의 데이터를 생성 했습니다. 제약조건으로 인해 더이상 생성 할 수 없습니다.")
            return data
    print(f"{len(data)}개의 데이터를 생성 했습니다.")
    return data

def create_airport_reachable_dummy_data(fake_data_num) :
    Faker.seed(random.random())
    faker = Faker()
    data = []
    for _ in range(fake_data_num) :
        try :
            airport_id = faker.random_int(1,2**15-1)
            hops = faker.random_int(1,2**31-1)
            data.append({'airport_id' : airport_id, 'hops' : hops})
        except :
            print(f"{len(data)}개의 데이터를 생성 했습니다. 제약조건으로 인해 더이상 생성 할 수 없습니다.")
            return data
    print(f"{len(data)}개의 데이터를 생성 했습니다.")
    return data

def create_employee_data(fake_data_num) :
    Faker.seed(random.random())
    faker = Faker()
    data = []
    for _ in range(fake_data_num) :
        try :
            firstname = faker.first_name()
            lastname = faker.last_name()
            birthdate = faker.date_of_birth()
            sex = faker.bothify(text='?', letters='MF')
            street = faker.street_name()
            city = faker.city()
            zip_code = faker.random_int(1, 2**15-1)
            country = faker.country()
            emailaddress = faker.email()
            telephoneno = faker.phone_number()
            salary = faker.pydecimal(min_value=0.01,right_digits=2, max_value=999999)
            department = random.choice(['Marketing','Buchhaltung','Management','Logistik','Flugfeld'])
            username = faker.user_name()
            password = faker.unique.password()
            data.append({'firstname' : firstname, 'lastname' : lastname, 'birthdate' : birthdate,'sex' : sex, 'street' : street,\
            'city' : city,'zip' : zip_code, 'country' : country, 'emailaddress' : emailaddress,'telephoneno' : telephoneno,\
                'salary' : salary, 'department' : department,'username' : username, 'password' : password})
        except :
            print(f"{len(data)}개의 데이터를 생성 했습니다. 제약조건으로 인해 더이상 생성 할 수 없습니다.")
            return data
    print(f"{len(data)}개의 데이터를 생성 했습니다.")
    return data

def create_flight_log_data(fake_data_num) :
    Faker.seed(random.random())
    faker = Faker()
    data = []
    for _ in range(fake_data_num) :
        try :
            log_date = faker.date()
            user = faker.user_name()
            flight_id = faker.random_int(1,2**31-1)
            flightno_old = faker.unique.bothify(text='??####')
            flightno_new = faker.unique.bothify(text='??####')
            from_old = faker.random_int(1,2**15-1)
            to_old = faker.random_int(1,2**15-1)
            from_new = faker.random_int(1,2**15-1)
            to_new = faker.random_int(1,2**15-1)
            departure_old = faker.date()
            arrival_old = faker.date()
            departure_new = faker.date()
            arrival_new = faker.date()
            airplane_id_old = faker.random_int(1,2**31-1)
            airplane_id_new = faker.random_int(1,2**31-1)
            airline_id_old = faker.random_int(1,2**15-1)
            airline_id_new = faker.random_int(1,2**15-1)
            comment =  faker.texts(nb_texts=1)[0]
            data.append({'log_date' : log_date, 'user' : user, 'flight_id' : flight_id,'flightno_old' : flightno_old, 'flightno_new' : flightno_new,\
                'from_old' : from_old,'to_old' : to_old, 'from_new' : from_new, 'to_new' : to_new,'departure_old' : departure_old,\
                    'arrival_old' : arrival_old, 'departure_new' : departure_new,'arrival_new' : arrival_new, 'airplane_id_old' : airplane_id_old,\
                        'airplane_id_new' : airplane_id_new, 'airline_id_old' : airline_id_old,'airline_id_new' : airline_id_new, 'comment' : comment})
        except :
            print(f"{len(data)}개의 데이터를 생성 했습니다. 제약조건으로 인해 더이상 생성 할 수 없습니다.")
            return data
    print(f"{len(data)}개의 데이터를 생성 했습니다.")
    return data

def create_flight_data(fake_data_num) :
    Faker.seed(random.random())
    faker = Faker()
    data = []
    for _ in range(fake_data_num) :
        try :
            flight_id = faker.random_int(1,2**31-1)
            flightno = faker.unique.bothify(text='??####')
            flight_from = faker.random_int(1,2**15-1)
            flight_to = faker.random_int(1,2**15-1)
            departure = faker.date()
            arrival = faker.date()
            airline_id = faker.random_int(1,2**15-1)
            airplane_id = faker.random_int(1,2**31-1)

            data.append({'flight_id' : flight_id, 'flightno' : flightno, 'from' : flight_from,'to' : flight_to, 'departure' : departure,\
                'arrival' : arrival,'airline_id' : airline_id, 'airplane_id' : airplane_id})
        except :
            print(f"{len(data)}개의 데이터를 생성 했습니다. 제약조건으로 인해 더이상 생성 할 수 없습니다.")
            return data
    print(f"{len(data)}개의 데이터를 생성 했습니다.")
    return data

def create_flightschedule_data(fake_data_num) :
    Faker.seed(random.random())
    faker = Faker()
    data = []
    for _ in range(fake_data_num) :
        try :
            flightno = faker.unique.bothify(text='??####')
            flight_from = faker.random_int(1,2**15-1)
            flight_to = faker.random_int(1,2**15-1)
            departure = faker.time()
            arrival = faker.time()
            airline_id = faker.random_int(1,2**15-1)
            ## 요일 선택해서 해당 요일만 1 나머지는 안넣음 -> 0이 디폴트로 들어감
            dow = [0 for _ in range(7)]
            dow[faker.random_int(0,6)] = 1
            data.append({'flightno' : flightno, 'from' : flight_from, 'to' : flight_to,'departure' : departure, 'arrival' : arrival,\
                'airline_id' : airline_id,'monday' : dow[0],'tuesday' : dow[1],'wednesday' : dow[2],'thursday' : dow[3],\
                    'friday' : dow[4],'saturday' : dow[5],'sunday' : dow[6]})
        except :
            print(f"{len(data)}개의 데이터를 생성 했습니다. 제약조건으로 인해 더이상 생성 할 수 없습니다.")
            return data
    print(f"{len(data)}개의 데이터를 생성 했습니다.")
    return data

def create_passenger_data(fake_data_num) :
    Faker.seed(random.random())
    faker = Faker()
    faker.add_provider(AirTravelProvider)
    data = []
    for _ in range(fake_data_num) :
        try :
            passenger_id = faker.random_int(1,2**31-1)
            passportno = faker.unique.passport_number()
            firstname = faker.first_name()
            lastname = faker.last_name()
            data.append({'passenger_id' : passenger_id, 'passportno' : passportno, 'firstname' : firstname, 'lastname' : lastname})
        except :
            print(f"{len(data)}개의 데이터를 생성 했습니다. 제약조건으로 인해 더이상 생성 할 수 없습니다.")
            return data
    print(f"{len(data)}개의 데이터를 생성 했습니다.")
    return data

def create_weatherdata_data(fake_data_num) :
    Faker.seed(random.random())
    faker = Faker()
    data = []
    for _ in range(fake_data_num) :
        try :
            log_date = faker.date()
            time = faker.time()
            station = faker.random_int(1,2**31-1)
            temp = faker.pydecimal(min_value=0.1, max_value=99.9, right_digits=1)
            humidity  = faker.pydecimal(min_value=0.1, max_value=999.9, right_digits=1)
            airpressure = faker.pydecimal(min_value=0.01, max_value=99999999.99, right_digits=2)
            wind = faker.pydecimal(min_value=0.1, max_value=999.9, right_digits=2)
            weather = random.choice(['Nebel-Schneefall','Schneefall','Regen','Regen-Schneefall','Nebel-Regen','Nebel-Regen-Gewitter','Gewitter','Nebel','Regen-Gewitter'])
            winddirection = faker.random_int(1,2**15-1)
            data.append({'log_date' : log_date, 'time' : time, 'station' : station, 'temp' : temp, 'humidity' : humidity,\
                'airpressure' : airpressure, 'wind' : wind, 'weather' : weather, 'winddirection' : winddirection})
        except :
            print(f"{len(data)}개의 데이터를 생성 했습니다. 제약조건으로 인해 더이상 생성 할 수 없습니다.")
            return data
    print(f"{len(data)}개의 데이터를 생성 했습니다.")
    return data

def create_passengerdetails_data(fake_data_num) :
    Faker.seed(random.random())
    faker = Faker()
    data = []
    for _ in range(fake_data_num) :
        try :
            passenger_id = faker.random_int(1,2**31-1)
            birthdate = faker.date()
            sex = faker.bothify(text='?', letters='MF')
            street = faker.street_name()
            city = faker.city()
            zip_code = faker.random_int(1, 2**15-1)
            country = faker.country()
            emailaddress = faker.email()
            telephoneno = faker.phone_number()
            data.append({'passenger_id' : passenger_id, 'birthdate' : birthdate, 'sex' : sex, 'street' : street, 'street' : street,\
                'city' : city, 'zip' : zip_code, 'country' : country, 'emailaddress' : emailaddress,'telephoneno': telephoneno})
        except :
            print(f"{len(data)}개의 데이터를 생성 했습니다. 제약조건으로 인해 더이상 생성 할 수 없습니다.")
            return data
    print(f"{len(data)}개의 데이터를 생성 했습니다.")
    return data

def create_booking_dummy_data(fake_data_num) :
    Faker.seed(random.random())
    faker = Faker()
    data = []
    for _ in range(fake_data_num) :
        try:
            flight_id = faker.random_int(1,2**31-1)
            seat = faker.bothify(text='??##', letters=''.join(chr(i) for i in range(ord('A'), ord('Z')-1)))
            passenger_id = faker.random_int(1,2**31-1)
            price = faker.pydecimal(min_value=1.00, max_value=99999999.99, right_digits=2)
            data.append({'flight_id' : flight_id, 'seat' : seat, 'passenger_id' : passenger_id,'price':price})
        except :
            print(f"{len(data)}개의 데이터를 생성 했습니다. 제약조건으로 인해 더이상 생성 할 수 없습니다.")
            return data
    print(f"{len(data)}개의 데이터를 생성 했습니다.")
    return data