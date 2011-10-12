#!/usr/bin/env python
# -ThemeShooterTk by HoKaze-
# Produces preview or screenshot of HBC theme

# import everything
from Tkinter import *
from tkMessageBox import *
import tkFileDialog
import zipfile
import os
from PIL import Image, ImageTk, ImageFont, ImageDraw, ImageChops, ImageEnhance
import re, linecache
from decimal import *
import random
import ConfigParser
import shutil #needed for shutil.rmtree, to remove directories and contents
import operator #needed to subtract tuples to fix bubble placement on saved files


# determine location of program folder (for extracting files, fonts, etc)
programpath = sys.path[0]

# determine current/original folder (for navigation, cli purposes, etc)
originalpath = os.getcwd()

# determine dark water theme folder (for missing files)
darkwaterpath = os.path.join(programpath, "darkwater")

# determine classic theme folder (for missing files)
classicpath = os.path.join(programpath, "classic")

# setup config file
config = ConfigParser.ConfigParser()
config.read(os.path.join(programpath, "settings"))

# setup which replacement theme to use
replacement_theme = (config.get("Images", "missing images replacement theme"))
if replacement_theme == "darkwater":
    replacement_theme_path = darkwaterpath
elif replacement_theme == "classic":
    replacement_theme_path = classicpath
else:
    replacement_theme_path = os.path.join(programpath, replacement_theme)

# use extra console output?
consoleoutput = (config.get("Text", "command line output"))


if consoleoutput == "yes":
    print "Drawing root window..."

# setup root window
root = Tk()
root.title("ThemeShooterTk")


# class containing bubble co-ordinates (4:3)
class BubbleClass:
    def __init__(self):
        self.pos1 = (random.randrange(0, 640), random.randrange(0, 480))
        self.pos2 = (random.randrange(0, 640), random.randrange(0, 480))
        self.pos3 = (random.randrange(0, 640), random.randrange(0, 480))
        self.pos4 = (random.randrange(0, 640), random.randrange(0, 480))
        self.pos5 = (random.randrange(0, 640), random.randrange(0, 480))
        self.pos6 = (random.randrange(0, 640), random.randrange(0, 480))
        self.rot1 = random.randrange(-45, 45)
        self.rot2 = random.randrange(-45, 45)
        self.rot3 = random.randrange(-45, 45)
        self.rot4 = random.randrange(-45, 45)
        self.rot5 = random.randrange(-45, 45)
        self.rot6 = random.randrange(-45, 45)
        self.size1 = random.randrange(32, 96)
        self.size2 = random.randrange(32, 96)
        self.size3 = random.randrange(32, 96)
        self.size4 = random.randrange(32, 96)
        self.size5 = random.randrange(32, 96)
        self.size6 = random.randrange(32, 96)
BubbleLocation = BubbleClass() # calls the class, randomises bubble positions


# file dialog for choosing theme.zip
def choosefile():
    global themefile
    global BubbleLocation
    os.chdir(originalpath) #cd to original dir for file select
    themefile = tkFileDialog.askopenfilename(title="Open theme file", filetypes=[("zip archive",".zip"),("All files","*")])
    filepath.delete(1.0, END)
    filepath.insert(END, themefile)
    BubbleLocation = BubbleClass() # command to re-randomise the bubbles with each new file opened


# Save screenshot depending on which radiobutton is chosen
def genscreen():
    if radio.pressed1 == 1:
        genscreen1()
    elif radio.pressed2 == 1:
        genscreen2()
    #elif radio.pressed3 == 1:
    #    genscreen3()


