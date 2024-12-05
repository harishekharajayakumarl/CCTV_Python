import cv2
import time
import os

def minimizeWindow():
    import win32gui, win32con
    window = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(window, win32con.SW_MINIMIZE)

def cctv():
    video = cv2.VideoCapture(0)
    video.set(3, 640)
    video.set(4, 480)
    width = video.get(3)
    height = video.get(4)
    print(f"Video resolution is set to {width} x {height}")
    print("Help-- \n1. Press esc to exit \n2. Press m to minimize")
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    date_time = time.strftime("recording_%H-%M-%d-%m-%y")
    output = cv2.VideoWriter(os.path.join('footages', date_time + '.mp4'), fourcc, 20.0, (640, 480))
    while video.isOpened():
        check, frame = video.read()
        if check:
            frame = cv2.flip(frame, 1)
            t = time.ctime()
            cv2.rectangle(frame, (5, 5), (100, 20), (255, 255, 255), cv2.FILLED)
            cv2.putText(frame, "Camera1", (10, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
            cv2.putText(frame, t, (420, 460), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
            cv2.imshow('CCTV Camera', frame)
            output.write(frame)
            key = cv2.waitKey(1)
            if key == 27:  # ESC key to exit
                print("Video footage saved in 'footages' directory")
                break
            elif key == ord('m'):  # 'm' key to minimize window
                minimizeWindow()
    video.release()
    output.release()
    cv2.destroyAllWindows()

print("*" * 80 + "\n" + " " * 30 + "Welcome to CCTV Software\n" + "*" * 80)
ask = int(input("Do you wish to open CCTV?\n 1. yes \n 2. no "))
if ask == 1:
    cctv()
else:
    print("Ok Bye")
