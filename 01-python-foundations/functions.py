# Functions - group instructions into a reusable, named unit of work.

def add_numbers(num1, num2):
    return num1 + num2


def take_backup(day):
    if day == "Monday":
        print("Backup script started ...")
    else:
        print(f"No scheduled backup on {day}.")


if __name__ == "__main__":
    total = add_numbers(20, 22)
    print("Sum:", total)

    for day in ["Monday", "Tuesday"]:
        take_backup(day)
