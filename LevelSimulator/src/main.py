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
current_level = input("현재 레벨 : ")
current_exp = input("현재 경험치 : ")
level_exp = 0

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