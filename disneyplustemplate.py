import string

DTemplate = string.Template("""

Run, chrome.exe $sUrl
Sleep, 5000
SetTitleMatchMode 2
WinMove, Disney+ | Video Player - Google Chrome, , 0, 0, 640,480 ;
Sleep, 6000
Click, 590,397
Sleep 100
Click, 590,397
Sleep, $sLength
SetTitleMatchMode 2
IfWinExist Disney+ | Video Player - Google Chrome
		WinClose
Sleep, 5000


""") 