# List View (4:3) Themeshot save
def genscreen1():
    if consoleoutput == "yes":
        print "Generating screenshot..."
    os.chdir(originalpath) #cd to original dir to create file
    snapshot = Image.new("RGBA", (640, 480)) #create new image
    snap1 = Image.open(background_file) #open background
    snapshot.paste(snap1, (0, 0)) #place background

    # bubbles have been moved to ensure they remain behind all other objects
    snap4mask = Image.open(bubble1_file)
    snap4_1mask = snap4mask.rotate(BubbleLocation.rot1, Image.BICUBIC, expand=True)
    snap4_1mask = snap4_1mask.resize((BubbleLocation.size1, BubbleLocation.size1), Image.BICUBIC)
    snap4_1 = snap4_1mask.convert("RGB")
    #snapshot.paste(snap4, (73, 303), snap4mask)
    genscreen_pos1 = tuple(map(operator.sub,BubbleLocation.pos1,(snap4_1.size[0]/2,snap4_1.size[1]/2))) #Coordinate system differences between the window and the saved file mean that the position needs to be altered. This code calculates the adjustment to be made (half the image size as a tuple) and via sorcery adds the original pos1 tuple to the half-size tuple. WTF!?
    snapshot.paste(snap4_1, genscreen_pos1, snap4_1mask) #random bubble placement
    snap4_2mask = snap4mask.rotate(BubbleLocation.rot2, Image.BICUBIC, expand=True)
    snap4_2mask = snap4_2mask.resize((BubbleLocation.size2, BubbleLocation.size2), Image.BICUBIC)
    snap4_2 = snap4_2mask.convert("RGB")
    genscreen_pos2 = tuple(map(operator.sub,BubbleLocation.pos2,(snap4_2.size[0]/2,snap4_1.size[1]/2)))
    snapshot.paste(snap4_2, genscreen_pos2, snap4_2mask)
    snap5mask = Image.open(bubble2_file)
    snap5_1mask = snap5mask.rotate(BubbleLocation.rot3, Image.BICUBIC, expand=True)
    snap5_1mask = snap5_1mask.resize((BubbleLocation.size3, BubbleLocation.size3), Image.BICUBIC)
    snap5_1 = snap5_1mask.convert("RGB")
    genscreen_pos3 = tuple(map(operator.sub,BubbleLocation.pos3,(snap5_1.size[0]/2,snap4_1.size[1]/2)))
    snapshot.paste(snap5_1, genscreen_pos3, snap5_1mask)
    snap5_2mask = snap5mask.rotate(BubbleLocation.rot4, Image.BICUBIC, expand=True)
    snap5_2mask = snap5_2mask.resize((BubbleLocation.size4, BubbleLocation.size4), Image.BICUBIC)
    snap5_2 = snap5_2mask.convert("RGB")
    genscreen_pos4 = tuple(map(operator.sub,BubbleLocation.pos4,(snap5_2.size[0]/2,snap4_1.size[1]/2)))
    snapshot.paste(snap5_2, genscreen_pos4, snap5_2mask)
    snap6mask = Image.open(bubble3_file)
    snap6_1mask = snap6mask.rotate(BubbleLocation.rot5, Image.BICUBIC, expand=True)
    snap6_1mask = snap6_1mask.resize((BubbleLocation.size5, BubbleLocation.size5), Image.BICUBIC)
    snap6_1 = snap6_1mask.convert("RGB")
    genscreen_pos5 = tuple(map(operator.sub,BubbleLocation.pos5,(snap6_1.size[0]/2,snap4_1.size[1]/2)))
    snapshot.paste(snap6_1, genscreen_pos5, snap6_1mask) #random bubble placement
    snap6_2mask = snap6mask.rotate(BubbleLocation.rot6, Image.BICUBIC, expand=True)
    snap6_2mask = snap6_2mask.resize((BubbleLocation.size6, BubbleLocation.size6), Image.BICUBIC)
    snap6_2 = snap6_2mask.convert("RGB")
    genscreen_pos6 = tuple(map(operator.sub,BubbleLocation.pos6,(snap6_2.size[0]/2,snap4_1.size[1]/2)))
    snapshot.paste(snap6_2, genscreen_pos6, snap6_2mask)

    snap2mask = Image.open(appsprev_file) #use image as mask
    snap2 = snap2mask.convert("RGB") #create RGB version
    snapshot.paste(snap2, (23, 198), snap2mask) #place image, using RGB and mask to avoid alpha problems...
    snap3mask = Image.open(appsnext_file)
    snap3 = snap3mask.convert("RGB")
    snapshot.paste(snap3, (553, 198), snap3mask)
    snap7mask = Image.open(appslisthover_file)
    snap7 = snap7mask.convert("RGB")
    snapshot.paste(snap7, (104, 58), snap7mask)
    snap8mask = Image.open(appslist_file)
    snap8 = snap8mask.convert("RGB")
    snapshot.paste(snap8, (104, 128), snap8mask) #create multiple...
    snapshot.paste(snap8, (104, 198), snap8mask)
    snapshot.paste(snap8, (104, 268), snap8mask)
    snapshot.paste(snap8, (104, 338), snap8mask)
    snap9mask = Image.open(networkicon_file)
    snap9 = snap9mask.convert("RGB")
    snapshot.paste(snap9, (579, 414), snap9mask)
    snap10mask = Image.open(geckoicon_file)
    snap10 = snap10mask.convert("RGB")
    snapshot.paste(snap10, (544, 414), snap10mask)
    snap11mask = Image.open("transtext.png")
    snap11 = snap11mask.convert("RGB")
    snapshot.paste(snap11, (0, 0), snap11mask)
    snap12mask = Image.open(os.path.join(programpath, "hbc.png"))
    snap12 = snap12mask.convert("RGB")
    snapshot.paste(snap12, (30, 418), snap12mask)

    # appdb images
    if use_ap_images == True:
        appdb_file = (config.get("Files", "application database"))
        # open appdb file
        config.read(os.path.join(programpath, appdb_file))
        # set images to use
        app_image1 = config.get("Images", "image1")
        app_image2 = config.get("Images", "image2")
        app_image3 = config.get("Images", "image3")
        app_image4 = config.get("Images", "image4")
        app_image5 = config.get("Images", "image5")
        # start pasting images
        snap13mask = Image.open(os.path.join(programpath, app_image1))
        snap13 = snap13mask.convert("RGB")
        snapshot.paste(snap13, (115, 65), snap13mask)
        snap14mask = Image.open(os.path.join(programpath, app_image2))
        snap14 = snap14mask.convert("RGB")
        snapshot.paste(snap14, (115, 135), snap14mask)
        snap15mask = Image.open(os.path.join(programpath, app_image3))
        snap15 = snap15mask.convert("RGB")
        snapshot.paste(snap15, (115, 205), snap15mask)
        snap16mask = Image.open(os.path.join(programpath, app_image4))
        snap16 = snap16mask.convert("RGB")
        snapshot.paste(snap16, (115, 275)) #for some reason this image corrupts the screenshot if pasted with its mask...
        snap17mask = Image.open(os.path.join(programpath, app_image5))
        snap17 = snap17mask.convert("RGB")
        snapshot.paste(snap17, (115, 345), snap17mask)
        

    snapshot.save("screenshot1.png", "PNG") #save the image at last!
    if consoleoutput == "yes":
        print "Screenshot saved."


