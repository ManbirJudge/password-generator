# ###################################
# Author: Manbir Singh Judge
# Date: Aug to Sep, 2021
# ###################################

import json
import pathlib
import random
from tkinter import *
from tkinter.ttk import Checkbutton

import pyperclip as pc

SYMBOLS = ['!', '@', '#', '$', '%', '&', '^', '*', '+', '-']
NUMBER_CHARS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
LOWERCASE_CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
UPPERCASE_CHARS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']
SIMILAR_CHARS = ['i', 'I', 'l', 'L', '1', '0', 'o', 'O']
AMB_CHARS = ['{', '}', '[', ']', '(', ')', '/', '\\', '\'', '\"', '`', ',', ';', ':', '.', '<', '>']


def save_settings():
    settings_dict = {
        'pwd_length': int(length_var.get()),
        'inc_symbols': bool(include_symbols.get()),
        'inc_nums': bool(include_nums.get()),
        'inc_lower_chr': bool(include_lower_chr.get()),
        'inc_upper_chr': bool(include_upper_chr.get()),
        'exc_similar_chr': bool(exclude_similar_chr.get()),
        'inc_amb_chr': bool(include_amb_chr.get()),
        'gen_on_this_dev': None,
        'auto_select': bool(auto_select.get()),
        'save_my_pre': bool(save_my_pre.get()),
    }

    with open('settings.json', 'w') as settings_json_file:
        json.dump(settings_dict, settings_json_file)


def load_settings():
    with open('settings.json', 'r') as settings_file:
        settings = dict(json.load(settings_file))

    if settings.get('pwd_length') is not None:
        length_var.set(str(settings['pwd_length']))

    if settings.get('inc_symbols') is not None:
        include_symbols.set(int(settings['inc_symbols']))

    if settings.get('inc_nums') is not None:
        include_nums.set(int(settings['inc_nums']))

    if settings.get('inc_lower_chr') is not None:
        include_lower_chr.set(int(settings['inc_lower_chr']))

    if settings.get('inc_upper_chr') is not None:
        include_upper_chr.set(int(settings['inc_upper_chr']))

    if settings.get('exc_similar_chr') is not None:
        exclude_similar_chr.set(int(settings['exc_similar_chr']))

    if settings.get('inc_amb_chr') is not None:
        include_amb_chr.set(int(settings['inc_amb_chr']))

    if settings.get('gen_on_this_dev') is not None:
        gen_on_ur_dev.set(int(settings['gen_on_this_dev']))

    if settings.get('auto_select') is not None:
        auto_select.set(int(settings['auto_select']))

    if settings.get('save_my_pre') is not None:
        save_my_pre.set(int(settings['save_my_pre']))


def generate_pwd():
    char_list = []

    pwd_len = int(length_var.get())

    include_symbols_ = bool(include_symbols.get())
    include_nums_ = bool(include_nums.get())
    include_lower_chr_ = bool(include_lower_chr.get())
    include_upper_chr_ = bool(include_upper_chr.get())
    exclude_similar_chr_ = bool(exclude_similar_chr.get())
    include_amb_chr_ = bool(include_amb_chr.get())

    auto_select_ = auto_select.get()
    save_my_pre_ = save_my_pre.get()

    if include_symbols_:
        char_list += SYMBOLS

    if include_nums_:
        char_list += NUMBER_CHARS

    if include_lower_chr_:
        char_list += LOWERCASE_CHARS

    if include_upper_chr_:
        char_list += UPPERCASE_CHARS

    if exclude_similar_chr_:
        for similar_char in SIMILAR_CHARS:
            if similar_char in char_list:
                char_list.remove(similar_char)

    if include_amb_chr_:
        char_list += AMB_CHARS

    password = ''

    if len(char_list) <= 0:
        return

    for i in range(pwd_len):
        new_chr = random.choice(char_list)
        password += str(new_chr)

    new_pwd.set(str(password))

    if auto_select_:
        new_pwd_entry.focus()
        new_pwd_entry.selection_range(0, END)

    if save_my_pre_:
        save_settings()


