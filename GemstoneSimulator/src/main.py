import core_extract


def process_image(image_path, setting):

    return None


def main():

    class_name = input("직업 이름 : ")
    limit = int(input("몇 중 : "))
    core_count = int(input("몇 코 : "))
    image_count = int(input("이미지 개수 : "))
    images = ""

    target_skills = []
    print("유효 스킬 이름 : ")
    while True:
        skill = input()
        if not skill:
            break
        target_skills.append(skill)

    total_matches = core_extract.main(image_count)
    print(f"Total Matches : {total_matches}")


    return None


if __name__ == "__main__":
    main()