# Grid View (4:3) Themeshot save
def genscreen2():
    if consoleoutput == "yes":
        print "Generating screenshot..."
    os.chdir(originalpath) #cd to original dir to create file
    snapshot = Image.new("RGBA", (640, 480)) #create new image
    snap1 = Image.open(background_file) #open background
    snapshot.paste(snap1, (0, 0)) #place background

    # bubbles have been moved to ensure they remain behind all other objects
    snap4mask = Image.open(bubble1_file)
    snap4_1mask = snap4mask.rotate(BubbleLocation.rot1, Image.BICUBIC, expand=True)
    snap4_1mask = snap4_1mask.resize((BubbleLocation.size1, BubbleLocation.size1), Image.BICUBIC)
    snap4_1 = snap4_1mask.convert("RGB")
    #snapshot.paste(snap4, (73, 303), snap4mask)
    genscreen_pos1 = tuple(map(operator.sub,BubbleLocation.pos1,(snap4_1.size[0]/2,snap4_1.size[1]/2))) #Coordinate system differences between the window and the saved file mean that the position needs to be altered. This code calculates the adjustment to be made (half the image size as a tuple) and via sorcery adds the original pos1 tuple to the half-size tuple. WTF!?
    snapshot.paste(snap4_1, genscreen_pos1, snap4_1mask) #random bubble placement
    snap4_2mask = snap4mask.rotate(BubbleLocation.rot2, Image.BICUBIC, expand=True)
    snap4_2mask = snap4_2mask.resize((BubbleLocation.size2, BubbleLocation.size2), Image.BICUBIC)
    snap4_2 = snap4_2mask.convert("RGB")
    genscreen_pos2 = tuple(map(operator.sub,BubbleLocation.pos2,(snap4_2.size[0]/2,snap4_1.size[1]/2)))
    snapshot.paste(snap4_2, genscreen_pos2, snap4_2mask)
    snap5mask = Image.open(bubble2_file)
    snap5_1mask = snap5mask.rotate(BubbleLocation.rot3, Image.BICUBIC, expand=True)
    snap5_1mask = snap5_1mask.resize((BubbleLocation.size3, BubbleLocation.size3), Image.BICUBIC)
    snap5_1 = snap5_1mask.convert("RGB")
    genscreen_pos3 = tuple(map(operator.sub,BubbleLocation.pos3,(snap5_1.size[0]/2,snap4_1.size[1]/2)))
    snapshot.paste(snap5_1, genscreen_pos3, snap5_1mask)
    snap5_2mask = snap5mask.rotate(BubbleLocation.rot4, Image.BICUBIC, expand=True)
    snap5_2mask = snap5_2mask.resize((BubbleLocation.size4, BubbleLocation.size4), Image.BICUBIC)
    snap5_2 = snap5_2mask.convert("RGB")
    genscreen_pos4 = tuple(map(operator.sub,BubbleLocation.pos4,(snap5_2.size[0]/2,snap4_1.size[1]/2)))
    snapshot.paste(snap5_2, genscreen_pos4, snap5_2mask)
    snap6mask = Image.open(bubble3_file)
    snap6_1mask = snap6mask.rotate(BubbleLocation.rot5, Image.BICUBIC, expand=True)
    snap6_1mask = snap6_1mask.resize((BubbleLocation.size5, BubbleLocation.size5), Image.BICUBIC)
    snap6_1 = snap6_1mask.convert("RGB")
    genscreen_pos5 = tuple(map(operator.sub,BubbleLocation.pos5,(snap6_1.size[0]/2,snap4_1.size[1]/2)))
    snapshot.paste(snap6_1, genscreen_pos5, snap6_1mask) #random bubble placement
    snap6_2mask = snap6mask.rotate(BubbleLocation.rot6, Image.BICUBIC, expand=True)
    snap6_2mask = snap6_2mask.resize((BubbleLocation.size6, BubbleLocation.size6), Image.BICUBIC)
    snap6_2 = snap6_2mask.convert("RGB")
    genscreen_pos6 = tuple(map(operator.sub,BubbleLocation.pos6,(snap6_2.size[0]/2,snap4_1.size[1]/2)))
    snapshot.paste(snap6_2, genscreen_pos6, snap6_2mask)

    snap2mask = Image.open(appsprev_file) #use image as mask
    snap2 = snap2mask.convert("RGB") #create RGB version
    snapshot.paste(snap2, (23, 198), snap2mask) #place image, using RGB and mask to avoid alpha problems...
    snap3mask = Image.open(appsnext_file)
    snap3 = snap3mask.convert("RGB")
    snapshot.paste(snap3, (553, 198), snap3mask)
    snap7mask = Image.open(appsgridhover_file)
    snap7 = snap7mask.convert("RGB")
    snapshot.paste(snap7, (108, 64), snap7mask)
    snap8mask = Image.open(appsgrid_file)
    snap8 = snap8mask.convert("RGB")
    snapshot.paste(snap8, (250, 64), snap8mask) #create multiple...
    snapshot.paste(snap8, (392, 64), snap8mask)
    snapshot.paste(snap8, (108, 128), snap8mask)
    snapshot.paste(snap8, (250, 128), snap8mask)
    snapshot.paste(snap8, (392, 128), snap8mask)
    snapshot.paste(snap8, (108, 192), snap8mask)
    snapshot.paste(snap8, (250, 192), snap8mask)
    snapshot.paste(snap8, (392, 192), snap8mask)
    snapshot.paste(snap8, (108, 256), snap8mask)
    snapshot.paste(snap8, (250, 256), snap8mask)
    snapshot.paste(snap8, (392, 256), snap8mask)
    snapshot.paste(snap8, (108, 320), snap8mask)
    snapshot.paste(snap8, (250, 320), snap8mask)
    snapshot.paste(snap8, (392, 320), snap8mask)
    snap9mask = Image.open(networkicon_file)
    snap9 = snap9mask.convert("RGB")
    snapshot.paste(snap9, (579, 414), snap9mask)
    snap10mask = Image.open(geckoicon_file)
    snap10 = snap10mask.convert("RGB")
    snapshot.paste(snap10, (544, 414), snap10mask)
    snap12mask = Image.open(os.path.join(programpath, "hbc.png"))
    snap12 = snap12mask.convert("RGB")
    snapshot.paste(snap12, (30, 418), snap12mask)

    # appdb images
    if use_ap_images == True:
        appdb_file = (config.get("Files", "application database"))
        # open appdb file
        config.read(os.path.join(programpath, appdb_file))
        # set images to use
        app_image1 = config.get("Images", "image1")
        app_image2 = config.get("Images", "image2")
        app_image3 = config.get("Images", "image3")
        app_image4 = config.get("Images", "image4")
        app_image5 = config.get("Images", "image5")
        # start pasting images
        snap13mask = Image.open(os.path.join(programpath, app_image1))
        snap13 = snap13mask.convert("RGB")
        snapshot.paste(snap13, (116, 72), snap13mask)
        snap14mask = Image.open(os.path.join(programpath, app_image2))
        snap14 = snap14mask.convert("RGB")
        snapshot.paste(snap14, (258, 72), snap14mask)
        snap15mask = Image.open(os.path.join(programpath, app_image3))
        snap15 = snap15mask.convert("RGB")
        snapshot.paste(snap15, (400, 72), snap15mask)
        snap16mask = Image.open(os.path.join(programpath, app_image4))
        snap16 = snap16mask.convert("RGB")
        snapshot.paste(snap16, (116, 136)) #for some reason this image corrupts the screenshot if pasted with its mask...
        snap17mask = Image.open(os.path.join(programpath, app_image5))
        snap17 = snap17mask.convert("RGB")
        snapshot.paste(snap17, (258, 136), snap17mask)
        

    snapshot.save("screenshot2.png", "PNG") #save the image at last!
    if consoleoutput == "yes":
        print "Screenshot saved."


