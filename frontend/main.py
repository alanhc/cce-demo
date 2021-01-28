from tkinter import *
from PIL import ImageTk, Image
import cv2
import requests
import io
root = Tk()

panel = Label(root)
panel.pack(side=LEFT)

def btn_press():
    print("hello")
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    print(cv2image.shape)
    url = "http://120.125.83.237:8080/api/predict"
    buf = io.BytesIO()
    is_success, im_buf_arr = cv2.imencode(".png", cv2image)
    byte_im = im_buf_arr.tobytes()

    files = {'file': byte_im}
    re = requests.post(url, files=files)
    w,h = re.headers['w'], re.headers['h']
    print(w,h)
    image = Image.frombytes('RGB', (int(w),int(h)), re.content)
    image.save("test.png")
    print(re.status_code)
    image = ImageTk.PhotoImage(image)
    panel.configure(image=image)
    panel.image = image
    

    

    
button = Button(root, text="style", command=btn_press)
button.pack()
# Create a frame
app = Frame(root, bg="white")
app.pack()
# Create a label in the frame
lmain = Label(app)
lmain.pack(side=LEFT)

# Capture from camera
cap = cv2.VideoCapture(0)

# function for video streaming
def video_stream():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream) 

video_stream()

root.mainloop()