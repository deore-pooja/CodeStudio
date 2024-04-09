import tkinter as tk
from tkinter import *
from tkinter import ttk 
from tkinter import font, colorchooser, filedialog, messagebox

import pdb
import subprocess
import configparser
import os 


compiler = tk.Tk()
compiler.geometry('800x500')
compiler.title('codestudio')
file_path = ''

## file path
def set_file_path(path):
    global file_path
    file_path =path


############################################## main menu ###################################################
# -------------------------------------&&&&&&&& End main menu &&&&&&&&&&& ----------------------------------
main_menu = tk.Menu()

#file icons
#new_icon = tk.PhotoImage(file='new.png')
#open_icon = tk.PhotoImage(file='open.png')
#open_recent_icon = tk.PhotoImage(file='C:\\Users\\Admin\\OneDrive\\Desktop\\icons2\\open_recent.png')
#clear_recently_opened_icon = tk.PhotoImage(file='C:\\Users\\Admin\\OneDrive\\Desktop\\icons2\\clear_recently_opened.png')
#save_icon = tk.PhotoImage(file='save.png')
#save_as_icon = tk.PhotoImage(file='save_as.png')
#auto_save_icon = tk.PhotoImage(file='C:\\Users\\Admin\\OneDrive\\Desktop\\icons2\\auto_save.png')
#close_editor_icon = tk.PhotoImage(file='C:\\Users\\Admin\\OneDrive\\Desktop\\icons2\\close_editor.png')
#exit_icon = tk.PhotoImage(file='exit.png')

file = tk.Menu(main_menu, tearoff=False)

#edit icons 
#copy_icon = tk.PhotoImage(file='copy.png')
#paste_icon = tk.PhotoImage(file='paste.png')
#cut_icon = tk.PhotoImage(file='cut.png')
#clear_all_icon = tk.PhotoImage(file='clear_all.png')
#find_icon = tk.PhotoImage(file='find.png')

edit = tk.Menu(main_menu, tearoff=False)

## view icons
tool_bar_icon = tk.PhotoImage(file='tool_bar.png')
status_bar_icon = tk.PhotoImage(file='status_bar.png')

view = tk.Menu(main_menu, tearoff=False)


Run = tk.Menu(main_menu, tearoff=False)


Terminal = tk.Menu(main_menu, tearoff=False)

##color_theme_icons

######## color theme 

light_default_icon = tk.PhotoImage(file='light_default.png')
light_plus_icon = tk.PhotoImage(file='light_plus.png')
dark_icon = tk.PhotoImage(file='dark.png')
red_icon = tk.PhotoImage(file='red.png')
monokai_icon = tk.PhotoImage(file='monokai.png')
night_blue_icon = tk.PhotoImage(file='night_blue.png')
color_theme = tk.Menu(main_menu, tearoff=False)

theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict = {
    'Light Default ' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2')
}


Help = tk.Menu(main_menu, tearoff=False)



# cascade 
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Run',menu=Run)
main_menu.add_cascade(label='Terminal',menu=Terminal)
main_menu.add_cascade(label='Color Theme', menu=color_theme)
main_menu.add_cascade(label='Help',menu=Help)


############################################## toolbar  ###################################################


tool_bar = ttk.Label(compiler)
tool_bar.pack(side=tk.TOP, fill=tk.X)

## font box 
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0, column=0, padx=5)


## size box 
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=14, textvariable = size_var, state='readonly')
font_size['values'] = tuple(range(8,81))
font_size.current(4)
font_size.grid(row=0, column=1, padx=5)

## language choice box
n = tk.StringVar()
languagechoosen = ttk.Combobox(tool_bar, width = 27, textvariable = n)
  
# Adding combobox drop down list
languagechoosen['values'] = ('Text Editor','Python')
 
languagechoosen.set('Text Editor') 
languagechoosen.grid(column=2, row=0, padx=5)

