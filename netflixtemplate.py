import string

NTemplate = string.Template("""

Run, chrome.exe $sUrl
Sleep, 5000
SetTitleMatchMode 2
WinMove, Netflix - Google Chrome, , 0, 0, 640,480 ;
MouseClick, left, 97, 252
Sleep, 5000
Send {f}
Sleep, $sLength
SetTitleMatchMode 2
IfWinExist Netflix - Google Chrome
		WinClose
Sleep, 5000


""") 