# Preview theme depending on which radiobutton is chosen
def previewtheme():

    if consoleoutput == "yes":
        print "Opening theme zip file..."

    # open zipfile, extract contents to original directory...error with folders?
    os.chdir(originalpath) #return to original directory
    global themefile
    themefile = filepath.get("1.0", "end").rstrip("\n") #gets themefile from filepath box, strips trailing \n
    zf = zipfile.ZipFile(themefile, "r")

    # original code replaced with extractall method to actually extract directories...some issues with extractall vs outfile.write?

    #for name in zf.namelist():
    #    outfile = open(name, "wb")
    #    outfile.write(zf.read(name))
    #    outfile.close()

    if consoleoutput == "yes":
        print "Extracting theme zip file..."

    zf.extractall(originalpath)

    if consoleoutput == "yes":
        print "Checking if all required files exist..."

    # test if files exist, if not, use dark water theme replacements
    global appsprev_file
    if os.path.exists("apps_previous.png") == True:
        appsprev_file = "apps_previous.png"
    else:
        appsprev_file = os.path.join(replacement_theme_path, "apps_previous.png")
    global appsnext_file
    if os.path.exists("apps_next.png") == True:
        appsnext_file = "apps_next.png"
    else:
        appsnext_file = os.path.join(replacement_theme_path, "apps_next.png")
    global bubble1_file
    if os.path.exists("bubble1.png") == True:
        bubble1_file = "bubble1.png"
    else:
        bubble1_file = os.path.join(replacement_theme_path, "bubble1.png")
    global bubble2_file
    if os.path.exists("bubble2.png") == True:
        bubble2_file = "bubble2.png"
    else:
        bubble2_file = os.path.join(replacement_theme_path, "bubble2.png")
    global bubble3_file
    if os.path.exists("bubble3.png") == True:
        bubble3_file = "bubble3.png"
    else:
        bubble3_file = os.path.join(replacement_theme_path, "bubble3.png")
    global appslisthover_file
    if os.path.exists("apps_list_hover.png") == True:
        appslisthover_file = "apps_list_hover.png"
    else:
        appslisthover_file = os.path.join(replacement_theme_path, "apps_list_hover.png")
    global appslist_file
    if os.path.exists("apps_list.png") == True:
        appslist_file = "apps_list.png"
    else:
        appslist_file = os.path.join(replacement_theme_path, "apps_list.png")
    global appsgridhover_file
    if os.path.exists("apps_grid_hover.png") == True:
        appsgridhover_file = "apps_grid_hover.png"
    else:
        appsgridhover_file = os.path.join(replacement_theme_path, "apps_grid_hover.png")
    global appsgrid_file
    if os.path.exists("apps_grid.png") == True:
        appsgrid_file = "apps_grid.png"
    else:
        appsgrid_file = os.path.join(replacement_theme_path, "apps_grid.png")
    global networkicon_file
    if os.path.exists("icon_network_active.png") == True:
        networkicon_file = "icon_network_active.png"
    else:
        networkicon_file = os.path.join(replacement_theme_path, "icon_network_active.png")
    global geckoicon_file
    if os.path.exists("icon_usbgecko_active.png") == True:
        geckoicon_file = "icon_usbgecko_active.png"
    else:
        geckoicon_file = os.path.join(replacement_theme_path, "icon_usbgecko_active.png")
    global background_file
    if os.path.exists("background.png") == True:
        background_file = "background.png"
    else:
        background_file = os.path.join(replacement_theme_path, "background.png")

    # setup font colours
    redvalue = linecache.getline("theme.xml", 5)
    redvalue = int(re.sub("\D", "", redvalue))
    greenvalue = linecache.getline("theme.xml", 6)
    greenvalue = int(re.sub("\D", "", greenvalue))
    bluevalue = linecache.getline("theme.xml", 7)
    bluevalue = int(re.sub("\D", "", bluevalue))
    alphavalue = linecache.getline("theme.xml", 8) 
    alphavalue = int(re.sub("\D", "", alphavalue))
    fontcolour = (redvalue, greenvalue, bluevalue) # sets RGB colour
    hexcolour = '#%02x%02x%02x' % fontcolour # converts RGB colour to hex
    decalpha = Decimal(alphavalue) / Decimal(255) # converts alphavalue to decimal
    linecache.clearcache() #this fixes the issue with transtext.png. Method of reading theme.xml stores a cache which needs to be cleared when a different theme.xml is loaded.

    if consoleoutput == "yes":
        print "Text - HEX:", hexcolour, ", RGB:", fontcolour

    # chosen font
    fontfile = os.path.join(programpath, "LiberationSans-Bold.ttf")

    # create lorem ipsum list
    lorem_lines = ["Lorem ipsum", "dolor sit amet consectetuer", "adipiscing elit.", "Aenean commodo ligula eget dolor.", "Aenean massa.", "Cum sociis natoque penatibus", "et magnis dis", "parturient montes, nascetur", "ridiculus mus.", "Donec quam felis, ultricies nec"]

    # use lorem ipsum dummy text or...
    if config.get("Text", "dummy text") == "yes":
        text_lines = lorem_lines
        if consoleoutput == "yes":
            print "Using lorem ipsum dummy text..."

    # use appdb text
    elif config.get("Text", "dummy text") == "no":
        appdb_file = (config.get("Files", "application database"))
        if consoleoutput == "yes":
            print "Using appdb text..."
        # show error if appdb file can't be found and default to lorem ipsum
        if os.path.isfile(os.path.join(programpath, appdb_file)) == False:
            showerror("Invalid or missing database", "The current setting for the application database is incorrect or the database is missing. Defaulting to lorem ipsum dummy text...")
            text_lines = lorem_lines
        # if appdb file can be found, use it
        elif os.path.isfile(os.path.join(programpath, appdb_file)) == True:
            # open appdb file
            config.read(os.path.join(programpath, appdb_file))
            # sort out text
            appdb_lines=[]
            appdb_lines.append(config.get("Text", "title1"))
            appdb_lines.append(config.get("Text", "description1"))
            appdb_lines.append(config.get("Text", "title2"))
            appdb_lines.append(config.get("Text", "description2"))
            appdb_lines.append(config.get("Text", "title3"))
            appdb_lines.append(config.get("Text", "description3"))
            appdb_lines.append(config.get("Text", "title4"))
            appdb_lines.append(config.get("Text", "description4"))
            appdb_lines.append(config.get("Text", "title5"))
            appdb_lines.append(config.get("Text", "description5"))
            text_lines = appdb_lines

    # if settings are incorrect, corrupted or deleted...
    else:
        showerror("Invalid dummy text setting", "The current setting for dummy text is incorrect. Defaulting to lorem ipsum text...")
        text_lines = lorem_lines

    if consoleoutput == "yes":
        print "Generating transtext.png..."

    # position, text, colour, size of dummy text
    dummy_data = [
        ((260, 65), text_lines[0], hexcolour, 16),
        ((260, 95), text_lines[1], hexcolour, 16),
        ((260, 135), text_lines[2], hexcolour, 16),
        ((260, 165), text_lines[3], hexcolour, 16),
        ((260, 205), text_lines[4], hexcolour, 16),
        ((260, 235), text_lines[5], hexcolour, 16),
        ((260, 275), text_lines[6], hexcolour, 16),
        ((260, 305), text_lines[7], hexcolour, 16),
        ((260, 345), text_lines[8], hexcolour, 16),
        ((260, 375), text_lines[9], hexcolour, 16),
        ]

    # create fully transparent image + alpha channel
    ttf_image = Image.new("RGB", (640, 480), (0,0,0))
    alpha = Image.new("L", ttf_image.size, "black")

    for pos, text, colour, size in dummy_data:

        # Make a grayscale image of the font, white on black.
        imagetext = Image.new("L", ttf_image.size, 0)
        drawtext = ImageDraw.Draw(imagetext)
        font = ImageFont.truetype(fontfile, size)
        drawtext.text(pos, text, font=font, fill="white")
        
        # Add the white text to our collected alpha channel. Gray pixels around
        # the edge of the text will eventually become partially transparent
        # pixels in the alpha channel.
        alpha = ImageChops.lighter(alpha, imagetext)
    
        # Make a solid color, and add it to the colour layer on every pixel
        # that has even a little bit of alpha showing.
        solidcolour = Image.new("RGBA", ttf_image.size, colour)
        imagemask = Image.eval(imagetext, lambda p: 255 * (int(p != 0)))
        ttf_image = Image.composite(solidcolour, ttf_image, imagemask)

    # Add the alpha channel to the image, set text transparency, then save
    ttf_image.putalpha(alpha)
    alpha2 = ttf_image.split()[3]
    alpha2 = ImageEnhance.Brightness(alpha2).enhance(decalpha)
    ttf_image.putalpha(alpha2)
    # image.save doesn't overwrite existing images it seems, so we have to remove any previous transtext files if they exist
    if os.path.exists("transtext.png") == True:
        os.remove("transtext.png")
    ttf_image.save("transtext.png", "PNG")

    if consoleoutput == "yes":
        print "transtext.png saved."

    # Determine which view to use
    if radio.pressed1 == 1:
        previewtheme1()
    elif radio.pressed2 == 1:
        previewtheme2()
    #elif radio.pressed3 == 1:
    #    previewtheme3()

    # create screenshot button
    #screenshot = Button(root, text="Generate Screenshot", command=genscreen)
    #screenshot.grid(row=2, columnspan=3, pady=5, padx=5)
    global SaveButtonExists
    if SaveButtonExists == 0:
        b3 = c2.create_image(35, 43, image=b1_photo)
        t3 = c2.create_text(35, 43, text="Save")
        def mousepress3(event):
            c2.itemconfig(b3, image=b1_photo_press)
            genscreen()
        def mouseover3(event):
            c2.itemconfig(b3, image=b1_photo_hover)
        def mouseoff3(event):
            c2.itemconfig(b3, image=b1_photo)
        def mouserelease3(event):
            c2.itemconfig(b3, image=b1_photo)
        c2.tag_bind(b3, "<Button-1>", mousepress3)
        c2.tag_bind(b3, "<Enter>", mouseover3)
        c2.tag_bind(b3, "<Leave>", mouseoff3)
        c2.tag_bind(b3, "<ButtonRelease-1>", mouserelease3)
        c2.tag_bind(t3, "<Button-1>", mousepress3)
        c2.tag_bind(t3, "<Enter>", mouseover3)
        c2.tag_bind(t3, "<Leave>", mouseoff3)
        c2.tag_bind(t3, "<ButtonRelease-1>", mouserelease3)
    SaveButtonExists = 1


