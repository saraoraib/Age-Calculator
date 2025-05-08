from datetime import datetime


def calculate_age(birth_date_str: str, reference_date: datetime) -> int:
    try:
        birth_date = datetime.strptime(birth_date_str, "%d-%m-%Y")
    except ValueError:
        raise ValueError("Invalid date format")

    if birth_date.year < 1 or not (1 <= birth_date.month <= 12) or not (1 <= birth_date.day <= 31):
        raise ValueError("Invalid date values")

    age = reference_date.year - birth_date.year - (
                (reference_date.month, reference_date.day) < (birth_date.month, birth_date.day))
    return age


def get_birth_day(birth_date_str: str) -> str:
    birth_date = datetime.strptime(birth_date_str, "%d-%m-%Y")
    return birth_date.strftime('%A')


def process_person_info(person_input: str) -> tuple:
    try:
        name, birth_date_str = person_input.split(", ")
        age = calculate_age(birth_date_str, datetime(2021, 1, 1))
        birth_day = get_birth_day(birth_date_str)
        return name, age, birth_day
    except ValueError as e:
        return None, None, str(e)


def main():
    people = []

    print("Enter names and birthdates (dd-mm-yyyy). Type 'done' to finish.")

    while True:
        user_input = input("Enter name and birthdate: ")

        if user_input.lower() == 'done':
            break

        name, age, result = process_person_info(user_input)

        if name is None:
            print(f"Error: {result}")
        else:
            people.append((name, age, result))

    if len(people) == 1:
        print("There is no oldest or youngest person.")
    else:
        oldest_person = max(people, key=lambda person: person[1])
        youngest_person = min(people, key=lambda person: person[1])

        for name, age, birth_day in people:
            print(f"{name} is {age} years old and was born on {birth_day}")

        print(f"The oldest one is {oldest_person[0]}")
        print(f"The youngest one is {youngest_person[0]}")

    print(f"Total People: {len(people)}")

    people_sorted = sorted(people, key=lambda person: person[1], reverse=True)
    print("\nPeople sorted by age from oldest to youngest:")
    for name, _, _ in people_sorted:
        print(name)

    print("\nPeople in reverse order of input:")
    for name, _, _ in reversed(people):
        print(name)

    print("\nPeople born on Sunday:")
    for name, _, birth_day in people:
        if birth_day == 'Sunday':
            print(name)


if __name__ == "__main__":
    main()