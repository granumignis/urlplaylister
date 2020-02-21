

Run, chrome.exe https://www.youtube.com/watch?v=NkK31uQNY28
Sleep, 5000
SetTitleMatchMode 2
WinMove, YouTube - Google Chrome, , 0, 0, 640,480 ;
Sleep, 5000
Send {f}
Sleep, 60000
SetTitleMatchMode 2
IfWinExist YouTube - Google Chrome
		WinClose
Sleep, 5000