## bold button 
bold_icon = tk.PhotoImage(file='bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=3, padx=5)

## italic button 
italic_icon = tk.PhotoImage(file='italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=4, padx=5)

## underline button 
underline_icon = tk.PhotoImage(file='underline.png')
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row = 0, column=5, padx=5)

## font color button 
font_color_icon = tk.PhotoImage(file='font_color.png')
font_color_btn = ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column=6,padx=5)

## align left 
align_left_icon = tk.PhotoImage(file='align_left.png')
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=7, padx=5)

## align center 
align_center_icon = tk.PhotoImage(file='align_center.png')
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=8, padx=5)

## align right 
align_right_icon = tk.PhotoImage(file='align_right.png')
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=9, padx=5)




# -------------------------------------&&&&&&&& End toolbar  &&&&&&&&&&& ----------------------------------

############################################## text editor ###################################################

code_editor = tk.Text(compiler)
code_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(compiler)
code_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
code_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=code_editor.yview)
code_editor.config(yscrollcommand=scroll_bar.set)


# font family and font size functionality 
current_font_family = 'Arial'
current_font_size = 12

def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    code_editor.configure(font=(current_font_family, current_font_size))

def change_fontsize(event=None):
    global current_font_size
    current_font_size = size_var.get()
    code_editor.configure(font=(current_font_family, current_font_size))


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)

######## buttons functionality 

