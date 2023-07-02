try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter


mainWindow = tkinter.Tk()

mainWindow.title("Aleph Pro")
mainWindow.geometry('640x350-8-200')
mainWindow.configure(background="#282828")
mainWindow['padx'] = 10
icon = tkinter.PhotoImage(file="ProjectMedia/mbc-gold-vk favicon.png")
mainWindow.iconphoto(True, icon)


mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)
mainWindow.columnconfigure(3, weight=1)
mainWindow.columnconfigure(4, weight=1)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.rowconfigure(4, weight=1)

# FIRST HALF

border_firstHalf = tkinter.LabelFrame(mainWindow, bd=5, background="#383838")
border_firstHalf.grid(row=0, column=0, sticky="nw", pady=16)
border_firstHalf['padx'] = 11
border_firstHalf['pady'] = 7

label = tkinter.Label(border_firstHalf, text="Aleph Pro Video Editor",
                      background="#383838", fg='#0277bd')
label.grid(row=0, column=0, sticky="n")

# frame for the radio buttons

optionFrame = tkinter.LabelFrame(border_firstHalf, text="Color Options", background="#383838", fg='#0277bd')
optionFrame.grid(row=1, column=0, sticky='nw', pady=5)
rbValue = tkinter.IntVar()
rbValue.set(1)
# Radio buttons
radio1 = tkinter.Radiobutton(optionFrame, text="Blue Theme", value=1,
                             variable=rbValue, background="#383838",
                             fg='#0277bd')
radio2 = tkinter.Radiobutton(optionFrame, text="Green Theme", value=2,
                             variable=rbValue, background="#383838",
                             fg='#0277bd')
radio3 = tkinter.Radiobutton(optionFrame, text="Red Theme", value=3,
                             variable=rbValue, background="#383838",
                             fg='#0277bd')
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')
optionFrame['padx'] = 11
optionFrame['pady'] = 10

nameFrame = tkinter.LabelFrame(border_firstHalf, text="PowerClip Name",
                               height=40, width=125, background="#383838",
                               fg='#0277bd')
nameFrame.grid(row=2, column=0, sticky="nw", pady=5)
nameFrame['padx'] = 10
nameFrame['pady'] = 5
entry_4_name = tkinter.Entry(nameFrame, width=16, background="#444444")
entry_4_name.grid(row=0, column=0)

# Spacing
spacing_label = tkinter.Label(border_firstHalf, text=' ', font=('Calibri', 46), background="#383838")
spacing_label.grid(row=3, column=0, sticky="n")

# SECOND HALF
# Entry boxes and Frames

border_second_half = tkinter.LabelFrame(mainWindow, bd=5, background="#383838")
border_second_half.grid(row=0, column=1, sticky='n', pady=16)
border_second_half['padx'] = 11
border_second_half['pady'] = 13


TopFrame = tkinter.LabelFrame(border_second_half, text="Sermon Video Filepath",
                              height=50, width=416, background="#383838",
                              fg='#0277bd')
TopFrame.grid(row=0, column=1, columnspan=1, sticky="n", pady=10)
TopFrame['padx'] = 10
TopFrame['pady'] = 5
# Sermon File Input line
entry1 = tkinter.Entry(TopFrame, width=65, background="#444444")
entry1.grid(row=0, column=0)

SecondFrame = tkinter.LabelFrame(border_second_half, text="Sermon Transcript Filepath",
                                 height=50, width=380, background="#383838", fg='#0277bd')
SecondFrame.grid(row=1, column=1, columnspan=1, sticky="w", pady=10)
SecondFrame['padx'] = 10
SecondFrame['pady'] = 5
# Transcript File Input line
entry2 = tkinter.Entry(SecondFrame, width=65, background="#444444")
entry2.grid(row=0, column=0)

ThirdFrame = tkinter.LabelFrame(border_second_half, text="Output Filepath",
                                height=50, width=380, background="#383838",
                                fg='#0277bd')
ThirdFrame.grid(row=2, column=1, columnspan=1, sticky="w", pady=10)
ThirdFrame['padx'] = 10
ThirdFrame['pady'] = 5
# Output Entry box
entry3 = tkinter.Entry(ThirdFrame, width=65, background="#444444")
entry3.grid(row=0, column=0)

FourthFrame = tkinter.LabelFrame(border_second_half, text="Start and Stop Marks (hh:mm:ss)",
                                 height=50, width=380, background="#383838", fg='#0277bd')
FourthFrame.grid(row=3, column=1, columnspan=1, sticky="w", pady=10)
FourthFrame['padx'] = 10
FourthFrame['pady'] = 5
entry4 = tkinter.Entry(FourthFrame, width=20, background="#444444")
entry5 = tkinter.Entry(FourthFrame, width=20, background="#444444")
entry4.grid(row=0, column=0, padx=10)
entry5.grid(row=0, column=1, padx=10)

mainWindow.mainloop()
