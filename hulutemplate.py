import string

HTemplate = string.Template("""

Run, chrome.exe $sUrl
Sleep, 5000
SetTitleMatchMode 2
WinMove, Hulu, , 0, 0, 640,480 ;
Sleep 1000
Send {space}
Sleep, 5000
Send {f}
Sleep, $sLength
SetTitleMatchMode 2
IfWinExist Hulu
		WinClose
Sleep, 5000


""") 