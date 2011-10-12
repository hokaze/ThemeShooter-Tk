### ThemeShooterTk - By HoKaze ###

ThemeShooterTk is an ugly, hastily written version of ThemeShooter written in python from scratch on a whim, based solely on screenshots from Wiibrew of ThemeShooter. It was created to provide a cross-platform alternative to the original ThemeShooter application and the vastly superior OS X version, ThemeShooterX. 
ThemeShooterTk boasts the beginnings of an application database, bubbles (with random placement, resizing and rotating), both grid view and list view (4:3 only), dummy text support, the ability to show previews in addition to saving screenshots, missing file replacement, config files for some basic settings, custom widgets built from the GTK2 Orta Theme and the KDE Oxygen Theme and a new preferences program.

This version attempts to emulate the original in being easy to use and fairly simple, there's just one python file, this readme, the license, font, a some images. Just make sure that (on UNIX and UNIX-like systems such as Linux) that the file is executable and double click in your favourite file-manager (or run it from your CLI shell of choice, if you prefer)

Windows users can use either this or the original ThemeShooter. The latter is probably less buggy and easier for you guys to run as it has less requirements, but I believe at this point I can boast more features ;)
OS X users will want to use ThemeShooterX instead of this as it has a lot more features, putting us all to shame. At the time of this README revision the download links for it don't work, so I guess you're stuck with ThemeShooterTk for now...

This program should work on any modern Windows, Linux or OS X machine (plus quite a few other OSes, in theory) as long as they meet the requirements below:

##Requirements:##
Python 2.x (Python 2.6 and 2.7 should work fine)
- Tkinter (should come with python)
- Python Imaging Library, PIL (Tends to be included with python)
- PIL: ImageTk Module (on Linux this tends to be kept seperate, look for the "python-imaging-tk" package)

##Todo list:##
- Better commenting and explanations
- Rejection of incorrectly-sized images?
- Widescreen support?
- Fix image mask bug with some application images when saving screenshots
- More bug testing! >.<;
- *Seriously, code needs cleaning up at somepoint, this is a horrible mess!*
- More bubbles?
- Less sorcery and arcane rituals invoked by the program...?

##Changelog:##
v0.11
Implemented a new, experimental preferences program. This allows you to set some of the settings without having to manually edit the files (trust me though, they are easy to understand and do manually...I hope). I've yet to add a way of launching it into the main program but you can run it seperately for now. I might add options for the appdb file in the future, but this may prove different.
Remember the bubble placment bug I mentioned for v0.11? This bug has, after much difficulty, been partially fixed: bubble placement is still a good few pixels off, but not to the same extent that it was. I suspect the resizing and rotating may also be causing issues here.
More README.txt tweaking.
Fixed a bug on KDE (and possibly other platforms) that meant most widgets were surrounded by a white bounding box. Found bug with windows version of PIL: appears that some official binaries don't have working font support. Using an unofficial build solves the problem.
Fixed bug regarding custom widget elements that caused program to crash on startup.


v0.10 [No public release]
Finally got around to implementing resizing and rotations. Rotations are between 45 clockwise and 45 counter-clockwise, sizes vary between 0.5x original size and 1.5x original size.
Fixed bug with the save button that created multiple, stacked instances of the button.
Noticed bug with bubble positions being slightly offset in the saved screenshots versus the previews. This is due to image coordinates working differently with images placed on the window and images placed into a file. Looking into it... 
All new features implemented across both views: files and preview windows.

v0.09
Now has multiple screenshot support in the works! Currently grid view works for both previewing and saving (although they may be a fex pixels off) in addition to the original list view.
Some code moved about, a few potential future bugs fixed...and a few new ones probably made.
Changed a few things in this README.

v0.08
Bugfix release, experimental widget graphics.
Fixed bug(s) related to transtext.png file and text rendering in general. The theme.xml is now cleared from cache after being read to allow for it to be replaced when a new theme is loaded.
Filepath box now actually works properly: instead of simply displaying the filepath chosen when you click Browse, the file opened depends on what is written into the filepath box (either by the file open dialog or your own manual entry)
Random bubble placement is now the same on the preview and saved file rather than being completely different for both: bubble coordinates are shared between functions and will only re-randomise when Browse is clicked again for the next theme.
Minor additions to debug output.
Fixed error that only seems to affect Windows (?) regarding file cleanup at the end. Needs looking into...?

