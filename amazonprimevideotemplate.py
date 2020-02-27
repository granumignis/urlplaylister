import string

APVTemplate = string.Template("""

Run, chrome.exe $sUrl
Sleep, 5000
SetTitleMatchMode 2
WinMove, Prime Video, , 0, 0, 640,480 ;
Sleep 5000
Send {space}
Sleep, 15000
Send {f}
Sleep, $sLength
SetTitleMatchMode 2
IfWinExist Prime Video
		WinClose
Sleep, 5000


""") 