import os
import webbrowser

def openChrome():
    os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

def openExplorer():
    os.startfile("C:\\Windows\\SysWOW64\\explorer.exe")

def openEdge():
    os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

def openCalc():
    os.startfile("C:\\Windows\\SysWOW64\\calc.exe")

def openCmd():
    os.startfile("C:\\Windows\\SysWOW64\\cmd.exe")

def opencontrolPanel():
    os.startfile("C:\\Windows\\SysWOW64\\control.exe")

def openNote():
    os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Notepad++.lnk")

def openWord():
    os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk")

def openPowerP():
    os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk")

def openPaint():
    os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\paint.net.lnk")

def openYt():
    webbrowser.open_new_tab('https://www.youtube.com/')

def openAmazon():
    webbrowser.open_new_tab('https://www.amazon.com/')

def openDocs():
    webbrowser.open_new_tab('https://docs.google.com/document/u/0/')

def shutdownandclose():
    import subprocess
    # forced shutdown closes windows without saving; you might need to add shell=True 
    confirmation = input("Do you want to proceed to shutdown(Y/n)? ")

    if confirmation =='Y':
        COMMAND  = """(New-Object -comObject Shell.Application).Windows() | foreach-object {$_.quit()}; Get-Process | Where-Object {$_.MainWindowTitle -ne \\"\\"} | stop-process; Stop-Computer"""
        os.system("shutdown /s /f /t 5")
        subprocess.run(['powershell', '-command', COMMAND], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        exit()