def copy_pwd():
    new_pwd_entry.focus()
    new_pwd_entry.selection_range(0, END)

    pwd = str(new_pwd.get())

    try:
        pc.copy(pwd)
    except Exception as e:
        print(f'[DEBUG] Error while copying text: {e}')


# configuring the window
root = Tk()

root.title('Password Generator')
root.geometry('530x300+100+100')
root.resizable(False, False)

# labels
Label(root, text="Password Length:").place(x=0, y=0)
Label(root, text="Include Symbols:").place(x=0, y=20)
Label(root, text="Include Numbers:").place(x=0, y=40)
Label(root, text="Include Lowercase Characters:").place(x=0, y=60)
Label(root, text="Include Uppercase Characters:").place(x=0, y=80)
Label(root, text="Exclude Similar Characters:").place(x=0, y=100)
Label(root, text="Include Ambiguous:").place(x=0, y=120)
Label(root, text="Generate on Your Device:").place(x=0, y=140)
Label(root, text="Auto-Select:").place(x=0, y=160)
Label(root, text="Save my Preferences:").place(x=0, y=180)
Label(root, text="Your New Password:").place(x=0, y=200)

# variables
length_var = StringVar()

include_symbols = IntVar()
include_nums = IntVar()
include_lower_chr = IntVar()
include_upper_chr = IntVar()
exclude_similar_chr = IntVar()
include_amb_chr = IntVar()
gen_on_ur_dev = IntVar()
auto_select = IntVar()
save_my_pre = IntVar()

new_pwd = StringVar()

# input widgets
length_entry = Entry(root, textvariable=length_var, relief=SOLID)
length_entry.place(x=200, y=0)

include_symbols_check = Checkbutton(root, text='e.g. @#$%&* ...', variable=include_symbols)
include_symbols_check.place(x=200, y=20)

include_nums_check = Checkbutton(root, text='e.g. 012345 ...', variable=include_nums)
include_nums_check.place(x=200, y=40)

include_lower_chr_check = Checkbutton(root, text='e.g. abcdef ...', variable=include_lower_chr)
include_lower_chr_check.place(x=200, y=60)

include_upper_chr_check = Checkbutton(root, text='e.g. ABCDEF ...', variable=include_upper_chr)
include_upper_chr_check.place(x=200, y=80)

exclude_similar_chr_check = Checkbutton(root, text='e.g. il1L 0oO', variable=exclude_similar_chr)
exclude_similar_chr_check.place(x=200, y=100)

include_amb_chr_check = Checkbutton(root, text='e.g. {}[]()/\\\'\"`~,;:.<>', variable=include_amb_chr)
include_amb_chr_check.place(x=200, y=120)

gen_on_ur_dev_check = Checkbutton(
    root,
    text='Do not Send across the Internet',
    variable=gen_on_ur_dev,
    state="disabled"
)
gen_on_ur_dev_check.place(x=200, y=140)

auto_select_check = Checkbutton(
    root,
    text='Select the Password when Generated',
    variable=auto_select
)
auto_select_check.place(x=200, y=160)

save_my_pre_check = Checkbutton(
    root,
    text='Save the Password Generation Settings on this Computer',
    variable=save_my_pre
)
save_my_pre_check.place(x=200, y=180)

new_pwd_entry = Entry(root, textvariable=new_pwd, state="readonly")
new_pwd_entry.place(x=200, y=200)

# buttons
new_pwd_copy_btn = Button(root, text='Copy', command=copy_pwd)
new_pwd_copy_btn.place(x=340, y=200)

gen_pwd_btn = Button(root, text='Generate Password', command=generate_pwd)
gen_pwd_btn.place(x=210, y=260)

# the main
if __name__ == "__main__":
    length_var.set('30')
    include_symbols.set(1)
    include_nums.set(1)
    include_lower_chr.set(1)
    include_upper_chr.set(1)

    if pathlib.Path.exists(pathlib.Path('settings.json')):
        load_settings()

    root.mainloop()
