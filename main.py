import time
from plyer import notification

def send_notification(title, message):
    notification.notify(title=title,message=message,timeout=3)

if __name__ == "__main__":
    title = "Desktop Notifier"
    message = "This is a test notification."

    send_notification(title, message)