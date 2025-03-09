

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


# Print loaded cores
def print_cores(loaded_cores):
    print("\n=== CORES ===")
    count = 0
    for core_num, skills in sorted(loaded_cores.items()):
        print(f"Core {core_num}: {', '.join(skills)}")
        count += 1
    print("=====================\n")


# Filter cores using skill input
def filter_cores_with_skills(cores, target_skills):

    filtered_cores = {}

    for core_num, skills in cores.items():
        if all(skill in target_skills for skill in skills):
            filtered_cores[core_num] = skills

    print(f"Found {len(filtered_cores)} cores containing only the specified skills")

    return filtered_cores


file_path = f'../data/core_skill_mapping.txt'

cores = load_core_information_from_file(file_path)

# Input skill names to filter cores
target_skills = []
print("Enter skill names : ")
while True:
    skill = input()
    if not skill:
        break
    target_skills.append(skill)

filtered_cores = filter_cores_with_skills(cores, target_skills)

print_cores(filtered_cores)