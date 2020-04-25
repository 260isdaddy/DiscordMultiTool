cls
py -3 -m pip >nul
IF %ERRORLEVEL% NEQ 0 py -3 -m pip install pip --user

py -3 -m discord >nul
IF %ERRORLEVEL% NEQ 0 py -3 -m pip install -U discord.py[voice] --user

py -3 -m requests >nul
IF %ERRORLEVEL% NEQ 0 py -3 -m pip install -U requests --user

py -3 -m BeautifulSoup4 >nul
IF %ERRORLEVEL% NEQ 0 py -3 -m pip install -U BeautifulSoup4 --user

py BotMain.py