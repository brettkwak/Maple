

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


# Check for validity
def is_valid_selection(selection, limit):

    # Check if representing skills are unique
    main_skills = [box[0] for _, box in selection]
    if len(set(main_skills)) != len(selection):
        return False

    # Check if any skill appears more than the limit
    skill_count = {}
    for _, box in selection:
        for skill in box:
            skill_count[skill] = skill_count.get(skill, 0) + 1

    # Check if any skill exceeds the limit
    for skill, count in skill_count.items():
        if count > limit:
            return False

    return True


# Backtracking algorithm for finding core combination
def backtrack(cores_list, start_index, current_selection, limit, core_count):

    # Check if selection is valid
    if len(current_selection) == core_count:
        if is_valid_selection(current_selection, limit):
            return [box_id for box_id, _ in current_selection]
        return None

    # Recursive
    for i in range(start_index, len(cores_list)):
        current_selection.append(cores_list[i])
        result = backtrack(cores_list, i + 1, current_selection, limit, core_count)
        if result:
            return result
        current_selection.pop()

    return None


# Find core combinations
def find_core_combination(core_list, limit, core_count):

    if len(core_list) < core_count:
        print(f"Not enough boxes: need {core_count}, found {len(core_list)}")
        return None

    # Convert to list of tuples for backtracking
    core_tuple = list(core_list.items())
    result = backtrack(core_tuple, 0, [], limit, core_count)

    if result:
        print(f"Found valid selection of {core_count} boxes: {result}")
    else:
        print("No valid selection found")

    return result


def main():

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
    print(filtered_cores)
    print_cores(filtered_cores)

    print(target_skills)
    result = find_core_combination(filtered_cores, 3, 6)
    print(result)

    return None


if __name__ == "__main__":
    main()