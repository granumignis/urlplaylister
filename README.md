Work in Progress Readme file

This software builds .ahk files that can be executed by the free Windows software 'AutoHotKey'. The resuling .ahk files are designed to play the URLs in Succession in an unattended fashion.  this can be nice if you want to set a playlist of 'background watching' material, but the material is located on different websites that do not allow such a cross-site playlist to be created.

The software currently has special funcionality for urls containing the following domains:

-disneyplus.com
-youtube.com
-hulu.com
-netflix.com

There is no guarantee of reliability or function and no liability is assumed for data loss or damage caused by the software. The software is provided 'as-is'.


IMPORTANT NOTES:

For the sites mentioned in the list above, ensure your account with those sites is the Premium or 'No Ads' tier. Ads will interfere with timing and produce unexpected or suboptimal results.

The resulting .ahk files will attempt to open all URLS in Chrome. As such, make sure of the following:
	No Chrome windows are open at the time you execute a resulting .ahk file
	Chrome has already been authenticated to the sites used in the playlist (if the site requires authentication)


EXAMPLE SYNTAX (windows command line):

	Add a playlist item to a new or existing .ahk file:

		python urlplaylister nameofplaylistfile.ahk

	Then, enter the url and the duration (in minutes) as prompted 
	Repeat this same syntax to add additional items to an existing .ahk playlist

To execute the .ahk file
	Double click the file (as long as AutoHotKey is installed on the system running the .ahk file)