# List View (4:3) Themeshot preview
def previewtheme1():

    if consoleoutput == "yes":
        print "Drawing preview window..."

    # setup preview window
    preview = Toplevel()
    preview.title("Theme Preview: List View (4:3)")
    
    # setup canvas and background
    os.chdir(originalpath) #return to original dir
    image1 = Image.open(background_file)
    image1 = ImageTk.PhotoImage(image1)
    background = Label(preview, image=image1)
    background.image = image1
    width1 = image1.width()
    height1 = image1.height()
    canvas =  Canvas(preview, width=width1, height=height1, highlightthickness=0) #highlighthickness set to avoid borders around preview
    canvas.pack()
    x = (width1)/2.0
    y = (height1)/2.0
    canvas.create_image(x, y, image=image1)

    # setup other images
    # bubbles have been moved to keep them behind other objects    
    image4 = Image.open(bubble1_file)
    image4_1 = image4.rotate(BubbleLocation.rot1, Image.BICUBIC, expand=True)
    image4_1 = image4_1.resize((BubbleLocation.size1, BubbleLocation.size1), Image.BICUBIC)
    image4_1 = ImageTk.PhotoImage(image4_1)
    bubble1_1 = Label(preview, image=image4_1)
    bubble1_1.image = image4_1
    #canvas.create_image(105, 335, image=image4)
    canvas.create_image(BubbleLocation.pos1, image=image4_1) #random bubble placement
    image4_2 = image4.rotate(BubbleLocation.rot2, Image.BICUBIC, expand=True)
    image4_2 = image4_2.resize((BubbleLocation.size2, BubbleLocation.size2), Image.BICUBIC)
    image4_2 = ImageTk.PhotoImage(image4_2)
    bubble1_2 = Label(preview, image=image4_2)
    bubble1_2.image = image4_2
    canvas.create_image(BubbleLocation.pos2, image=image4_2)

    image5 = Image.open(bubble2_file)
    image5_1 = image5.rotate(BubbleLocation.rot3, Image.BICUBIC, expand=True)
    image5_1 = image5_1.resize((BubbleLocation.size3, BubbleLocation.size3), Image.BICUBIC)
    image5_1 = ImageTk.PhotoImage(image5_1)
    bubble2_1 = Label(preview, image=image5_1)
    bubble2_1.image = image5_1
    #canvas.create_image(500, 145, image=image5)
    canvas.create_image(BubbleLocation.pos3, image=image5_1)
    image5_2 = image5.rotate(BubbleLocation.rot4, Image.BICUBIC, expand=True)
    image5_2 = image5_2.resize((BubbleLocation.size4, BubbleLocation.size4), Image.BICUBIC)
    image5_2 = ImageTk.PhotoImage(image5_2)
    bubble2_2 = Label(preview, image=image5_2)
    bubble2_2.image = image5_2
    canvas.create_image(BubbleLocation.pos4, image=image5_2)

    image6 = Image.open(bubble3_file)
    image6_1 = image6.rotate(BubbleLocation.rot5, Image.BICUBIC, expand=True)
    image6_1 = image6_1.resize((BubbleLocation.size5, BubbleLocation.size5), Image.BICUBIC)
    image6_1 = ImageTk.PhotoImage(image6_1)
    bubble3_1 = Label(preview, image=image6_1)
    bubble3_1.image = image6_1
    canvas.create_image(BubbleLocation.pos5, image=image6_1)
    image6_2 = image6.rotate(BubbleLocation.rot6, Image.BICUBIC, expand=True)
    image6_2 = image6_2.resize((BubbleLocation.size6, BubbleLocation.size6), Image.BICUBIC)
    image6_2 = ImageTk.PhotoImage(image6_2)
    bubble3_2 = Label(preview, image=image6_2)
    bubble3_2.image = image6_2
    canvas.create_image(BubbleLocation.pos6, image=image6_2)

    image2 = Image.open(appsprev_file)
    image2 = ImageTk.PhotoImage(image2)
    apps_previous = Label(preview, image=image2)
    apps_previous.image = image2
    canvas.create_image(55, 220, image=image2)
    
    image3 = Image.open(appsnext_file)
    image3 = ImageTk.PhotoImage(image3)
    apps_next = Label(preview, image=image3)
    apps_next.image = image3
    canvas.create_image(585, 220, image=image3)

    image7 = Image.open(appslisthover_file)
    image7 = ImageTk.PhotoImage(image7)
    apps_list_hover = Label(preview, image=image7)
    apps_list_hover.image = image7
    canvas.create_image(320, 90, image=image7)

    image8 = Image.open(appslist_file)
    image8 = ImageTk.PhotoImage(image8)
    apps_list = Label(preview, image=image8)
    apps_list.image = image8
    canvas.create_image(320, 160, image=image8)
    canvas.create_image(320, 230, image=image8)
    canvas.create_image(320, 300, image=image8)
    canvas.create_image(320, 370, image=image8)

    image9 = Image.open(networkicon_file)
    image9 = ImageTk.PhotoImage(image9)
    icon_network_active = Label(preview, image=image9)
    icon_network_active.image = image9
    canvas.create_image(595, 430, image=image9)

    image10 = Image.open(geckoicon_file)
    image10 = ImageTk.PhotoImage(image10)
    icon_usbgecko_active = Label(preview, image=image10)
    icon_usbgecko_active.image = image10
    canvas.create_image(560, 430, image=image10)

    global use_ap_images
    use_ap_images = False

    # re-open settings file to check for appdb images settings
    config.read(os.path.join(programpath, "settings"))
    if config.get("Images", "appdb images") == "yes":
        appdb_file = (config.get("Files", "application database"))
        if consoleoutput == "yes":
            print "Using appdb images..."

        # show error if appdb file can't be found
        if os.path.isfile(os.path.join(programpath, appdb_file)) == False:
            showerror("Invalid or missing database", "The current setting for the application database is incorrect or the database is missing. Application images will not be used...")

        # if appdb file can be found, use it
        elif os.path.isfile(os.path.join(programpath, appdb_file)) == True:
            # open appdb file
            config.read(os.path.join(programpath, appdb_file))
            # set images to use
            app_image1 = config.get("Images", "image1")
            app_image2 = config.get("Images", "image2")
            app_image3 = config.get("Images", "image3")
            app_image4 = config.get("Images", "image4")
            app_image5 = config.get("Images", "image5")

            # place images on canvas
            image13 = Image.open(os.path.join(programpath, app_image1))
            image13 = ImageTk.PhotoImage(image13)
            app1 = Label(preview, image=image13)
            app1.image = image13
            canvas.create_image(180, 90, image=image13)
            image14 = Image.open(os.path.join(programpath, app_image2))
            image14 = ImageTk.PhotoImage(image14)
            app2 = Label(preview, image=image14)
            app2.image = image14
            canvas.create_image(180, 160, image=image14)
            image15 = Image.open(os.path.join(programpath, app_image3))
            image15 = ImageTk.PhotoImage(image15)
            app3 = Label(preview, image=image15)
            app3.image = image15
            canvas.create_image(180, 230, image=image15)
            image16 = Image.open(os.path.join(programpath, app_image4))
            image16 = ImageTk.PhotoImage(image16)
            app4 = Label(preview, image=image16)
            app4.image = image16
            canvas.create_image(180, 300, image=image16)
            image17 = Image.open(os.path.join(programpath, app_image5))
            image17 = ImageTk.PhotoImage(image17)
            app5 = Label(preview, image=image17)
            app5.image = image17
            canvas.create_image(180, 370, image=image17)
            use_ap_images = True

        # if settings are incorrect, corrupted or deleted...
        else:
            showerror("Invalid images setting", "The current setting for application images is incorrect. Application images will not be used...")

    # place transtext image on canvas
    image11 = Image.open("transtext.png")
    image11 = ImageTk.PhotoImage(image11)
    dummytext = Label(preview, image=image11)
    dummytext.image = image11
    canvas.create_image(320, 240, image=image11)

    # finally insert homebrew channel logo
    image12 = Image.open(os.path.join(programpath, "hbc.png"))
    image12 = ImageTk.PhotoImage(image12)
    hbc = Label(preview, image=image12)
    hbc.image = image12
    canvas.create_image(160, 430, image=image12)

    # preview window cannot be resized
    preview.resizable(0,0)

    if consoleoutput == "yes":
        print "Preview window done!"

    # start preview window
    preview.mainloop


