import threading

print(threading.currentThread().getName())

if threading.current_thread() == threading.main_thread(): 
    print("Current thread is the main thread")
else:
    print("The current thread is not the main thread")