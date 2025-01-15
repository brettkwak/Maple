import pandas as pd

# Fuction to load the data
def load_data(file_path):
    return pd.read_csv(file_path)

# Load all data
level_exp_data = load_data('../data/Level_EXP.csv')
daily_quest_data = load_data('../data/Daily_EXP.csv')
monster_park_data = load_data('../data/Monster_Park.csv')
# Print
print(level_exp_data)
print(daily_quest_data)
print(monster_park_data)

# Input Level, EXP
current_level = int(input("현재 레벨 : "))
current_exp = int(input("현재 경험치 : "))
level_exp = 0

# Function to calculate needed XP to next level
def exp_left(current_level, current_exp):
    df = level_exp_data
    exp = df[df['Level'] == current_level]['EXP'].values[0] - current_exp
    string_exp = f"{exp:,}"
    return string_exp
# Test
exp_left(current_level, current_exp)

# Function to fetch required data from daily_quest_data
def fetch_daily_quest_data(index):
    df = daily_quest_data
    row = df.iloc[index]
    location = row['Name']
    exp = row['EXP']
    return location, exp

# Function to find out daily quest location
def get_daily_quest(level):
    if 200 <= level < 210:
        # 여로
        index = 0
    elif 210 <= level < 220:
        # 츄츄
        index = 1
    elif 220 <= level < 225:
        # 레헬른
        index = 2
    elif 225 <= level < 230:
        # 아르카나
        index = 3
    elif 230 <= level < 235:
        # 모라스
        index = 4
    elif 235 <= level < 240:
        # 에스페라
        index = 5
    elif 240 <= level < 245:
        # 셀라스
        index = 6
    elif 245 <= level < 250:
        # 문브릿지
        index = 7
    elif 250 <= level < 255:
        # 고통의 미궁
        index = 8
    elif 255 <= level < 260:
        # 리멘
        index = 9
    elif 260 <= level < 265:
        # 세르니움
        index = 10
    elif 265 <= level < 270:
        # 호텔 아르크스
        index = 11
    elif 270 <= level < 275:
        # 오디움
        index = 12
    elif 275 <= level < 280:
        # 도원경
        index = 13
    elif 280 <= level < 285:
        # 아르테르아
        index = 14
    elif 285 <= level < 290:
        # 카르시온
        index = 15
    elif 290 <= level < 295:
        # 탈라하트
        index = 16
    return fetch_daily_quest_data(index)

# Function to fetch monster park data
def fetch_monster_park_data(index):
    df = monster_park_data
    row = df.iloc[index]
    location = row['Name']
    exp = row['EXP']
    return location, exp

# Function to find out monster park location
def get_monster_park(level):
    if 200 <= level < 210:
        # 여로
        index = 0
    elif 210 <= level < 220:
        # 츄츄
        index = 1
    elif 220 <= level < 225:
        # 레헬른
        index = 2
    elif 225 <= level < 230:
        # 아르카나
        index = 3
    elif 230 <= level < 235:
        # 모라스
        index = 4
    elif 235 <= level < 240:
        # 에스페라
        index = 5
    elif 240 <= level < 245:
        # 셀라스
        index = 6
    elif 245 <= level < 250:
        # 문브릿지
        index = 7
    elif 250 <= level < 255:
        # 고통의 미궁
        index = 8
    elif 255 <= level < 260:
        # 리멘
        index = 9
    return fetch_monster_park_data(index)

# Function to change int format to string
def int_to_str(number):
    number = f"{number:,}"
    return number

# Function to find out data range
def exp_range(current_level, current_exp):
    print("현재 레벨 : " + str(current_level))
    print("현재 경험치 : " + str(current_exp))
    print("다음 레벨까지 남은 경험치 : " + exp_left(current_level, current_exp))
    daily_quest_location, daily_quest_exp = get_daily_quest(current_level)
    print("일일 퀘스트 지역 : " + daily_quest_location)
    print("일일 퀘스트 경험치 : " + int_to_str(daily_quest_exp))
    monster_park_location, monster_park_exp = get_monster_park(current_level)
    print("몬스터 파크 지역 : " + monster_park_location)
    print("몬스터 파크 경험치 : " + int_to_str(monster_park_exp))
    return None
# Test
exp_range(current_level, current_exp)

# Setting Input
input("일일 퀘스트? (Y/N) : ")
input("주간 퀘스트? (Y/N) : ")
input("몬스터 파크 횟수 : ")

# Result Example
print("계산 전 레벨 / 경험치")
print("Lv. " + str(current_level))
print(str(current_exp) + " / " + str(level_exp))
print("계산 후 레벨 / 경험치")
print("Lv. " + str(current_level))
print(str(current_exp) + " / " + str(level_exp))