# Grid View (4:3) Themeshot preview
def previewtheme2():

    if consoleoutput == "yes":
        print "Drawing preview window..."

    # setup preview window
    preview = Toplevel()
    preview.title("Theme Preview: Grid View (4:3)")
    
    # setup canvas and background
    os.chdir(originalpath) #return to original dir
    image1 = Image.open(background_file)
    image1 = ImageTk.PhotoImage(image1)
    background = Label(preview, image=image1)
    background.image = image1
    width1 = image1.width()
    height1 = image1.height()
    canvas =  Canvas(preview, width=width1, height=height1, highlightthickness=0) #highlighthickness set to avoid borders around preview
    canvas.pack()
    x = (width1)/2.0
    y = (height1)/2.0
    canvas.create_image(x, y, image=image1)

    # setup other images
    # bubbles have been moved to keep them behind other objects    
    image4 = Image.open(bubble1_file)
    image4_1 = image4.rotate(BubbleLocation.rot1, Image.BICUBIC, expand=True)
    image4_1 = image4_1.resize((BubbleLocation.size1, BubbleLocation.size1), Image.BICUBIC)
    image4_1 = ImageTk.PhotoImage(image4_1)
    bubble1_1 = Label(preview, image=image4_1)
    bubble1_1.image = image4_1
    #canvas.create_image(105, 335, image=image4)
    canvas.create_image(BubbleLocation.pos1, image=image4_1) #random bubble placement
    image4_2 = image4.rotate(BubbleLocation.rot2, Image.BICUBIC, expand=True)
    image4_2 = image4_2.resize((BubbleLocation.size2, BubbleLocation.size2), Image.BICUBIC)
    image4_2 = ImageTk.PhotoImage(image4_2)
    bubble1_2 = Label(preview, image=image4_2)
    bubble1_2.image = image4_2
    canvas.create_image(BubbleLocation.pos2, image=image4_2)

    image5 = Image.open(bubble2_file)
    image5_1 = image5.rotate(BubbleLocation.rot3, Image.BICUBIC, expand=True)
    image5_1 = image5_1.resize((BubbleLocation.size3, BubbleLocation.size3), Image.BICUBIC)
    image5_1 = ImageTk.PhotoImage(image5_1)
    bubble2_1 = Label(preview, image=image5_1)
    bubble2_1.image = image5_1
    #canvas.create_image(500, 145, image=image5)
    canvas.create_image(BubbleLocation.pos3, image=image5_1)
    image5_2 = image5.rotate(BubbleLocation.rot4, Image.BICUBIC, expand=True)
    image5_2 = image5_2.resize((BubbleLocation.size4, BubbleLocation.size4), Image.BICUBIC)
    image5_2 = ImageTk.PhotoImage(image5_2)
    bubble2_2 = Label(preview, image=image5_2)
    bubble2_2.image = image5_2
    canvas.create_image(BubbleLocation.pos4, image=image5_2)

    image6 = Image.open(bubble3_file)
    image6_1 = image6.rotate(BubbleLocation.rot5, Image.BICUBIC, expand=True)
    image6_1 = image6_1.resize((BubbleLocation.size5, BubbleLocation.size5), Image.BICUBIC)
    image6_1 = ImageTk.PhotoImage(image6_1)
    bubble3_1 = Label(preview, image=image6_1)
    bubble3_1.image = image6_1
    canvas.create_image(BubbleLocation.pos5, image=image6_1)
    image6_2 = image6.rotate(BubbleLocation.rot6, Image.BICUBIC, expand=True)
    image6_2 = image6_2.resize((BubbleLocation.size6, BubbleLocation.size6), Image.BICUBIC)
    image6_2 = ImageTk.PhotoImage(image6_2)
    bubble3_2 = Label(preview, image=image6_2)
    bubble3_2.image = image6_2
    canvas.create_image(BubbleLocation.pos6, image=image6_2)
    
    image3 = Image.open(appsnext_file)
    image3 = ImageTk.PhotoImage(image3)
    apps_next = Label(preview, image=image3)
    apps_next.image = image3
    canvas.create_image(585, 223, image=image3)

    image7 = Image.open(appsgridhover_file)
    image7 = ImageTk.PhotoImage(image7)
    apps_grid_hover = Label(preview, image=image7)
    apps_grid_hover.image = image7
    canvas.create_image(179, 95, image=image7)

    image8 = Image.open(appsgrid_file)
    image8 = ImageTk.PhotoImage(image8)
    apps_grid = Label(preview, image=image8)
    apps_grid.image = image8
    canvas.create_image(322, 96, image=image8)
    canvas.create_image(464, 96, image=image8)
    canvas.create_image(180, 160, image=image8)
    canvas.create_image(322, 160, image=image8)
    canvas.create_image(464, 160, image=image8)
    canvas.create_image(180, 224, image=image8)
    canvas.create_image(322, 224, image=image8)
    canvas.create_image(464, 224, image=image8)
    canvas.create_image(180, 288, image=image8)
    canvas.create_image(322, 288, image=image8)
    canvas.create_image(464, 288, image=image8)
    canvas.create_image(180, 352, image=image8)
    canvas.create_image(322, 352, image=image8)
    canvas.create_image(464, 352, image=image8)

    image9 = Image.open(networkicon_file)
    image9 = ImageTk.PhotoImage(image9)
    icon_network_active = Label(preview, image=image9)
    icon_network_active.image = image9
    canvas.create_image(595, 430, image=image9)

    image10 = Image.open(geckoicon_file)
    image10 = ImageTk.PhotoImage(image10)
    icon_usbgecko_active = Label(preview, image=image10)
    icon_usbgecko_active.image = image10
    canvas.create_image(560, 430, image=image10)

    global use_ap_images
    use_ap_images = False

    # re-open settings file to check for appdb images settings
    config.read(os.path.join(programpath, "settings"))
    if config.get("Images", "appdb images") == "yes":
        appdb_file = (config.get("Files", "application database"))
        if consoleoutput == "yes":
            print "Using appdb images..."

        # show error if appdb file can't be found
        if os.path.isfile(os.path.join(programpath, appdb_file)) == False:
            showerror("Invalid or missing database", "The current setting for the application database is incorrect or the database is missing. Application images will not be used...")

        # if appdb file can be found, use it
        elif os.path.isfile(os.path.join(programpath, appdb_file)) == True:
            # open appdb file
            config.read(os.path.join(programpath, appdb_file))
            # set images to use
            app_image1 = config.get("Images", "image1")
            app_image2 = config.get("Images", "image2")
            app_image3 = config.get("Images", "image3")
            app_image4 = config.get("Images", "image4")
            app_image5 = config.get("Images", "image5")

            # place images on canvas
            image13 = Image.open(os.path.join(programpath, app_image1))
            image13 = ImageTk.PhotoImage(image13)
            app1 = Label(preview, image=image13)
            app1.image = image13
            canvas.create_image(181, 97, image=image13)
            image14 = Image.open(os.path.join(programpath, app_image2))
            image14 = ImageTk.PhotoImage(image14)
            app2 = Label(preview, image=image14)
            app2.image = image14
            canvas.create_image(323, 97, image=image14)
            image15 = Image.open(os.path.join(programpath, app_image3))
            image15 = ImageTk.PhotoImage(image15)
            app3 = Label(preview, image=image15)
            app3.image = image15
            canvas.create_image(465, 97, image=image15)
            image16 = Image.open(os.path.join(programpath, app_image4))
            image16 = ImageTk.PhotoImage(image16)
            app4 = Label(preview, image=image16)
            app4.image = image16
            canvas.create_image(181, 161, image=image16)
            image17 = Image.open(os.path.join(programpath, app_image5))
            image17 = ImageTk.PhotoImage(image17)
            app5 = Label(preview, image=image17)
            app5.image = image17
            canvas.create_image(323, 161, image=image17)
            use_ap_images = True

        # if settings are incorrect, corrupted or deleted...
        else:
            showerror("Invalid images setting", "The current setting for application images is incorrect. Application images will not be used...")

    # finally insert homebrew channel logo
    image12 = Image.open(os.path.join(programpath, "hbc.png"))
    image12 = ImageTk.PhotoImage(image12)
    hbc = Label(preview, image=image12)
    hbc.image = image12
    canvas.create_image(160, 430, image=image12)

    # preview window cannot be resized
    preview.resizable(0,0)

    if consoleoutput == "yes":
        print "Preview window done!"

    # start preview window
    preview.mainloop


