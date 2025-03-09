

# Load core information from .txt file
def load_core_information_from_file(file_path):

    cores = {}

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(', ')
            if len(parts) >= 4 and parts[0].startswith('Core '):
                core_num = int(parts[0].split(' ')[1])
                skills = parts[1:4]
                cores[core_num] = skills


    print(f"Loaded {len(cores)} cores from {file_path}")
    return cores


file_path = f'../data/core_skill_mapping.txt'

load_core_information_from_file(file_path)