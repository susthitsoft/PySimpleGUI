import PySimpleGUI as sg
import sys

'''
Quickly add a GUI to your script!

This simple script shows a 1-line-GUI addition to a typical Python command line script.

Previously this script accepted 1 parameter on the command line.  When executed, that
parameter is read into the variable fname.

The 1-line-GUI shows a form that allows the user to browse to find the filename. The GUI
stores the result in the variable fname, just like the command line parsing did.
'''

if len(sys.argv) == 1:
    button, (fname,) = sg.FlexForm('My Script').LayoutAndRead([[sg.T('Document to open')],
                                                           [sg.In(), sg.FileBrowse()],
                                                           [sg.Open(), sg.Cancel()]])
else:
    fname = sys.argv[1]

if not fname:
    sg.MsgBox("Cancel", "No filename supplied")
    raise SystemExit("Cancelling: no filename supplied")
