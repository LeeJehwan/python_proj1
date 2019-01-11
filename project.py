import sys
import os


def show(data):
    for x in data:
        print(x.split())


def get_avg(l):
    sum_data = int(l[2]) + int(l[3])
    l.append(sum_data/2)



def data_processing(data):
    new_data = list()
    for x in data:
        tmplist = x.split()
        tmplist[1] += " " + tmplist[2]
        tmplist.remove(tmplist[2])
        new_data.append(tmplist)

    for x in new_data:
        get_avg(x)

    for x in new_data:
        print(x)






def search():
    print("search")


def change_score():
    print("change score")


def search_grade():
    print("search grade")


def add_data():
    print("add data")


def remove_data():
    print("remove data")


def quit_program():
    print("quit")


def input_command():
    comm = input("# ")
    return comm.lower()


def read_file():
    args = sys.argv[1:]
    file_name = "students.txt"
    if len(args) == 1:
        file_name = args[0]
    elif len(args) == 0:
        pass
    else:
        print("error: too many argument")
        print("Usage: ")
        print("python project.py [filename.txt]")
        return -1

    if not os.path.exists(file_name):
        print("No", file_name, "file")
        return -1

    with open(file_name, "r") as f:
        return f.readlines()


def write_file():
    print("file write")


def main():
    data = read_file()
    if data == -1:
        return
    data_processing(data)
    #show(data)
    while True:
        comm = input_command()
        if comm == "show":
            show(data)
        elif comm == "search":
            search()
        elif comm == "changescore":
            change_score()
        elif comm == "searchgrade":
            search_grade()
        elif comm == "add":
            add_data()
        elif comm == "remove":
            remove_data()
        elif comm == "quit":
            break
        else:
            continue

    quit_program()


if __name__ == '__main__':
    main()

