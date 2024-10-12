import PySimpleGUI as sg
layout = [[sg.Text("UNISKA MAAB", font=("helvetica", 24))],
          [sg.Text("BANJARMASIN", font=("Courier", 18))]]
window = sg.Window(title="New Icon",
                   layout=layout,
                   element_justification="center",
                   icon="favicon.ico",
                   size=(430, 200))

window.read()
window.close()