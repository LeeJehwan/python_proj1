import sys
import os
import readline


class AutoComplete:
    def __init__(self, commands):
        self.commands = commands

    def complete(self, text, state):
        for cmd in self.commands:
            if cmd.startswith(text.lower()):
                if not state:
                    return cmd
                else:
                    state -= 1


def auto_command_complete(commands):
    auto = AutoComplete(commands)
    readline.set_completer(auto.complete)


def show_table():
    print("{0:^12}".format("Student"), end="")
    print("{0:>14}".format("Name"), end="")
    print("{0:^14}".format("Midterm"), end="")
    print("{0:^10}".format("Final"), end="")
    print("{0:^11}".format("Average"), end="")
    print("{0:^11}".format("Grade"))
    print('-' * 70)


def show_label(x):
    print("{0:^12}".format(x[0]), end="")
    print("{0:>14}".format(x[1]), end="")
    print("{0:^14}".format(x[2]), end="")
    print("{0:^10}".format(x[3]), end="")
    print("{0:^11.1f}".format(x[4]), end="")
    print("{0:^11}".format(x[5]))


def show(data):
    show_table()
    for x in data:
        show_label(x)
    print()
    print()


def search(data):
    commands = []
    for x in data:
        commands.append(x[0])
    auto_command_complete(commands)

    std_id = input("Student ID: ")
    for x in data:
        if std_id == x[0]:
            show_table()
            show_label(x)
            print()
            print()
            return
    print("NO SUCH PERSON.")
    print()


def change_score(data):
    commands = []
    for x in data:
        commands.append(x[0])
    auto_command_complete(commands)
    std_id = input("Student ID: ")
    auto_command_complete([])
    for x in data:
        if std_id == x[0]:
            test_name = input("Mid/Final? ")
            if test_name == 'mid':
                point = int(input("Input new score: "))
                if 0 <= point <= 100:
                    show_table()
                    show_label(x)
                    x[2] = str(point)
                    x[4] = get_avg(x)
                    x[5] = get_grade(x)
                    print("Score changed.")
                    show_label(x)
                    print()

            elif test_name == 'final':
                point = int(input("Input new score: "))
                if 0 <= point <= 100:
                    show_table()
                    show_label(x)
                    x[3] = str(point)
                    x[4] = get_avg(x)
                    x[5] = get_grade(x)
                    print("Score changed.")
                    show_label(x)
                    print()

            data_sort(data)
            print()
            return
    print("NO SUCH PERSON.")
    print()


def search_grade(data):
    grade_list = ['A', 'B', 'C', 'D', 'F']
    auto_command_complete(grade_list)
    grade = input("Grade to search: ")
    auto_command_complete([])

    if grade not in grade_list:
        print()
        return

    is_grade = False
    for x in data:
        if grade == x[5]:
            is_grade = True

    if is_grade is True:
        show_table()
        for x in data:
            if grade == x[5]:
                show_label(x)
        print()
    else:
        print("NO RESULTS.")
    print()


def add_data(data):
    std_id = input("Student ID: ")
    for x in data:
        if std_id == x[0]:
            print("ALREADY EXISTS.")
            print()
            return

    new_std = list()
    new_std.append(std_id)
    new_std.append(input("Name: "))
    new_std.append(input("Midterm Score: "))
    new_std.append(input("Final Score: "))
    new_std.append(get_avg(new_std))
    new_std.append(get_grade(new_std))
    data.append(new_std)
    data_sort(data)
    print("Student added.")
    print()


def remove_data(data):
    if len(data) == 0:
        print("List is empty.")
        print()
        return

    commands = []
    for x in data:
        commands.append(x[0])
    auto_command_complete(commands)
    std_id = input("Student ID: ")
    for x in data:
        if std_id == x[0]:
            data.remove(x)
            print("Student removed.")
            print()
            return
    print("NO SUCH PERSON.")
    print()


def quit_program(data):
    save = input("Save data?[yes/no] ")
    if save == "yes":
        write_file(data)


def input_command():
    commands = ["show", "search", "changescore", "searchgrade", "add", "remove", "quit"]
    auto_command_complete(commands)
    comm = input("# ")
    auto_command_complete([])
    return comm.lower()


def read_file():
    args = sys.argv[1:]
    filename = "students.txt"
    if len(args) == 1:
        filename = args[0]
    elif len(args) == 0:
        pass
    else:
        print("error: too many argument")
        print("Usage: ")
        print("python project.py [filename.txt]")
        return -1

    if not os.path.exists(filename):
        print("No", filename, "file")
        return -1

    with open(filename, "r") as f:
        return f.readlines()


def write_file(data):
    filename = input("File name: ")
    with open(filename, "w") as f:
        for x in data:
            stu = str(x[0]) + '\t' + x[1] + '\t' + str(x[2]) + '\t' + str(x[3]) + '\n'
            f.write(stu)


def get_avg(l):
    sum_data = int(l[2]) + int(l[3])
    return sum_data/2


def get_grade(l):
    std_avg = l[4]
    if std_avg >= 90:
        grade = "A"
    elif std_avg >= 80:
        grade = "B"
    elif std_avg >= 70:
        grade = "C"
    elif std_avg >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade


def data_processing(data):
    new_data = list()
    for x in data:
        tmplist = x.split()
        tmplist[1] += " " + tmplist[2]
        tmplist.remove(tmplist[2])
        new_data.append(tmplist)

    for x in new_data:
        x.append(get_avg(x))
        x.append(get_grade(x))
    data_sort(new_data)
    return new_data


def data_sort(data):
    data.sort(key=lambda e: e[4], reverse=True)


def main():
    readline.parse_and_bind('tab: complete')
    data = read_file()
    if data == -1:
        return
    data = data_processing(data)
    show(data)
    while True:
        comm = input_command()
        if comm == "show":
            show(data)
        elif comm == "search":
            search(data)
            auto_command_complete([])
        elif comm == "changescore":
            change_score(data)
        elif comm == "searchgrade":
            search_grade(data)
        elif comm == "add":
            add_data(data)
        elif comm == "remove":
            remove_data(data)
            auto_command_complete([])
        elif comm == "quit":
            break
        else:
            continue

    quit_program(data)


if __name__ == '__main__':
    main()


