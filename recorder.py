from tkinter import *
from tkinter import messagebox
import pyscreenrec  # Screen Recorder Library


root = Tk()
root.geometry("400x500")
root.title("Screen Recorder")
root.resizable(False, False)


bg_image = PhotoImage(file="bg.png") 
bg_label = Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Initialize Screen Recorder
rec = pyscreenrec.ScreenRecorder()

# Functions
def start_rec():
    file = Filename.get()
    if not file.strip():
        messagebox.showerror("Error", "Filename cannot be empty!")
        return
    rec.start_recording(f"{file}.mp4", 5)

def pause_rec():
    rec.pause_recording()

def resume_rec():
    rec.resume_recording()

def stop_rec():
    rec.stop_recording()

# App Icon
image_icon = PhotoImage(file="icon.png")  # Ensure you have a file named 'icon.png'
root.iconphoto(False, image_icon)

# Header
heading = Label(root, text="Screen Recorder", bg="#000", fg="#fff", font=("Arial", 20, "bold"))
heading.pack(pady=20)

# Entry Box for Filename
Filename = StringVar()
entry = Entry(root, textvariable=Filename, width=20, font=("Arial", 15), bd=2, relief=GROOVE, justify="center")
entry.place(x=100, y=150)
Filename.set("recording")

# Buttons
start_btn = Button(root, text="Start", font=("Arial", 15, "bold"), fg="#fff", bg="#28a745", width=10, command=start_rec)
start_btn.place(x=140, y=200)

image_pause = PhotoImage(file="pause.png")
pause_btn = Button(root, image=image_pause, bd=0, bg="#fff", command=pause_rec)
pause_btn.place(x=70, y=300)

image_resume = PhotoImage(file="start.png")
resume_btn = Button(root, image=image_resume, bd=0, bg="#fff", command=resume_rec)
resume_btn.place(x=160, y=300)

image_stop = PhotoImage(file="stop.png")
stop_btn = Button(root, image=image_stop, bd=0, bg="#fff", command=stop_rec)
stop_btn.place(x=250, y=300)



# Run Tkinter Main Loop
root.mainloop()