# setup contents of root window
label = Label(root, text="Theme.zip: ")
filepath = Text(root, height=1, width=40, highlightthickness=0) #On KDE4 most widgets were surrounded with a strange white box. This appears to be due the focus highlight on such widgets. Setting highlightthickness to 0 solves this issue

# position root window contents
label.grid(row=0, column=0, pady=10, padx=5)
filepath.grid(row=0, column=1, pady=10)
#browse.grid(row=0, column=2, pady=10, padx=5)
#preview.grid(row=1, columnspan=3, pady=5, padx=5)

# custom buttons code - uses Orta GTK theme buttons

# setup canvas for browse button
c = Canvas(root, width=70, height=28, highlightthickness=0)
c.grid(row=0, column=2, pady=10, padx=5)

# PIL image handling
b1_image = Image.open(os.path.join(programpath, "button-normal.png"))
b1_photo = ImageTk.PhotoImage(b1_image)
b1_image_hover = Image.open(os.path.join(programpath, "button-prelight.png"))
b1_photo_hover = ImageTk.PhotoImage(b1_image_hover)
b1_image_press = Image.open(os.path.join(programpath, "button-pressed-prelight.png"))
b1_photo_press = ImageTk.PhotoImage(b1_image_press)

# create button and text
b1 = c.create_image(35, 14, image=b1_photo)
t1 = c.create_text(35, 14, text="Browse")

