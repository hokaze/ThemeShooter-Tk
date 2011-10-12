#!/usr/bin/env python
# -ThemeShooterTk preferences program by HoKaze-
# Modifies some settings in the settings file...although really, it's not that hard to edit it by hand <_<;

from Tkinter import *
from PIL import Image, ImageTk
import ConfigParser, os

class data:
    programpath = sys.path[0]
    config = ConfigParser.ConfigParser()
    settingsfile = os.path.join(programpath, "settings") 
    config.read(settingsfile)
    dummy_text = config.get("Text", "dummy text")
    cli_output = config.get("Text", "command line output")
    appdb_images = config.get("Images", "appdb images")
    replacement_theme = config.get("Images", "missing images replacement theme")

root = Tk()
root.title("ThemeShooterTk Preferences")


def toggle_dummy_text(event):
    if data.dummy_text == "yes":
        data.dummy_text = "no"
        c2.itemconfig(DummyCheckBox, image=CheckBox_photo)
    else:
        data.dummy_text = "yes"
        c2.itemconfig(DummyCheckBox, image=CheckBox_photo_selected)

def toggle_cli_output(event):
    if data.cli_output == "yes":
        data.cli_output = "no"
        c3.itemconfig(CliCheckBox, image=CheckBox_photo)
    else:
        data.cli_output = "yes"
        c3.itemconfig(CliCheckBox, image=CheckBox_photo_selected)

def toggle_appdb_images(event):
    if data.appdb_images == "yes":
        data.appdb_images = "no"
        c4.itemconfig(ImageCheckBox, image=CheckBox_photo)
    else:
        data.appdb_images = "yes"
        c4.itemconfig(ImageCheckBox, image=CheckBox_photo_selected)

def ClassicTheme(event):
    if data.replacement_theme != "classic":
        c5.itemconfig(ClassicRadioBox, image=Radio_photo_selected)
        c5.itemconfig(DarkwaterRadioBox, image=Radio_photo)
        data.replacement_theme = "classic"

def DarkwaterTheme(event):
    if data.replacement_theme != "darkwater":
        c5.itemconfig(DarkwaterRadioBox, image=Radio_photo_selected)
        c5.itemconfig(ClassicRadioBox, image=Radio_photo)
        data.replacement_theme = "darkwater"

def SaveSettings():
    data.config.set("Text", "dummy text", data.dummy_text)
    data.config.set("Text", "command line output", data.cli_output)
    data.config.set("Images", "appdb images", data.appdb_images)
    data.config.set("Images", "missing images replacement theme", data.replacement_theme)
    data.config.write(sys.stdout) #print what will be saved
    f = open(data.settingsfile, "w") #open settings file in write mode
    data.config.write(f) #write settings to file

# Dummy text
dummy_label = Label(root, text="Use dummy text?")
# Checkbox code
CheckBox_image = Image.open(os.path.join(data.programpath, "CheckBox2.png"))
CheckBox_photo = ImageTk.PhotoImage(CheckBox_image)
CheckBox_image_selected = Image.open(os.path.join(data.programpath, "CheckBox1.png"))
CheckBox_photo_selected = ImageTk.PhotoImage(CheckBox_image_selected)
c2 = Canvas(root, width=15, height=15, highlightthickness=0)
if data.dummy_text == "yes":
    DummyCheckBox = c2.create_image(7, 7, image=CheckBox_photo_selected)
else:
    DummyCheckBox = c2.create_image(7, 7, image=CheckBox_photo)
c2.tag_bind(DummyCheckBox, "<Button-1>", toggle_dummy_text)    

# Command line output
cli_label = Label(root, text="Enable command line output?")
# Checkbox code
c3 = Canvas(root, width=15, height=15, highlightthickness=0)
if data.cli_output == "yes":
    CliCheckBox = c3.create_image(7, 7, image=CheckBox_photo_selected)
else:
    CliCheckBox = c3.create_image(7, 7, image=CheckBox_photo)
c3.tag_bind(CliCheckBox, "<Button-1>", toggle_cli_output) 

