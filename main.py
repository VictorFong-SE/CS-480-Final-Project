import PySimpleGUI as sg
import workingDatabase
sqlDatabase = workingDatabase.DB()

sqlDatabase.performTextQuery("SELECT * FROM matches2020;")

#sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.

sql_search = [
    [
        sg.Text("Optional Arguments"),
        sg.In(size=(25, 1), enable_events=True, key="-inputArgs-"),
        sg.Button('Submit', font=('Times New Roman', 12))

    ],
    [
        sg.Listbox(
            values=["Games Won",
                    "Games Lost",
                    "Player With Most Points",
                    "Game Stats"], enable_events=True, size=(75, 36), key="-FILE LIST-"
        )
    ],
]

sql_output = [
    [
        sg.Text("Look Into The Esports Data To Stay Updated!", font=('Times New Roman', 20)),
    ],

    [

        sg.Listbox(
            values=[], enable_events=True, size=(75, 36), key="-OUT LIST-"
        )
    ],
]
layout = [
    [
        sg.Column(sql_search),
        sg.VSeperator(),
        sg.Column(sql_output),
    ]
]

window = sg.Window("Image Viewer", layout)
while True:
    # Run the Event Loop
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break

    if event == 'Submit':
        sqlDatabase.performInternalQuery(values[0], values[1])

window.close()