v0.07
Some bugfixes, cleanup and minor new features:
Theme zips that contain folders are now supported with the simpler zipfile.extractall() function.
Added "classic" theme as an option to use for any missing images/files alongside Dark Water and classic is now enabled by default (seeing as it contains backgrounds and a theme.xml file). Users can use their own folders as replacements for missing images by simply making a folder in their themeshootertk directory and setting "missing images replacement theme" in the settings file from "classic" to the name of their custom folder.
Added a setting for command line output support, which displays messages as to what the program is currently doing, which may be useful for debugging so we can see roughly at what point something failed if python's own errormessages aren't enough. At the moment these messages are basic and not really all that useful but they can give a better feel as to how long each task (e.g. extracting files, drawing windows/previews, etc) takes.
Cleaned up replacement image, background.png, hbc.png and file-cleanup related code. In theory this should take care of most OSError and missing file bugs...in theory...

v0.06
Now has basic application database support, allowing for text and images from actual homebrew apps to replace the lorem ipsum dummy text. The appdb file's text and images are enabled by default in this version with lorem ipsum being the fallback.
Implementation of configuration files: settings, which stores program settings (more options to come) and appdb, which allows the user to edit the text and images used for the applications simply by editing the file in a text editor. Hopefully the format should make it easy for just about anyone to change settings. 
Also includes even more error checking! Whilst it's still far from perfect and most of this code was hacked together, often when tired or stressed so bugs are to be expected, overall most errors caused by missing files or incorrectly set options within the settings file shouldn't be a problem; instead prompting a dialog of the error and falling back on defaults.
Finally, placement of text should be more accurate now.

PLEASE NOTE: not all images of homebrew apps work (for example, wiidoom.png has different settings to the other files in order to make it load without corrupting the screenshot). At this point time whilst you can substitue my text and images with your own, it is advised not too until I get some bugs with image masks on the screenshots sorted out. Preview should be fine though.


v0.05
Any graphics used for screenshots that are missing will now be substituted with graphics from the Dark Water v2 theme.
Bubble number has been increased to two of each unique type of bubble instead of one and bubble placement is now pseudo-random for both the previewer and the screenshot generator. Bubble instances are created earlier on now to ensure that they remain in the background rather than above some objects. (Please note that bubble placement in the preview and the screenshot file will not be the same and overlaps between bubbles are possible. Multiple clicks of the generate screenshot button may result in better results)
Fixed bug involving running the program from the commandline when in another directory. We now record the program/program files directory for ThemeShooterTk as well as the directory the user is currently in and switch directory at certain intervals to prevent missing file errors due to the program expecting everything to be in one directory for it.

v0.04
Screenshots can now be generated.
I went on a different angle with this compared to my original plan (saving the tkinter canvas) and as such this version involved me rebuilding the preview a second time but using different functions and co-ordinates to place it on an image. Originally die to some limits with my code's structure the program generated the preview AND the screenshot in one go, leading to longer loading times.
This was fixed by moving the file cleanup function to after the root window's mainloop, ensuring that the files would be cleaned up when the GUI was closed down. This allowed me to move the screenshot generation code and cut down on time for the preview as well as making things a bit neater ^_^

PLEASE NOTE: the file cleanup code has been moved and as a result if the entire python script is killed rather than just the GUI (e.g. control-C on command line, killing the python process with "kill", etc) the files won't be cleaned up and you'll have a mess of extracted files to deal with :(

v0.03
Image alpha now works! :D
I was able to find a solution eventually and implementing it was a piece of cake but I was stumped by how my test values worked fine when setting opacity but when I set it to actually use the values from the xml (converted into a format that the function could use) failed. Turns out that I'd forgotten to perform the conversion using the decimal function rather than normal math >.<

v0.02 [Initial release to public]
Added hbc icon, added font, implemented dummy text, setup font to not require installation (only needs to be in same directory as executable), minor code adjustments, cleanup of files implemented and code has been commented somewhat.

v0.01 [No public release]
Initial program, not yet released. 
Bulk of program completed, currently lacks hbc icon, dummy text, font, comments. Attempts at generating screenshot from tkinter canvas unsuccessful.

##Special Thanks:##
Team Twiizers for HBC, 
SifJar for the original program (and allowing me to release this version!),
Leathl for ThemeShooterX (which helped give me some motivation, despite my lack of time, to continue improving on ThemeShooterTk),
NeoRame for "Dark Waters v2" theme and
bg4545 for improved hbc.png
