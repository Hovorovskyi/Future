rules = ('''Hello, it`s your TODO list.
        if you want append new task - enter 'new'
        if you want to see your tasks - enter 'check'
        if you want mark the task as complete - enter task name and +''')


def read_file():
    f = open('todolist.txt', 'r')
    for i in f:
        print(i)
    return f.close()


def append_file(todo):
    f = open('todolist.txt', 'w')
    f.seek(0)
    f.write(f'{todo}')
    f.close()
    return rules


def new_task():
    todo = {}
    task = input('Enter new task: ')
    todo[task] = 'working'
    if task == 'q':
        return rules
    return append_file(todo)


def my_tasks():
    return read_file()


def finish():
    task_end = input('Enter task and + (without "space"): ')
    for k in todo:
        if task_end[:-1] == k and task_end[-1] == '+':
            todo[k] = 'finish'
        return todo


def start():
    do = ['new', 'check', '+', 'q']
    time = True
    print(rules)
    while time:
        for i in do:
            enter = input('Enter what you want to do: ')
            if enter == do[0]:
                todo = new_task()
                print(todo)
            elif enter == do[1]:
                check = my_tasks()
                print(check)
            elif enter[-1] == do[2]:
                end_task = finish()
                print(end_task)
            elif enter == do[3]:
                print('Finish')
                time = False
            else:
                print(rules)


if __name__ == '__main__':
    print(start())