# event functions
def mousepress1(event):
    c.itemconfig(b1, image=b1_photo_press)
    choosefile()

def mouseover1(event):
    c.itemconfig(b1, image=b1_photo_hover)

def mouseoff1(event):
    c.itemconfig(b1, image=b1_photo)

def mouserelease1(event):
    c.itemconfig(b1, image=b1_photo)

# bindings for the custom button
c.tag_bind(b1, "<Button-1>", mousepress1)
c.tag_bind(b1, "<Enter>", mouseover1)
c.tag_bind(b1, "<Leave>", mouseoff1)
c.tag_bind(b1, "<ButtonRelease-1>", mouserelease1)

# duplicated for text on top of button
c.tag_bind(t1, "<Button-1>", mousepress1)
c.tag_bind(t1, "<Enter>", mouseover1)
c.tag_bind(t1, "<Leave>", mouseoff1)
c.tag_bind(t1, "<ButtonRelease-1>", mouserelease1)

# Radio Button stuff
c3 = Canvas(root, width=350, height=24, highlightthickness=0)
c3.grid(row=1, columnspan=3, padx=5)

class radio:
    pressed1 = 1
    pressed2 = 0
    #pressed3 = 0

def radiopress1(event):
    if radio.pressed1 == 0:
        c3.itemconfig(Radio1, image=Radio_photo_selected)
        radio.pressed1 = 1
        c3.itemconfig(Radio2, image=Radio_photo)
        radio.pressed2 = 0
        #c3.itemconfig(Radio3, image=Radio_photo)
        #radio.pressed3 = 0

def radiopress2(event):
    if radio.pressed2 == 0:
        c3.itemconfig(Radio1, image=Radio_photo)
        radio.pressed1 = 0
        c3.itemconfig(Radio2, image=Radio_photo_selected)
        radio.pressed2 = 1
        #c3.itemconfig(Radio3, image=Radio_photo)
        #radio.pressed3 = 0

def radiopress3(event):
    if radio.pressed3 == 0:
        c3.itemconfig(Radio1, image=Radio_photo)
        radio.pressed1 = 0
        c3.itemconfig(Radio2, image=Radio_photo)
        radio.pressed2 = 0
        #c3.itemconfig(Radio3, image=Radio_photo_selected)
        #radio.pressed3 = 1

Radio_image = Image.open(os.path.join(programpath, "RadioButton2.png"))
Radio_photo = ImageTk.PhotoImage(Radio_image)
Radio_image_selected = Image.open(os.path.join(programpath, "RadioButton1.png"))
Radio_photo_selected = ImageTk.PhotoImage(Radio_image_selected)

Radio1 = c3.create_image(7, 7, image=Radio_photo_selected)
Radio1Text = c3.create_text(62, 7, text="List View (4:3)")
Radio2 = c3.create_image(247, 7, image=Radio_photo)
Radio2Text = c3.create_text(302, 7, text="Grid View (4:3)")
#Radio3 = c3.create_image(127, 7, image=Radio_photo)
#Radio3Text = c3.create_text(182, 7, text="Radio Button 3")

c3.tag_bind(Radio1, "<Button-1>", radiopress1)
c3.tag_bind(Radio2, "<Button-1>", radiopress2)
#c3.tag_bind(Radio3, "<Button-1>", radiopress3)
c3.tag_bind(Radio1Text, "<Button-1>", radiopress1)
c3.tag_bind(Radio2Text, "<Button-1>", radiopress2)
#c3.tag_bind(Radio3Text, "<Button-1>", radiopress3)

# Preview button code
c2 = Canvas(root, width=70, height=61, highlightthickness=0)
c2.grid(row=2, columnspan=3, padx=5)
b2 = c2.create_image(35, 14, image=b1_photo)
t2 = c2.create_text(35, 14, text="Preview")
def mousepress2(event):
    c2.itemconfig(b2, image=b1_photo_press)
    previewtheme()
def mouseover2(event):
    c2.itemconfig(b2, image=b1_photo_hover)
def mouseoff2(event):
    c2.itemconfig(b2, image=b1_photo)
def mouserelease2(event):
    c2.itemconfig(b2, image=b1_photo)
c2.tag_bind(b2, "<Button-1>", mousepress2)
c2.tag_bind(b2, "<Enter>", mouseover2)
c2.tag_bind(b2, "<Leave>", mouseoff2)
c2.tag_bind(b2, "<ButtonRelease-1>", mouserelease2)
c2.tag_bind(t2, "<Button-1>", mousepress2)
c2.tag_bind(t2, "<Enter>", mouseover2)
c2.tag_bind(t2, "<Leave>", mouseoff2)
c2.tag_bind(t2, "<ButtonRelease-1>", mouserelease2)

# No save button until after Preview
SaveButtonExists = 0

# root window cannot be resized
root.resizable(0,0)

if consoleoutput == "yes":
    print "Root window done!"

# start root window
root.mainloop()


if consoleoutput == "yes":
    print "Performing file cleanup..."

# remove extracted files from current/original directory, AFTER root window has been closed
os.chdir(originalpath)
extractedfiles = zipfile.ZipFile(themefile)
for i in extractedfiles.infolist():
    if os.path.isfile(i.filename): #if file, delete file
        os.remove(i.filename)
    else:
        shutil.rmtree(i.filename) #if folder, delete folder AND contents

os.remove("transtext.png") #then remove transparent text file


if consoleoutput == "yes":
    print "File cleanup done!"
