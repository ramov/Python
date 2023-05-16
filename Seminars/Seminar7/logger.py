    
def log_all(text):
    with open('log.txt', 'a', encoding="utf-8") as data:
        data.write(text + '\n')

def log_out():
    with open('log.txt', 'r', encoding="utf-8") as data:
        print(*data.readlines())
