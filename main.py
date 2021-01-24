import PySimpleGUI as sg
import pprint
import os.path
import json


def show_diagnostic_results():
    return


def format_output(json):
    return


def load_window():
    # First the window layout in 2 columns
    input_column = [
        [
            sg.Text("Ransomware File     "),
            sg.In(size=(65, 1), enable_events=True, key="-FILE-"),
            sg.FileBrowse(),
        ],
        [
            sg.Text("Ransomware Name     "),
            sg.In(size=(65, 1), enable_events=True, key="-NAME-"),

        ],
        [
            sg.Text("Ransomware Extension"),
            sg.In(size=(65, 1), enable_events=True, key="-EXTENSION-"),
        ],
        [
            sg.Button('Submit')
        ],
        [
            sg.HSeparator()
        ],
        [
            sg.Text("Input instructions")
        ]

    ]

    results_viewer_column = [
        [sg.Text("Diagnostics Results")],
        [sg.Text(size=(100, 100), key="-TOUT-")],
        [sg.Image(key="-IMAGE-")],
    ]

    # ----- Full layout -----
    layout = [
        [
            sg.Column(input_column),
            sg.VSeperator(),
            sg.Column(results_viewer_column),
        ]
    ]

    window = sg.Window("Ransomware Solution Recomendation System", layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "Submit":
            file = values["-FILE-"]
            name = values["-NAME-"]
            extension = values["-EXTENSION-"]

            # function call to main func
            '''
            print(file)
            print(name)
            print(extension)
            '''

            #out =  main(file,name,extension) //return (json1 json2 json3)


            window["-TOUT-"].update(json.dumps(parsed, indent=4, sort_keys=True))



load_window()
