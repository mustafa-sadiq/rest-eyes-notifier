import time
from win10toast import ToastNotifier
toast = ToastNotifier()

every_x_minutes = 20

while(True):
    toast.show_toast("Rest-Eyes-Notifier", "Look away! Give your eyes some rest for at least 20 seconds.", duration=20)
    time.sleep(every_x_minutes*60)