# bold button functionality
def change_bold():
    text_property = tk.font.Font(font=code_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        code_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        code_editor.configure(font=(current_font_family, current_font_size, 'normal'))
    
bold_btn.configure(command=change_bold)


# italic functionlaity
def change_italic():
    text_property = tk.font.Font(font=code_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        code_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        code_editor.configure(font=(current_font_family, current_font_size, 'normal'))
    
italic_btn.configure(command=change_italic)

# underline functionality 
def change_underline():
    text_property = tk.font.Font(font=code_editor['font'])
    if text_property.actual()['underline'] == 0:
        code_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        code_editor.configure(font=(current_font_family, current_font_size, 'normal'))
    
underline_btn.configure(command=change_underline)


## font color functionality 
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    code_editor.configure(fg=color_var[1])


font_color_btn.configure(command=change_font_color)

### align functionality 

def align_left():
    text_content = code_editor.get(1.0, 'end')
    code_editor.tag_config('left', justify=tk.LEFT)
    code_editor.delete(1.0, tk.END)
    code_editor.insert(tk.INSERT, text_content, 'left')

align_left_btn.configure(command=align_left)

## center 
def align_center():
    text_content = code_editor.get(1.0, 'end')
    code_editor.tag_config('center', justify=tk.CENTER)
    code_editor.delete(1.0, tk.END)
    code_editor.insert(tk.INSERT, text_content, 'center')

align_center_btn.configure(command=align_center)

## right 
def align_right():
    text_content = code_editor.get(1.0, 'end')
    code_editor.tag_config('right', justify=tk.RIGHT)
    code_editor.delete(1.0, tk.END)
    code_editor.insert(tk.INSERT, text_content, 'right')

align_right_btn.configure(command=align_right)





code_editor.configure(font=('Arial', 12))


# -------------------------------------&&&&&&&& End text editor &&&&&&&&&&& ----------------------------------


##############################################  status bar ###################################################

status_bar = ttk.Label(compiler, text = 'Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False 
def changed(event=None):
    global text_changed
    if code_editor.edit_modified():
        text_changed = True 
        words = len(code_editor.get(1.0, 'end-1c').split())
        characters = len(code_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f'Characters : {characters} Words : {words}')
    code_editor.edit_modified(False)

code_editor.bind('<<Modified>>', changed)




# -------------------------------------&&&&&&&& End  status bar &&&&&&&&&&& ----------------------------------


############################################## main menu functinality ###################################################

## variable 
url = ''

## new functionality
def new_file(event=None):
    global url 
    url = ''
    code_editor.delete(1.0, tk.END)

## file commands 
file.add_command(label='New',compound=tk.LEFT, accelerator='Ctrl+N', command=new_file)

## open functionality

def open_file(event=None):
    global url 
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            code_editor.delete(1.0, tk.END)
            code_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return 
    except:
        return 
    compiler.title(os.path.basename(url))

file.add_command(label='Open file', compound=tk.LEFT, accelerator='Ctrl+O', command=open_file)


## open recent 

def Open_Recent(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Open Recent')
    try:
        with open(url, 'r') as fr:
            code_editor.delete(1.0, tk.END)
            code_editor.insert(tk.END, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    compiler.title(os.path.basename(url))

file.add_command(label='Open Recent', compound=tk.LEFT, accelerator='Ctrl+R', command=Open_Recent)


## clear recently opened

def Clear_Recently_Opened(event=None):
    global url
    # Clear the global variable or list that holds the URLs of recently opened files
    url = None
    # Clear the contents of the code_editor widget
    code_editor.delete(1.0, tk.END)
    # Update the title of the compiler window
    compiler.title("Compiler")                

file.add_command(label='Clear Recently Opened', compound=tk.LEFT, command=Clear_Recently_Opened)


## save file 

def save_file(event=None):
    global url 
    try:
        if url:
            content = str(code_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
            content2 = code_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return 

file.add_command(label='Save', compound=tk.LEFT, accelerator='Ctrl+S', command = save_file)


## save as functionality 

def save_as(event=None):
    global url 
    try:
        content = code_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
        url.write(content)
        url.close()
    except:
        return 

file.add_command(label='Save As', compound=tk.LEFT, accelerator='Ctrl+Alt+S', command=save_as)

def Auto_Save(event=None):
    global url
    try:
        content = code_editor.get(1.0, tk.END)
        # Use filedialog.asksaveasfile() to prompt for a file save location
        file = filedialog.asksaveasfile(mode='w', filetypes=(('Text File', '.txt'), ('All Files', '.*')))
        if file is not None:
            # Write the content to the file
            file.write(content)
            file.close()
    except:
        return

file.add_command(label='Auto Save', compound=tk.LEFT, command=Auto_Save)


def Close_Editor(event=None):
    global url
    try:
        content = code_editor.get(1.0, tk.END)
        # Use filedialog.asksaveasfile() to prompt for a file save location before closing
        file = filedialog.asksaveasfile(mode='w', filetypes=(('Text File', '.txt'), ('All Files', '.*')))
        if file is not None:
            # Write the content to the file
            file.write(content)
            file.close()
        code_editor.delete(1.0, tk.END)  # Clear the code_editor widget
    except FileNotFoundError:
        return
    except:
        return
    compiler.title('Untitled')  # Update the title to 'Untitled'

file.add_command(label='Close Editor', compound=tk.LEFT, accelerator='Ctrl+F', command=Close_Editor)


## exit functionality 

def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning',' Do you want to save the file ?')
            if mbox is True:
                if url:
                    content =code_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        compiler.destroy()
                else:
                    content2 = str(code_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    compiler.destroy()
            elif mbox is False:
                compiler.destroy()
        else:
            compiler.destroy()
    except:
        return 
file.add_command(label='Exit', compound=tk.LEFT, accelerator='Ctrl+Q', command=exit_func)


############ find functionality 

def find_func(event=None):

    def find():
        word = find_input.get()
        code_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = code_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break 
                end_pos = f'{start_pos}+{len(word)}c'
                code_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                code_editor.tag_config('match', foreground='red', background='yellow')
    
    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = code_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        code_editor.delete(1.0, tk.END)
        code_editor.insert(1.0, new_content)

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    ## frame 
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    ## labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text= 'Replace')

    ## entry 
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## button 
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text= 'Replace', command=replace)

    ## label grid 
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    ## entry grid 
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    ## button grid 
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()

## edit commands 
edit.add_command(label='Undo',compound=tk.LEFT,accelerator='Ctrl+Z',command=lambda:code_editor.event_generate("<Contrl z>"))
edit.add_command(label='Copy', compound=tk.LEFT, accelerator='Ctrl+C', command=lambda:code_editor.event_generate("<Control c>"))
edit.add_command(label='Paste',compound=tk.LEFT, accelerator='Ctrl+V', command=lambda:code_editor.event_generate("<Control v>"))
edit.add_command(label='Cut', compound=tk.LEFT, accelerator='Ctrl+X', command=lambda:code_editor.event_generate("<Control x>"))
edit.add_command(label='Clear All', compound=tk.LEFT, accelerator='Ctrl+Alt+X', command= lambda:code_editor.delete(1.0, tk.END))
edit.add_command(label='Find/Replace', compound=tk.LEFT, accelerator='Ctrl+F', command = find_func)

## view check button 

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False 
    else :
        code_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        code_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True 


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False 
    else :
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True 


view.add_checkbutton(label='Tool Bar',onvalue=True, offvalue=0,variable = show_toolbar, compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label='Status Bar',onvalue=1, offvalue=False,variable = show_statusbar, compound=tk.LEFT, command=hide_statusbar)


## Run Functionality

def run_code(codestudio):
    file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Python Files', '*.py'), ('All Files', '*.*')))
    if file_path:
        try:
            subprocess.run(['python', file_path])
        except Exception as e:
            messagebox.showerror("Error", str(e))

Run.add_command(label='Run', compound=tk.LEFT, accelerator='F5', command=run_code)


def Start_Debugger(codestudio):
    content = str(code_editor.get(1.0, tk.END))
    codestudio.test()
    # Save the content to a temporary file
    with open('temp.py', 'w') as f:
        f.write(content)
    # Run the temporary file using subprocess
    subprocess.run(['python', 'temp.py'])
    # Remove the temporary file
    os.remove('temp.py')

Run.add_command(label='Run Task', command=lambda: Start_Debugger(codestudio))

def Start_Debugging(codestudio):
    content = str(code_editor.get(1.0, tk.END))
    codestudio.test()
    pdb.run('codestudio.py')

Run.add_command(label='Start Debugging', compound=tk.LEFT, accelerator='F5', command=lambda: Start_Debugging(codestudio))

def Run_Without_Debugging(codestudio):
    content = str(code_editor.get(1.0, tk.END))
    codestudio.test()
    print(get(1.0, tk.END))

Run.add_command(label='Run Without Debugging', compound=tk.LEFT, accelerator='Ctrl+F5', command=lambda: Run_Without_Debugging(codestudio))

def Stop_Debugging(codestudio):
    codestudio.test()
    pdb.set_trace() 
    tk.stopdebugging()

Run.add_command(label='Stop Debugging', compound=tk.LEFT, accelerator='Shift+F5', command=lambda: Stop_Debugging(codestudio))

def Restart_Debugging(codestudio):
    content = str(code_editor.get(1.0, tk.END))
    codestudio.test()
    pdb.set_trace()
    pdb.debug('codestudio.py')

Run.add_command(label='Restart Debugging', compound=tk.LEFT, accelerator='Ctrl+F6', command=lambda: Restart_Debugging(codestudio))


## Open Configuration Functionality
config = configparser.ConfigParser()

# Add the structure to the file we will create
config.add_section('postgresql')
config.set('postgresql', 'host', 'localhost')
config.set('postgresql', 'user', 'finxter1')
config.set('postgresql', 'port', '5522')
config.set('postgresql', 'password', '02_qwerty_2002')
config.set('postgresql', 'db', 'postgres')
config.add_section('user_info')
config.set('user_info', 'admin', 'Deore Pooja')
config.set('user_info', 'login', 'deorepooja')
config.set('user_info', 'password', '02_qwerty_2002')
Run.add_command(label='Open configuration')

## Step Over Functionality
def Step_Over(codestudio):
    content = str(code_editor.get(1.0.tk.Selected))
    codestudio.test()
    pdb.run('codestudio.py')
Run.add_command(label='Step Over',compound=tk.LEFT,accelerator='F10')

## Step Into Functionality
def Step_Into(codestudio):
    content = str(code_editor.get(1.0.tk.Selected))
    codestudio.test()
    pdb.run('codestudio.py')
Run.add_command(label='Step Into',compound=tk.LEFT,accelerator='F11')

## Step Out Functionality
def Step_Out (codestudio):
    content = str(code_editor.get(1.0.tk.Selected))
    codestudio.test()
    pdb.run('codestudio.py')
Run.add_command(label='Step Out',compound=tk.LEFT,accelerator='Shift+F11')

## Continue Functionality
def Continue(codestudio):
     content = str(code_editor.get(1.0,tk.END))
     codestudio.test()
     pdb.run('codestudio.py')
Run.add_command(label='Continue',compound=tk.LEFT,accelerator='Alt+F5')

## Terminal command

## New Terminal Functionality

def Open_Terminal():
    subprocess.Popen(['start', 'cmd'], shell=True)

Terminal.add_command(label='Open Terminal', compound=tk.LEFT, accelerator='Ctrl+T', command=Open_Terminal)

def New_Terminal(codestudio):
    codestudio.test()
    tk.python
    pdb.run('codestudio.py')
    content = str(code_editor.get(1.0.tk.END))
    exec(open("codestudio.py").read())
Terminal.add_command(label='New Terminal',compound=tk.LEFT,accelerator='Ctrl+Shift+T')


## Run Build Task Functionality
def Run_Build_Task(codestudio):
    content = str(code_editor.get(1.0.tk.END))
    codestudio.test()
    pdb.run('codestudio.py')
Terminal.add_command(label='Run Build Task',compound=tk.LEFT,accelerator='Ctrl+Shift+B')

## Run Active File Functionality
def Run_Active_File(codestudio):
    content = str(code_editor.get(1.0.tk.END))
    codestudio.test()
    pdb.run('codestudio.py')
Terminal.add_command(label='Run Active File')

## Run Selected Text Functionality
def Run_Selected_Text(codestudio):
    content = str(code_editor.get(tk.selected))
    codestudio.test()
    pdb.run('codestudio.py')
Terminal.add_command(label='Run Selected Text')

## Terminate Task Functionality
def Terminate_Task(codestudio):
    codestudio.test()
    pdb.set_trace() 
    tk.terminatetask()
Terminal.add_command(label='Terminate Task')




## Help command
Help.add_command(label='Show All Commands',compound=tk.LEFT,accelerator='Ctrl+shift+P')
Help.add_command(label='Join Us On Email')
Help.add_command(label='Report Issue')
Help.add_command(label='Check For updates')    



## view check button 
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False 
    else :
        code_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        code_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True 


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False 
    else :
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True 
        
### color theme functionality

def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    code_editor.config(background=bg_color, fg=fg_color) 
count = 0 
for i in color_dict:
    color_theme.add_radiobutton(label = i, variable=theme_choice, compound=tk.LEFT, command=change_theme)
    count += 1 
        


# -------------------------------------&&&&&&&& End main menu  functinality&&&&&&&&&&& ----------------------------------

compiler.config(menu=main_menu)

#### bind shortcut keys 

## file
compiler.bind("<Control-n>", new_file)
compiler.bind("<Control-o>", open_file)
compiler.bind("<Control-r>", Open_Recent)
compiler.bind("<Control-s>", save_file)
compiler.bind("<Control-Alt-s>", save_as)
compiler.bind("<Control-f>", Close_Editor)
compiler.bind("<Control-q>", exit_func)

## edit 
compiler.bind("<Control-f>", find_func)

compiler.mainloop()