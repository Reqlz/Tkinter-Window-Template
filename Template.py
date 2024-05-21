# --Config {

title_bar_background="#050505" #Hexcode
title_bar_foreground="#ffffff" #Hexcode
title_bar_font="HelveticaBold" #Font (All one word)
title_bar_font_size=10 #Font Size
title_bar_name="Custom Tkinter Titlebar" #String
window_offset=[200, 50] #Offset [X, Y] 
window_size='300x200' #Size 'Width x Height'
window_on_top=True #Boolean
# }--

# -Initialise {
import tkinter as tk #noqa
from tkinter import * #noqa
from tkinter import ttk #noqa
import os
r = tk.Tk()
r.title(title_bar_name)
r.geometry(f'{window_size}+{window_offset[0]}+{window_offset[1]}')
r.overrideredirect(True)
r.config(bg='#FFFFFF')
r.attributes("-topmost", window_on_top)
setwins=0
global r_state
r_state=True
def destroycheck(w, wins, setcheck):
    global setwins
    global r_state
    if setcheck=="s":
        if wins !=0:
            w.destroy()
            setwins-=1
    else:
      w.destroy()
      r_state=False

# }-

#   ----------TITLE BAR-----------{
def title_bar(w, name, settingswindowcheck, window):
  global setwins
  # -Functions{
  def move(e):
    w.geometry(f"+{e.x_root-xwin}+{e.y_root-ywin}")
  
  def get_pos(event):
    global xwin
    global ywin
    xwin = event.x
    ywin = event.y
  def settingsclicked():
    settingswindow()
    settingsbutton.config(bg=title_bar_background, fg="#000000")
  def reroute():
    settingsbutton.config(bg=title_bar_background, fg="#FFFFFF")
    windowcheck()
  # }-
  
  # -Widgets {
  titlebar = tk.Frame(w, bg=title_bar_background)
  titlebar_name = tk.Label(titlebar, text=f"{name}", bg=title_bar_background, fg=title_bar_foreground, font=f"{title_bar_font}, {title_bar_font_size}")
  closebutton = tk.Label(titlebar, text="X", bg=title_bar_background, fg="#ffffff")
  if window=="m":
    settingsbutton = tk.Label(titlebar, text="S", bg=title_bar_background, fg="#ffffff")
  # }-
  
  # -Bind {
  if window=="m":
    settingsbutton.bind("<Button-1>", lambda e: settingsbutton.config(bg="#CCFFCC", fg="#000000"))
    settingsbutton.bind("<ButtonRelease-1>", lambda e: reroute())
    settingsbutton.bind("<Enter>", lambda e: settingsbutton.config(bg=title_bar_background, fg="green"))
    settingsbutton.bind("<Leave>", lambda e: settingsbutton.config(fg="#FFFFFF"))
  closebutton.bind("<Button-1>", lambda e: closebutton.config(bg="red", fg="#050505"))
  closebutton.bind("<ButtonRelease-1>", lambda e: destroycheck(w, setwins, window))
  closebutton.bind("<Enter>", lambda e: closebutton.config(fg="red"))
  closebutton.bind("<Leave>", lambda e: closebutton.config(fg="#FFFFFF"))
  titlebar.bind("<B1-Motion>", move)
  titlebar.bind("<Button-1>", get_pos)
  titlebar_name.bind("<B1-Motion>", move)
  titlebar_name.bind("<Button-1>", get_pos)
  # }-
  
  # -Pack {
  titlebar_name.pack(side=LEFT, pady=2, padx=4)
  closebutton.pack(side=RIGHT, pady=2)
  if window=="m":
    settingsbutton.pack(side=RIGHT, pady=2)
  titlebar.pack(fill=X, expand=1, anchor=N)
  # }-

title_bar(r, title_bar_name, False, "m")
#   }----------TITLE BAR-----------

#   ----------SETTINGS-----------{
settings=[
  "Dark", True, "300x200"
]
themes=[
  "Light",
  "Dark",
  "Brainfuq"
]
sizes=[
  "300x200",
  "450x300",
  "1024x768",
  "1280x1040",
  "1366x768",
  "1440x900",
  "1920x1080",
]
def applysettings(tempsettings):
  settings=tempsettings
  global windowfg
  match settings[0]:
    case "light":
      r.config(bg="#FFFFFF")
      windowfg="#000000"
    case "dark":
      r.config(bg="#000000")
      windowfg="#FFFFFF"
    case "brainfuq":
      r.config(bg="#FF0000")
      windowfg="00FF00"
  match settings[1]:
    case True:
      r.attributes("-topmost", True)
    case False:
      r.attributes("-topmost", False)
  match settings[2]:
    case "300x200":
      r.geometry("300x200")
    case "450x300":
      r.geometry("450x300")
    case "1024x768":
      r.geometry("1024x768")
    case "1280x1040":
      r.geometry("1280x1040")
    case "1366x768":
      r.geometry("1366x768")
    case "1440x900":
      r.geometry("1440x900")
    case "1920x1080":
      r.geometry("1920x1080")
def windowcheck():
  global setwins
  if setwins<1:
      settingswindow()
      setwins+=1

def settingswindow():
  s=tk.Tk()
  s.attributes("-topmost", True)
  s.geometry("300x200")
  s.overrideredirect(True)
  s.config(bg='#FFFFFF')
  title_bar(s, "Settings", True, "s")
  tempsettings=settings
  apply=tk.Button(s, text="Apply", command=lambda: applysettings(tempsettings)).pack(anchor="se")
  clicked=StringVar()
  clicked.set(settings[0])
  clicked2=StringVar()
  clicked.set(settings[2])
  theme_menu=OptionMenu(s, clicked, *themes)
  theme_menu.pack(pady=10, padx=10)
  size_menu=OptionMenu(s, clicked2, *sizes)
  size_menu.pack(pady=10, padx=10)
  winx=s.winfo_reqwidth()
  winy=s.winfo_reqheight()
  theme_menu.place(x=winx*0.25, y=winy*0.25)
  size_menu.place(x=winx*0.75, y=winy*0.25)
  def checkclosestate():
    global r_state
    if r_state == False:
      s.destroy()
    s.after(10, checkclosestate)
  checkclosestate()
#   }----------SETTINGS-----------

# -Preset {
settingsbutton=tk.Button(r, text="Settings", bg=title_bar_background, fg="#ffffff", command=windowcheck)
settingsbutton.pack(anchor="se", pady=6, padx=6)
# }-

# -Window {

# Put your code here!

# }-

# -Mainloop
r.mainloop()

