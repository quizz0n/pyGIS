@echo off &setlocal
set /p "folder=Enter the folder name to be created: "
md "%~dp0\%folder%" ||(pause &goto :eof)
md "%~dp0\%folder%\Images"
md "%~dp0\%folder%\Initiale"
md "%~dp0\%folder%\Prj"
md "%~dp0\%folder%\Style"
md "%~dp0\%folder%\Tiling"
md "%~dp0\%folder%\Vecini"
