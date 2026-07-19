import threading

def display():
    print("Hello from thread!")

t = threading.Thread(target=display)

t.start()
t.join()
