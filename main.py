from interface import *
def run():
    i = Interface()
    while True:
        i.display_main_menu()
        truefalse = i.handle_main_menu()
        if not truefalse:
            break

if __name__ == '__main__':
    run()
