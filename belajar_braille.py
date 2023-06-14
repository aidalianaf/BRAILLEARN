import tkinter as tk
import customtkinter

"""
Nama    : Aida Liana Febiansyah
NIM     : 1202223078
Kelas   : SI-46-02
"""

# Daftar kode Braille
braille_codes = {
    'A': '⠁', 'B': '⠃', 'C': '⠉', 'D': '⠙', 'E': '⠑',
    'F': '⠋', 'G': '⠛', 'H': '⠓', 'I': '⠊', 'J': '⠚',
    'K': '⠅', 'L': '⠇', 'M': '⠍', 'N': '⠝', 'O': '⠕',
    'P': '⠏', 'Q': '⠟', 'R': '⠗', 'S': '⠎', 'T': '⠞',
    'U': '⠥', 'V': '⠧', 'W': '⠺', 'X': '⠭', 'Y': '⠽',
    'Z': '⠵'
}

# Membuat GUI
root = tk.Tk()
root.title('BRAILLEARN')
root.geometry('350x450+500+100')
root.configure(bg='#F4F4F4')

def clear():
    for widget in root.winfo_children():
        widget.destroy()

# Fungsi untuk Translate dari Braille Code
def translate_frame():
    clear()
    def translation():
        text = insert_entry.get()

        for widget in translate_frame.winfo_children():
            widget.destroy()

        label_insert = customtkinter.CTkLabel(translate_frame, text=f"Insert text : {text}", font=('inter', 18), fg_color='transparent', text_color='black')
        label_insert.grid(row=0, column=0, sticky='w', padx=(20, 10))

        translation = ''
        for letter in text.upper():
            if letter == ' ':
                continue
            else:
                translation += braille_codes[letter]

        label_translation = customtkinter.CTkLabel(translate_frame, text=translation, font=('inter', 90), fg_color='transparent', text_color='black')
        label_translation.grid(row=1, column=0, pady=(60, 0), padx=(18,0))

        done_button = customtkinter.CTkButton(translate_frame, text='Done', border_color='black', border_width=1, fg_color='#F46D59', text_color='black', corner_radius=0, width=200, height=40, command=home)
        done_button.grid(row=2, column=0, pady=(50, 0), padx=(18,0))


    # Translate label 
    translate_label = customtkinter.CTkLabel(root, text='Translate to Braille', font=('inter', 18), fg_color='transparent', text_color='black')
    translate_label.pack(pady=(30, 10))

    # Translate Input Frame
    translate_frame = customtkinter.CTkScrollableFrame(root, width=300, height=300, fg_color='#5B9DFF', border_color='black', border_width=1, corner_radius=0, orientation='horizontal')
    translate_frame.pack()

    # widgets for translate input frame
    insert_label = customtkinter.CTkLabel(translate_frame, text='Insert text : ', font=('inter', 18), fg_color='transparent', text_color='black')
    insert_label.pack(pady=(60,0), padx=50)

    insert_entry = customtkinter.CTkEntry(translate_frame, corner_radius=0, fg_color='white', text_color='black', font=('inter', 22), width=200, height=40, border_color='black', border_width=1)
    insert_entry.pack(pady=(10, 0), padx=50)

    insert_button = customtkinter.CTkButton(translate_frame, text='Translate', border_color='black', border_width=1, fg_color='#F46D59', text_color='black', corner_radius=0, width=200, height=40, command=translation)
    insert_button.pack(pady=10, padx=50)

