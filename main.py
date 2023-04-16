import tkinter

number, message = 0, 0

def last_message():
    global number, message

    popup = tkinter.Toplevel()
    popup.title("!")
    popup.geometry("200x50+{}+{}".format(window.winfo_rootx() + window.winfo_width() // 2 - 110,
                                         window.winfo_rooty() + window.winfo_height() // 2 - 50))
    popup.iconbitmap('icon.ico')
    popup.resizable(False, False)

    if message == 1:
        text = tkinter.Label(popup, text=f"You are thinking of {number}.")
        text.pack()
        popup.after(3000, popup.destroy)
    else:
        text = tkinter.Label(popup, text=f"You are not thinking of a number.")
        text.pack()
        popup.after(3000, popup.destroy)

def thinking_message():
    popup = tkinter.Toplevel()
    popup.title("...")
    popup.geometry("200x50+{}+{}".format(window.winfo_rootx() + window.winfo_width() // 2 - 110,
                                         window.winfo_rooty() + window.winfo_height() // 2 - 50))
    popup.iconbitmap('icon.ico')
    popup.resizable(False, False)

    text = tkinter.Label(popup, text="Thinking...")
    text.pack()

    popup.after(3000, popup.destroy)
    window.after(3100, last_message)

def guess_number(event):
    global number, message
    try:
        number = input.get()
        number = int(number.replace(",", "").replace(" ", ""))
        message = 1
        thinking_message()

    except ValueError:
        message = 0
        thinking_message()

window = tkinter.Tk()
window.title("I can guess any number.")
window.geometry("400x70+{}+{}".format((window.winfo_screenwidth() // 2) - (400 // 2),
                                      (window.winfo_screenheight() // 2) - (70 // 2)))
window.iconbitmap('icon.ico')
window.resizable(False, False)

description = tkinter.Label(window, text="Think of any number, input it and I will be able to guess it.")
input = tkinter.Entry(window, justify="center")
input.bind("<Return>", guess_number)

description.pack()
input.pack()

window.mainloop()
