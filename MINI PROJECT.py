import tkinter as tk
window=tk.Tk()
window.title("String Reversal")
window.geometry("600x400")
window.configure(bg="pink")
font1=("curlz mt",15,"bold")
font2=("algerian",25,"bold")
font3=("Chiller",25,"normal")
label1=tk.Label(text="String Reversal",font=font2,
                foreground="black",background="violet red")
label1.pack()
def word():
    result=e.get()[-1::-1]
    label2=tk.Label(text=result,font=font3,
                    foreground="purple",background="pink").pack()
def string():
    result=e.get().split()
    str1=''
    for i in result:
        str1=str1+' '+i[-1::-1]
    label2=tk.Label(text=str1,font=font3,
                    foreground="purple",background="pink").pack()
def sentence():
    result=e.get().split()
    str1=''
    for i in range(-1,-len(result)-1,-1):
        str1+=result[i]+' '
    label2=tk.Label(text=str1,font=font3,
                    foreground="purple",background="pink").pack()
def entry1():
    global e
    label=tk.Label(text="Enter Word:",font=font1,bg="#00ffff").pack()
    e=tk.Entry(window,fg="black",bg="pink",width=60)
    e.pack()
    button=tk.Button(text="Submit",font=font1,
                 bg="Violet",fg="black",relief="raised",command=word)
    button.pack()
def entry2():
    global e
    label=tk.Label(text="Enter Sentence:",font=font1,bg="#00ffff").pack()
    e=tk.Entry(window,fg="black",bg="pink",width=60)
    e.pack()
    button=tk.Button(text="Submit",font=font1,
                 bg="Violet",fg="black",relief="raised",command=string)
    button.pack()
def entry3():
    global e
    label=tk.Label(text="Enter Sentence:",font=font1,bg="#00ffff").pack()
    e=tk.Entry(window,fg="black",bg="pink",width=60)
    e.pack()
    button=tk.Button(text="Submit",font=font1,
                 bg="Violet",fg="black",relief="raised",command=sentence)
    button.pack()
button1=tk.Button(text="Reverse letters of a Word",font=font1,borderwidth=5,
                 bg="Violet",fg="black",relief="raised",command=entry1)
button1.pack()
button2=tk.Button(text="Reverse words of a Sentence",font=font1,borderwidth=5,
                 bg="Violet",fg="black",relief="raised",command=entry2)
button2.pack()
button3=tk.Button(text="Reverse letters of a Sentence",font=font1,borderwidth=5,
                 bg="Violet",fg="black",relief="raised",command=entry3)
button3.pack()


