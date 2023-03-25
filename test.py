import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # create the 7 main buttons
        self.button1 = tk.Button(
            self, text="Button 1", command=self.show_screen1, height=5, width=20)
        self.button1.pack(side="left", padx=10, pady=10)

        self.button2 = tk.Button(
            self, text="Button 2", command=self.show_screen2, height=5, width=20)
        self.button2.pack(side="left", padx=10, pady=10)

        self.button3 = tk.Button(
            self, text="Button 3", command=self.show_screen3, height=5, width=20)
        self.button3.pack(side="left", padx=10, pady=10)

        self.button4 = tk.Button(
            self, text="Button 4", command=self.show_screen4, height=5, width=20)
        self.button4.pack(side="left", padx=10, pady=10)

        self.button5 = tk.Button(
            self, text="Button 5", command=self.show_screen5, height=5, width=20)
        self.button5.pack(side="left", padx=10, pady=10)

        self.button6 = tk.Button(
            self, text="Button 6", command=self.show_screen6, height=5, width=20)
        self.button6.pack(side="left", padx=10, pady=10)

        self.button7 = tk.Button(
            self, text="Button 7", command=self.show_screen7, height=5, width=20)
        self.button7.pack(side="left", padx=10, pady=10)

        # create the frames for the sub-screens
        self.screen1 = tk.Frame(self.master)
        self.screen2 = tk.Frame(self.master)
        self.screen3 = tk.Frame(self.master)
        self.screen4 = tk.Frame(self.master)
        self.screen5 = tk.Frame(self.master)
        self.screen6 = tk.Frame(self.master)
        self.screen7 = tk.Frame(self.master)

        # create the buttons for each sub-screen
        self.screen1_button1 = tk.Button(
            self.screen1, text="Screen 1 Button 1", command=self.show_screen1_sub1, height=5, width=20)
        self.screen1_button1.pack(side="left", padx=10, pady=10)

        self.screen1_button2 = tk.Button(
            self.screen1, text="Screen 1 Button 2", command=self.show_screen1_sub2, height=5, width=20)
        self.screen1_button2.pack(side="left", padx=10, pady=10)

        self.screen2_button1 = tk.Button(
            self.screen2, text="Screen 2 Button 1", command=self.show_screen2_sub1, height=5, width=20)
        self.screen2_button1.pack(side="left", padx=10, pady=10)

        self.screen2_button2 = tk.Button(
            self.screen2, text="Screen 2 Button 2", command=self.show_screen2_sub2, height=5, width=20)
        self.screen2_button2.pack(side="left", padx=10, pady=10)

        self.screen3_button1 = tk.Button(
            self.screen3, text="Screen 3 Button 1", command=self.show_screen3_sub1, height=5, width=20)
        self.screen3_button1.pack(side="left", padx=10, pady=10)

        self.screen3_button2 = tk.Button(
            self.screen3, text="Screen 3 Button 2", command=self.show_screen3_sub2, height=5, width=20)
        self.screen3_button2.pack(side="left", padx=10, pady=10)

        self.screen4_button1 = tk.Button(
            self.screen4, text="Screen 4 Button 1", command=self.show_screen4_sub1, height=5, width=20)
        self.screen4_button1.pack(side="left", padx=10, pady=10)

        self.screen4_button2 = tk.Button(
            self.screen4, text="Screen 4 Button 2", command=self.show_screen4_sub2, height=5, width=20)
        self.screen4_button2.pack(side="left", padx=10, pady=10)

        self.screen5_button1 = tk.Button(
            self.screen5, text="Screen 5 Button 1", command=self.show_screen5_sub1, height=5, width=20)
        self.screen5_button1.pack(side="left", padx=10, pady=10)

        self.screen5_button2 = tk.Button(
            self.screen5, text="Screen 5 Button 2", command=self.show_screen5_sub2, height=5, width=20)
        self.screen5_button2.pack(side="left", padx=10, pady=10)

        self.screen6_button1 = tk.Button(
            self.screen6, text="Screen 6 Button 1", command=self.show_screen6_sub1, height=5, width=20)
        self.screen6_button1.pack(side="left", padx=10, pady=10)

        self.screen6_button2 = tk.Button(
            self.screen6, text="Screen 6 Button 2", command=self.show_screen6_sub2, height=5, width=20)
        self.screen6_button2.pack(side="left", padx=10, pady=10)

        self.screen7_button1 = tk.Button(
            self.screen7, text="Screen 7 Button 1", command=self.show_screen7_sub1, height=5, width=20)
        self.screen7_button1.pack(side="left", padx=10, pady=10)

        self.screen7_button2 = tk.Button(
            self.screen7, text="Screen 7 Button 2", command=self.show_screen7_sub2, height=5, width=20)
        self.screen7_button2.pack(side="left", padx=10, pady=10)

        # set the initial visibility of the sub-screens to hidden
        self.screen1.pack_forget()
        self.screen2.pack_forget()
        self.screen3.pack_forget()
        self.screen4.pack_forget()
        self.screen5.pack_forget()
        self.screen6.pack_forget()
        self.screen7.pack_forget()

    def show_screen1(self):
        # hide all other sub-screens
        self.screen2.pack_forget()
        self.screen3.pack_forget()
        self.screen4.pack_forget()
        self.screen5.pack_forget()
        self.screen6.pack_forget()
        self.screen7.pack_forget()

        # show the selected sub-screen
        self.screen1.pack(side="top", fill="both", expand=True)

    def show_screen2(self):
        self.screen1.pack_forget()
        self.screen3.pack_forget()
        self.screen4.pack_forget()
        self.screen5.pack_forget()
        self.screen6.pack_forget()
        self.screen7.pack_forget()

        self.screen2.pack(side="top", fill="both", expand=True)

    def show_screen3(self):
        self.screen1.pack_forget()
        self.screen2.pack_forget()
        self.screen4.pack_forget()
        self.screen5.pack_forget()
        self.screen6.pack_forget()
        self.screen7.pack_forget()

        self.screen3.pack(side="top", fill="both", expand=True)

    def show_screen4(self):
        self.screen1.pack_forget()
        self.screen2.pack_forget()
        self.screen3.pack_forget()
        self.screen5.pack_forget()
        self.screen6.pack_forget()
        self.screen7.pack_forget()

        self.screen4.pack(side="top", fill="both", expand=True)

    def show_screen5(self):
        self.screen1.pack_forget()
        self.screen2.pack_forget()
        self.screen3.pack_forget()
        self.screen4.pack_forget()
        self.screen6.pack_forget()
        self.screen7.pack_forget()

        self.screen5.pack(side="top", fill="both", expand=True)

    def show_screen6(self):
        self.screen1.pack_forget()
        self.screen2.pack_forget()
        self.screen3.pack_forget()
        self.screen4.pack_forget()
        self.screen5.pack_forget()
        self.screen7.pack_forget()

        self.screen6.pack(side="top", fill="both", expand=True)

    def show_screen7(self):
        self.screen1.pack_forget()
        self.screen2.pack_forget()
        self.screen3.pack_forget()
        self.screen4.pack_forget()
        self.screen5.pack_forget()
        self.screen6.pack_forget()

        self.screen7.pack(side="top", fill="both", expand=True)

    def show_screen1_sub1(self):
        self.screen1_button1.pack_forget()
        self.screen1_button2.pack_forget()

        self.screen1_sub1.pack(side="top", fill="both", expand=True)

    def show_screen1_sub2(self):
        self.screen1_button1.pack_forget()
        self.screen1_button2.pack_forget()

        self.screen1_sub2.pack(side="top", fill="both", expand=True)

    def show_screen2_sub1(self):
        self.screen2_button1.pack_forget()
        self.screen2_button2.pack_forget()

        self.screen2_sub1.pack(side="top", fill="both", expand=True)

    def show_screen2_sub2(self):
        self.screen2_button1.pack_forget()
        self.screen2_button2.pack_forget()

        self.screen2_sub2.pack(side="top", fill="both", expand=True)

    def show_screen3_sub1(self):
        self.screen3_button1.pack_forget()
        self.screen3_button2.pack_forget()

        self.screen3_sub1.pack(side="top", fill="both", expand=True)

    def show_screen3_sub2(self):
        self.screen3_button1.pack_forget()
        self.screen3_button2.pack_forget()

        self.screen3_sub2.pack(side="top", fill="both", expand=True)

    def show_screen4_sub1(self):
        self.screen4_button1.pack_forget()
        self.screen4_button2.pack_forget()

        self.screen4_sub1.pack(side="top", fill="both", expand=True)

    def show_screen4_sub2(self):
        self.screen4_button1.pack_forget()
        self.screen4_button2.pack_forget()

        self.screen4_sub2.pack(side="top", fill="both", expand=True)

    def show_screen5_sub1(self):
        self.screen5_button1.pack_forget()
        self.screen5_button2.pack_forget()

        self.screen5_sub1.pack(side="top", fill="both", expand=True)

    def show_screen5_sub2(self):
        self.screen5_button1.pack_forget()
        self.screen5_button2.pack_forget()

        self.screen5_sub2.pack(side="top", fill="both", expand=True)

    def show_screen6_sub1(self):
        self.screen6_button1.pack_forget()
        self.screen6_button2.pack_forget()

        self.screen6_sub1.pack(side="top", fill="both", expand=True)

    def show_screen6_sub2(self):
        self.screen6_button1.pack_forget()
        self.screen6_button2.pack_forget()

        self.screen6_sub2.pack(side="top", fill="both", expand=True)

    def show_screen7_sub1(self):
        self.screen7_button1.pack_forget()

        self.screen7_button2.pack_forget()

        self.screen7_sub1.pack(side="top", fill="both", expand=True)

    def show_screen7_sub2(self):
        self.screen7_button1.pack_forget()
        self.screen7_button2.pack_forget()

        self.screen7_sub2.pack(side="top", fill="both", expand=True)


# create the GUI application
app = Application()

# set the window title
#app.title("Button Application")

# run the main loop
app.mainloop()
