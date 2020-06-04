import string

APVTemplate = string.Template("""

Run, chrome.exe $sUrl
Sleep, 5000
SetTitleMatchMode 2
WinMove, Prime Video - Google Chrome, , 0, 0, 640,480
WinActivate, Prime Video - Google Chrome
Sleep 5000
Click, 312,280
Sleep, 15000
Send {f}
Sleep, $sLength
SetTitleMatchMode 2
IfWinExist Prime Video - Google Chrome
		WinClose
Sleep, 5000


""") 