from interface import *
def run():
    i = Interface()
    i.load()
    while True:
        i.display_main_menu()
        truefalse = i.handle_main_menu()
        if not truefalse:
            break

if __name__ == '__main__':
    run()
