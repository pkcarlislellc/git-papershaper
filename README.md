# git-papershaper
Papershpaer Open Source Project
﻿Paper Shaper (C)2014, 2019.  Distributed under the GNU General Public License compliments of P. K. Carlisle LLC

Introduction:

I made an effort to make Paper Shaper as easy to use as possible.  I hope that you enjoy it, and that the operation is as simple as I anticipated.  Please read at least the Summary, Selecting Wallpaper and Operation sections for basic usage (they're short).

I started off your gallery of offline images with a couple of public domain JPG images.  Feel free to delete them if desired...the point was simply to get you up and running as quickly as possible.  If selecting wallpaper from both webcams and an offline gallery, you may want to have a similar number of offline images and webcams for a more random feel.

Enjoy!

Summary:

This program uses one of three user selected options and provides random wallpaper on that basis.

The user can:

- choose a random offline image from any JPG image stored in ~/com.pkcarlisle/papershaper/gallery/
- choose a random online image from any webcam online in a user maintained list in ~/com.pkcarlisle/papershaper/webcamgrab.txt
- choose a random image from either a user stored offline gallery image OR an online webcam (Paper Shaper decides)
- choose how often the wallpaper updates

Paper Shaper requires the lynx browser.  Paper Shaper uses lynx because it will grab an image then go away, so it can run silently in the background as an automated process however often you invoke Paper Shaper. To use lynx, YOU DO NOT, NOT, NOT (did I say NOT?) replace your current browser, learn a new browser, change your default browser, transfer cookies, bookmarks, or anything of the sort.  In fact, once you have lynx installed, you can forget that it's even there.   Lynx will be available as part of your Linux distro.  Paper Shaper assumes that lynx will be installed in /usr/bin/  (**UBUNTU users, see the SPECIAL NOTE in the Technical Specifications regarding lynx versus links browsers.)

Paper Shaper requires python.  It will be available with your Linux distro or at http://www.python.org/. Paper Shaper is written for  Python 3. BOTH Python 2 and Python 3 versions are included in this package. As of October, 2019, the default version, that is, papershaper.py is written for Python 3. papershaper-python-2.py is the Python 2 version for those who want it. (For either version, usage is the same, just use the command 'python3 papershaper...' or 'python papershaper-python-2.py...' as desired.)

Selecting wallpaper:

As your wallpaper, use your operating system's normal process for choosing ~/com.pkcarlisle/papershaper/papershaper.jpg as wallpaper.  Paper Shaper handles the swapping and selecting of various images.  Because the name of the file will always be consistent, this image can be referenced as wallpaper by your operating system and update without irregularity.

Note that at times a webcam image may appear grainy, gray, black or otherwise distorted or downright ugly.  Paper Shaper is most likely not the cause in these instances.  Webcams generally run 24/7, get rained on, fogged over, take pictures of pitch blackness at times, or go offline temporarily or permanently.  The best test is to go to the log of the last URL Paper Shaper used at ~/com.pkcarlisle/papershaper/papershaper.log, copy the URL listed there and drop it into a browser like Firefox manually.  If the image is similar or you get an error, there's your answer.  If you want to alter the listing of webcams to add or delete a webcam, see the technical specifications section below.

For best results, invoke Paper Shaper from a start up script or as a Startup Application.

To add new local/offline wallpaper(s), just drop a .jpg into the gallery. Papershaper will rescan the gallery folder and incorporate your addition. 

Operation:

You do not need an external event launcher like cron or evolution calendar to update wallpaper from the local image gallery or random webcam. As a rule you launch with the command python3 ~/com.pkcarlisle/papershaper/papershaper.py or similar as a start up script or command when your computer starts.  Adding a startup command varies from one Linux spin to another.  Paper Shaper has been tested in, and runs beautifully in: KDE 4 (Kubuntu 12.04 LTS), Gnome 2 (CentOS 6 / RHEL 6), MATE (Fedora 20, Ubuntu MATE 18.04). Use your GUI's
process to add a startup command.

Advanced usage is as follows:
python3 papershaper.py [g | w | m ] [minutes]

g – select a random wallpaper image from user's local/offline gallery of JPG images stored in ~/com.pkcarlisle/papershaper/gallery/
 (use this option if you are not always online or if you don't want webcam wallpaper)

w – select a random wallpaper image online from the listing of webcams found in ~/com.pkcarlisle/papershaper/webcamgrab.txt

m – Max Random: get a random wallpaper from offline gallery OR a random image from an online webcam (Paper Shaper chooses)

minutes is the minutes to delay between refreshes, default is 20 minutes.

For example the command python3 papershaper.py m 30 refreshes randomly from either a webcam or local gallery image every 30 minutes

Default usage is python3 ~/com.pkcarlisle/papershaper/papershaper.py It gets a random wallpaper from your offline/local gallery only, once every 20 minutes (use this usage if you are not always online or if you don't want webcam wallpaper).

If you specify the first option (g or w or m) then you must specify the minutes as well.

Technical Specifications:

This program assumes that you will be using images in .JPG format because there are a lot of webcam sites that serve images in .JPG format.  If you do have an image that is in another format and you really want to use it in the Paper Shaper queue, consider converting it to .JPG format with the GIMP (takes approximately 60 seconds).  Support for other graphics formats is not planned.  

Paper Shaper requires the lynx browser.  Paper Shaper uses lynx because it will grab an image then go away, so it can run silently in the background as an automated process however often you invoke Paper Shaper. To use lynx, YOU DO NOT, NOT, NOT (did I say NOT?) replace your current browser, learn a new browser, change your default browser, transfer cookies, bookmarks, or anything of the sort.  In fact, once you have lynx installed, you can forget that it's even there.   Lynx will be available as part of your Linux distro.  Paper Shaper assumes that lynx will be installed in /usr/bin/

** SPECIAL NOTE FOR UBUNTU USERS. In Ububtu 18.04 there is an offering of a command line browser calld links. links IS NOT lynx. Papershaper requires the lynx browser. 'sudo apt install lynx' or similar should get lynx installed for you. lynx is not installed by Ubuntu 18.04 by default, but is readily available for installation.

This program requires Python.  It will be available with your Linux distro or at http://www.python.org/. Papershaper was originally written for and tested in Python 2.6.6.  In anticipation of end of life/support by the Python developers for Python 2, in October, 2019, Papershaper was updated to run in Python 3 by default. BOTH Python 2 and Python 3 versions are included in this package. As of October, 2019, the default version, that is, papershaper.py is written for Python 3. papershaper-python-2.py is the Python 2 version for those who want it. (For either version, usage is the same, just use the command 'python3 papershaper...' or 'python papershaper-python-2.py...' as desired.)

The listing of webcams file can contain comments.  Just don't end a comment with .JPG Or .JPG?  Comments in this file are filtered out automatically when Paper Shaper updates the wallpaper.  

The webcam list at ~/com.pkcarlisle/papershaper/webcamgrab.txt can be modified.  You can add or remove cams from the list with the following rules:  You can add comments as you like, just don't end a comment with .JPG or .JPG?  Comments in this file are filtered out automatically when Paper Shaper updates the wallpaper.  The actual webcam URLs must be in a valid URL format. So, you may have a comment like London, England or Antarctica, RRS James Clark Ross Research Ship Webcam but the URLs would have to be in a format like http://common.gcstatic.com/u/webcam/webcam73-roof.jpg or http://www.antarctica.ac.uk/webcams/rrs_james_clark_ross/webcam.jpg.  Either one comment or URL per line.  Edit with your favorite text editor.

The listing of local/offline images is located in ~/com.pkcarlisle/papershaper/gallerylist.txt.  This list cannot contain comments and will be replaced every time Paper Shaper updates the wallpaper. You do not need to (and should not) create or maintain a local images file list manually.  It is created automatically based on the files you store in ~/com.pkcarlisle/papershaper/gallery/ (plus your webcam listing if you choose webcam images).

To add new local/offline wallpaper(s), just drop a .jpg into the gallery. Papershaper will rescan the gallery folder and incorporate your addition. 

This program logs the last URL or local .JPG file pulled to ~/com.pkcarlisle/papershaper/papershaper.log.  This is purely for your convenience.  Not every webcam includes a label, and not all of them have images large enough or interesting enough or of good enough quality to be worth keeping. The log will tell you which URL or file generated the last wallpaper image and you can delete any URL you do not like from the webcam list.

Q: I want to use papershaper to monitor only one image from only one online webcam and to update it periodically. How can I do that?

A: Backup then edit the webcam list at ~/com.pkcarlisle/papershaper/webcamgrab.txt. Copy the webcam you want TWICE, like this:

London, England  
http://common.gcstatic.com/u/webcam/webcam73-roof.jpg  
London, England  
http://common.gcstatic.com/u/webcam/webcam73-roof.jpg  

Remove all other website listings and also any blank lines from ~/com.pkcarlisle/papershaper/webcamgrab.txt.

Set your papershaper startup command to use only online content with the w option: /usr/bin/papershaper w 1  
You are essentially fooling papershaper into selecting a 'random' online webcam but limiting the choice to only one webcam. This updates wallpaper from the same webcam
as often as you wish.

Q: How do I add new wallpaper to papershaper?  

A: Drop any wallpaper quality .JPG into the gallery at ~/com.pkcarlisle/papershaper/gallery/  
There is no need to rescan the folder, papershaper will rescan the folder for all wallpapers the next time it cycles.  

Q: How many wallpapers can you have in the papershaper queue?  

A: I have not run into a limit yet and I have around 250 including webcams and offline gallery images.  

The Fine Print:

The source of the original list of webcams was Portalview Live Desktop Wallpaper created by Michelle Blowers located at https://sourceforge.net/projects/portalviewlivew/, created under a GNU General Public License version 3.0. That original list was modified, added to, subtracted from, and altered significantly for Paper Shaper.

This program assumes that you will be using images in .JPG format because there are a lot of webcam sites that serve images in .JPG format.  If you do have an image that is in another format and you really want to use it in the Paper Shaper queue, consider converting it with the GIMP (takes approximately 60 seconds).  Support for other graphics formats is not planned.

Yes, this is for Linux.  No, it's not for Windows or Mac.  Nuff said.

If you found this file elsewhere, links to latest information is here:

Google Code:
https://code.google.com/p/paper-shaper-random-wallpaper-tool/ (October, 2019: Deprecated: Google Code is no longer an active service/venture.)

Sourceforge:
https://sourceforge.net/projects/papershaper/

Free Software Foundation:
http://directory.fsf.org/wiki/Paper_Shaper

(C)2014,2019.  Distributed under the GNU General Public License compliments of P. K. Carlisle LLC at www.pkcarlisle.com. Notes to mail@pkcarlisle.com. Follow on twitter @pkcarlislellc. 

Feedback is always welcome, although any communication may be used by me without restriction.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the license, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose.  See the GNU General Public License for more details.

It is purely optional, as just stated...you may use Paper Shaper forever and a day at no cost, but if you would like to contribute something for Paper Shaper, it will certainly encourage me in developing future projects and distributing them through similar channels. To contribute, go to http://www.pkcarlisle.com/blog.html#wsawom1

Changelog:

Thu Sep 11 2014  
Now, with more webcams!  Expanded the list of webcams in webcamgrab.txt. 
Updated and clarified the documentation.

Mon Oct 7 2019
Converted papershaper.py to Python 3 in anticipation of Python 2 reaching end of life/support by the Python developers.

Retained Python 2 version for those who want it.

Updated documentation regarding Python 2 versus Python 3.

Added a note for Ubuntu users about lynx versus links.
