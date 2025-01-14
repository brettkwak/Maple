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

def exp_left(current_level, current_exp):
    df = level_exp_data
    exp = df[df['Level'] == current_level + 1]['EXP'].values[0] - current_exp
    string_exp = f"{exp:,}"
    return string_exp
# Test
exp_left(current_level, current_exp)

# Function to find out data range
def exp_range(current_level, current_exp):
    print("현재 레벨 : " + str(current_level))
    print("현재 경험치 : " + str(current_exp))
    print("다음 레벨까지 남은 경험치 : " + exp_left(current_level, current_exp))
    print("일일 퀘스트 지역 : ")
    print("일일 퀘스트 경험치 : ")
    print("몬스터 파크 지역 : ")
    print("몬스터 파크 경험치 : ")
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