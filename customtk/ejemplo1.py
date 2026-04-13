import customtkinter

def button_callback():
    print("button preessed")

app=customtkinter.Ctk()
app.title("Mi App")
app.geometry("400x150")

button = customtkainter.CTkButton(app , text="ay button",command=button_callback)
button.grid(row=0 , column=0, padx=20,pady=20)

app.mainloop()