def incorrect_page():
    for x in ex_frame.winfo_children():
        x.destroy()

    answer_list = copy
    for i, x in enumerate(answer_list):
        if x == '#5B9DFF':
            answer_list[i] = 'black'

    correct_label = customtkinter.CTkLabel(ex_frame, text='Incorrect :(', font=('inter', 40, 'bold'), fg_color='transparent', text_color='white')
    correct_label.place(x=50, y=10)

    alphabet_label = customtkinter.CTkLabel(ex_frame, text=alphabet_code[indeks], font=('inter', 30, 'bold'), fg_color='transparent', text_color='black' )
    alphabet_label.place(x=135, y=70)

    # generating braille round button
    top_left = customtkinter.CTkButton(ex_frame, text='', fg_color=answer_list[0], border_color='black', border_width=2, corner_radius=30, width=30, height=30, hover_color=answer_list[0])
    top_left.place(x=110, y=120)

    middle_left = customtkinter.CTkButton(ex_frame, text='', fg_color=answer_list[1], border_color='black', border_width=2, corner_radius=30, width=30, height=30, hover_color=answer_list[1])
    middle_left.place(x=110, y=160)

    bottom_left = customtkinter.CTkButton(ex_frame, text='', fg_color=answer_list[2], border_color='black', border_width=2, corner_radius=30, width=30, height=30, hover_color=answer_list[2])
    bottom_left.place(x=110, y=200)

    top_right = customtkinter.CTkButton(ex_frame, text='', fg_color=answer_list[3], border_color='black', border_width=2, corner_radius=30, width=30, height=30, hover_color=answer_list[3])
    top_right.place(x=155, y=120)

    middle_right = customtkinter.CTkButton(ex_frame, text='', fg_color=answer_list[4], border_color='black', border_width=2, corner_radius=30, width=30, height=30, hover_color=answer_list[4])
    middle_right.place(x=155, y=160)

    bottom_right = customtkinter.CTkButton(ex_frame, text='', fg_color=answer_list[5], border_color='black', border_width=2, corner_radius=30, width=30, height=30, hover_color=answer_list[5])
    bottom_right.place(x=155, y=200)

    next_button = customtkinter.CTkButton(ex_frame, text='Next', border_color='black', border_width=1, fg_color='#F46D59', text_color='black', corner_radius=0, width=200, height=40, command=lambda: exercise(nomor))
    next_button.place(x=50, y=290)

    if nomor == 4:
        next_button.configure(text='Done', command=home)

def correct_page():
    for x in ex_frame.winfo_children():
        x.destroy()

    answer_list = copy
    for i, x in enumerate(answer_list):
        if x == '#5B9DFF':
            answer_list[i] = 'black'

    correct_label = customtkinter.CTkLabel(ex_frame, text='Correct!', font=('inter', 40, 'bold'), fg_color='transparent', text_color='white')
    correct_label.place(x=70, y=10)

    alphabet_label = customtkinter.CTkLabel(ex_frame, text=alphabet_code[indeks], font=('inter', 30, 'bold'), fg_color='transparent', text_color='black' )
    alphabet_label.place(x=135, y=70)

    # generating braille round button
    top_left = customtkinter.CTkButton(ex_frame, text='', fg_color=answer_list[0], border_color='black', border_width=2, corner_radius=30, width=30, height=30, hover_color=answer_list[0])
    top_left.place(x=110, y=120)

    middle_left = customtkinter.CTkButton(ex_frame, text='', fg_color=answer_list[1], border_color='black', border_width=2, corner_radius=30, width=30, height=30, hover_color=answer_list[1])
    middle_left.place(x=110, y=160)

    bottom_left = customtkinter.CTkButton(ex_frame, text='', fg_color=answer_list[2], border_color='black', border_width=2, corner_radius=30, width=30, height=30, hover_color=answer_list[2])
    bottom_left.place(x=110, y=200)

    top_right = customtkinter.CTkButton(ex_frame, text='', fg_color=answer_list[3], border_color='black', border_width=2, corner_radius=30, width=30, height=30, hover_color=answer_list[3])
    top_right.place(x=155, y=120)

    middle_right = customtkinter.CTkButton(ex_frame, text='', fg_color=answer_list[4], border_color='black', border_width=2, corner_radius=30, width=30, height=30, hover_color=answer_list[4])
    middle_right.place(x=155, y=160)

    bottom_right = customtkinter.CTkButton(ex_frame, text='', fg_color=answer_list[5], border_color='black', border_width=2, corner_radius=30, width=30, height=30, hover_color=answer_list[5])
    bottom_right.place(x=155, y=200)

    next_button = customtkinter.CTkButton(ex_frame, text='Next', border_color='black', border_width=1, fg_color='#F46D59', text_color='black', corner_radius=0, width=200, height=40, command=lambda: exercise(nomor))
    next_button.place(x=50, y=290)

    if nomor == 4:
        next_button.configure(text='Done', command=home)

def confirm_answer():
    global nomor
    global copy
    alphabet = alphabet_code[indeks]
    answer_list = [top_left.cget('fg_color'), middle_left.cget('fg_color'), bottom_left.cget('fg_color'), top_right.cget('fg_color'), middle_right.cget('fg_color'), bottom_right.cget('fg_color')]
    copy = answer_list.copy()
    nomor = indeks

    # answer code
    answer_code = {'A': ['#5B9DFF', 'white', 'white', 'white', 'white', 'white'],
                'B': ['#5B9DFF', '#5B9DFF', 'white', 'white', 'white', 'white'],
                'C': ['#5B9DFF', 'white', 'white', '#5B9DFF', 'white', 'white'],
                'D': ['#5B9DFF', 'white', 'white', '#5B9DFF', '#5B9DFF', 'white']}

    # match the answer 
    if answer_list == answer_code[alphabet]:
        nomor += 1
        correct_page()
    else:
        nomor += 1
        incorrect_page()

