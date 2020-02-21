import string

YTemplate = string.Template("""

Run, chrome.exe $sUrl
Sleep, 5000
SetTitleMatchMode 2
WinMove, YouTube - Google Chrome, , 0, 0, 640,480 ;
Sleep, 5000
Send {f}
Sleep, $sLength
SetTitleMatchMode 2
IfWinExist YouTube - Google Chrome
		WinClose
Sleep, 5000


""") 