# Appdb images
image_label = Label(root, text="Use Application Database images?")
# Checkbox code
c4 = Canvas(root, width=15, height=15, highlightthickness=0)
if data.appdb_images == "yes":
    ImageCheckBox = c4.create_image(7, 7, image=CheckBox_photo_selected)
else:
    ImageCheckBox = c4.create_image(7, 7, image=CheckBox_photo)
c4.tag_bind(CliCheckBox, "<Button-1>", toggle_appdb_images) 

# Theme replacement
theme_label = Label(root, text="Which theme to use in case of missing files?")
# Radiobox code
c5 = Canvas(root, width=300, height=15, highlightthickness=0)
Radio_image = Image.open(os.path.join(data.programpath, "RadioButton2.png"))
Radio_photo = ImageTk.PhotoImage(Radio_image)
Radio_image_selected = Image.open(os.path.join(data.programpath, "RadioButton1.png"))
Radio_photo_selected = ImageTk.PhotoImage(Radio_image_selected)
if data.replacement_theme == "classic":
    ClassicRadioBox = c5.create_image(57, 7, image=Radio_photo_selected)
    ClassicText = c5.create_text(87, 7, text="Classic")
    DarkwaterRadioBox = c5.create_image(197, 7, image=Radio_photo)
    DarkwaterText = c5.create_text(237, 7, text="Darkwater")
else:
    ClassicRadioBox = c5.create_image(57, 7, image=Radio_photo)
    ClassicText = c5.create_text(87, 7, text="Classic")
    DarkwaterRadioBox = c5.create_image(197, 7, image=Radio_photo_selected)
    DarkwaterText = c5.create_text(237, 7, text="Darkwater")
c5.tag_bind(ClassicRadioBox, "<Button-1>", ClassicTheme)
c5.tag_bind(ClassicText, "<Button-1>", ClassicTheme)
c5.tag_bind(DarkwaterRadioBox, "<Button-1>", DarkwaterTheme)
c5.tag_bind(DarkwaterText, "<Button-1>", DarkwaterTheme)

# Save Button
c = Canvas(root, width=70, height=28, highlightthickness=0)
b1_image = Image.open(os.path.join(data.programpath, "button-normal.png"))
b1_photo = ImageTk.PhotoImage(b1_image)
b1_image_hover = Image.open(os.path.join(data.programpath, "button-prelight.png"))
b1_photo_hover = ImageTk.PhotoImage(b1_image_hover)
b1_image_press = Image.open(os.path.join(data.programpath, "button-pressed-prelight.png"))
b1_photo_press = ImageTk.PhotoImage(b1_image_press)
b1 = c.create_image(35, 14, image=b1_photo)
t1 = c.create_text(35, 14, text="Save")
def mousepress1(event):
    c.itemconfig(b1, image=b1_photo_press)
    SaveSettings()
def mouseover1(event):
    c.itemconfig(b1, image=b1_photo_hover)
def mouseoff1(event):
    c.itemconfig(b1, image=b1_photo)
def mouserelease1(event):
    c.itemconfig(b1, image=b1_photo)
c.tag_bind(b1, "<Button-1>", mousepress1)
c.tag_bind(b1, "<Enter>", mouseover1)
c.tag_bind(b1, "<Leave>", mouseoff1)
c.tag_bind(b1, "<ButtonRelease-1>", mouserelease1)
c.tag_bind(t1, "<Button-1>", mousepress1)
c.tag_bind(t1, "<Enter>", mouseover1)
c.tag_bind(t1, "<Leave>", mouseoff1)
c.tag_bind(t1, "<ButtonRelease-1>", mouserelease1)


# Setup root window
Intro = Label(root, text="Set several settings for ThemeShooterTk here:")
Intro.grid(row=0, column=0, columnspan=2, padx=5, pady=10)
dummy_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
c2.grid(row=1, column=1, padx=5, pady=5)
cli_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
c3.grid(row=2, column=1, padx=5, pady=5)
image_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)
c4.grid(row=3, column=1, padx=5, pady=5)
theme_label.grid(row=4, columnspan=2, padx=5, pady=5, sticky=W)
c5.grid(row=5, columnspan=2, padx=5, pady=5)
c.grid(row=6, columnspan=2, padx=5, pady=10)

root.mainloop()
