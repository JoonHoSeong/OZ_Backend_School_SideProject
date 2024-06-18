import json
import os
from sqlalchemy import create_engine #데이터 베이스와 연결하기 위한 라이브러리
from sqlalchemy import MetaData #메타데이터를 받아오기 위한 라이브러리
from sqlalchemy.engine import reflection #데이터 베이스 내의 정보를 가져오기 위한 라이브러리
from faker import Faker #더미데이터만들기 위해 사용
from tools.temp_tool import *

connectData = get_connectData('setting/config.json')
engine, metadata, inspector = connect_DB(connectData)