def exercise(index=0):
    global alphabet_code
    global top_left
    global middle_left
    global bottom_left
    global top_right
    global middle_right
    global bottom_right
    global indeks
    global ex_frame

    clear()

    indeks = index

    def change_color(button):
        if button.cget('fg_color') == 'white':
            button.configure(fg_color='#5B9DFF', hover_color='white')
        elif button.cget('fg_color') == '#5B9DFF':
            button.configure(fg_color='white', hover_color='#5B9DFF')

    # exercise label 
    excercise_label = customtkinter.CTkLabel(root, text='Exercise', font=('inter', 18), fg_color='transparent', text_color='black')
    excercise_label.pack(pady=(30, 10))

    # excercise frame
    ex_frame = customtkinter.CTkFrame(root, width=300, height=360, fg_color='#F1C13B', border_color='black', border_width=1, corner_radius=0)
    ex_frame.pack()

    # generating the alphabet label
    alphabet_code = [alphabet for alphabet in braille_codes.keys()]

    alphabet_label = customtkinter.CTkLabel(ex_frame, text=alphabet_code[indeks], font=('inter', 40, 'bold'), fg_color='transparent', text_color='black' )
    alphabet_label.place(x=135, y=5)

    # generating braille round button
    top_left = customtkinter.CTkButton(ex_frame, text='', fg_color='white', border_color='black', border_width=2, corner_radius=50, width=50, height=50, hover_color='#5B9DFF', command=lambda: change_color(top_left))
    top_left.place(x=85, y=70)

    middle_left = customtkinter.CTkButton(ex_frame, text='', fg_color='white', border_color='black', border_width=2, corner_radius=50, width=50, height=50, hover_color='#5B9DFF', command=lambda: change_color(middle_left))
    middle_left.place(x=85, y=140)

    bottom_left = customtkinter.CTkButton(ex_frame, text='', fg_color='white', border_color='black', border_width=2, corner_radius=50, width=50, height=50, hover_color='#5B9DFF', command=lambda: change_color(bottom_left))
    bottom_left.place(x=85, y=210)

    top_right = customtkinter.CTkButton(ex_frame, text='', fg_color='white', border_color='black', border_width=2, corner_radius=50, width=50, height=50, hover_color='#5B9DFF', command=lambda: change_color(top_right))
    top_right.place(x=165, y=70)

    middle_right = customtkinter.CTkButton(ex_frame, text='', fg_color='white', border_color='black', border_width=2, corner_radius=50, width=50, height=50, hover_color='#5B9DFF', command=lambda: change_color(middle_right))
    middle_right.place(x=165, y=140)

    bottom_right = customtkinter.CTkButton(ex_frame, text='', fg_color='white', border_color='black', border_width=2, corner_radius=50, width=50, height=50, hover_color='#5B9DFF', command=lambda: change_color(bottom_right))
    bottom_right.place(x=165, y=210)

    # check button
    check = customtkinter.CTkButton(ex_frame, text='Check', border_color='black', border_width=1, fg_color='#F46D59', text_color='black', corner_radius=0, width=200, height=40, command=confirm_answer)
    check.place(x=50, y=290)

def home():
    clear()

    # buttons for home screen
    translate_button = customtkinter.CTkButton(root, text='Translate\nto Braille', border_color='black', border_width=1, fg_color='#5B9DFF', text_color='black', corner_radius=0, width=150, height=300, command=translate_frame, font=('inter', 18))
    translate_button.pack(side='left', padx=20, pady=20)

    excercise_button = customtkinter.CTkButton(root, text='Exercise', border_color='black', border_width=1, fg_color='#F1C13B', text_color='black', corner_radius=0, width=150, height=300, command=exercise, font=('inter', 18))
    excercise_button.pack(side='right', padx=(0, 20), pady=20)

def welcome_frame():
    # labels 
    welcome_label = customtkinter.CTkLabel(root, text='Welcome to', font=('inter', 30), fg_color='transparent', text_color='black')
    welcome_label.pack(pady=(130, 0))

    braille_label = customtkinter.CTkLabel(root, text='BRAILLEARN', font=('inter', 40), fg_color='transparent', text_color='black')
    braille_label.pack(pady=10)

    # start button
    start = customtkinter.CTkButton(root, text='Start', border_color='black', border_width=1, fg_color='#F46D59', text_color='black', corner_radius=0, width=100, command=home)
    start.pack()

if __name__ == '__main__':
    welcome_frame()

root.mainloop()