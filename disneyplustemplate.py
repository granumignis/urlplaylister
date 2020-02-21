import string

DTemplate = string.Template("""

Run, chrome.exe $sUrl
Sleep, 5000
SetTitleMatchMode 2
WinMove, Disney+ - Google Chrome, , 0, 0, 640,480 ;
Sleep, 5000
MouseClick, left, 590,397
Sleep, 500
MouseClick, left, 590,397
Sleep, $sLength
SetTitleMatchMode 2
IfWinExist Disney+ - Google Chrome
		WinClose
Sleep, 5000


""") 


