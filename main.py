import PySimpleGUI as sg
import workingDatabase

sqlDatabase = workingDatabase.DB()

sqlDatabase.performTextQuery("SELECT * FROM matches2020;")

sg.theme('DarkBlue2')


def make_table(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]

    return data


# ------ Make the Table Data ------
data = make_table(num_rows=100, num_cols=20)
headings = [str(data[0][x]) + '     ' for x in range(len(data[0]))]

sql_search = [
    [
        sg.Text("Input Arguments"),
        sg.Input(size=(25, 1), enable_events=True, key="-inputArgs-"),
        sg.Button('Submit', font=('Times New Roman', 12))

    ],
    [
        sg.Listbox(
            values=[
                "01. Custom Query - Input: a mySQL query within the bounds of Select permissions - Output: The result of that query.",
                "02. Most Popular Champion - Input: role (ie. top) - Output: Champion and number of times played",
                "03. Number of Wins - Input: TeamName (ie. Fnatic) - Output: the number of wins that the given team had that year.",
                "04. Match Winner - Input: matchID (ex.5655-7249) - Output: the Winning team, and players of that team.",
                "05. Tag-Move Speed - Input: A tag of a champion (ex. Mage) - Output: The movespeeds of the champions, asc.",
                "06. Difficulty - Input: Champion Name(ie. Jhin) - Output: Difficulty levels.",
                "07. Health - Input: Champion Name(ie. Jhin) - Output: Health levels.",
                "08. Mana - Input: Champion Name(ie. Jhin) - Output: Mana levels.",
                "09. Move Speed - Input: Champion Name(ie. Jhin) - Output: Move Speed levels.",
                "10. Attack Damage - Input: Champion Name(ie. Jhin) - Output: Attack Damage levels.",
                "11. Attack Range - Input: Champion Name(ie. Jhin) - Output: Attack Range levels.",
                "12. Attack Speed -  Input: Champion Name(ie. Jhin) - Output: Attack Speed levels.",
                "13. Armor - Input: Champion Name(ie. Jhin) - Output: Armor levels.",
                "14. Magic Resist - Input: Champion Name(ie. Jhin) - Output: Magic Resist levels.",
                "15. All Stats - Input: Champion tag (ie.Assassin) - Output: All stats of that tag, organized by name",
                "16. Specify - Input: Team Name, Role (ie. G2 Esports,top) - Output: A list of champions the role has played on their team",
                "17. Rivalry - Input: Team A, Team B (ie. G2 Esports,Fnatic) - Output: all games between the two, and stats of them."
                ], enable_events=True, size=(100, 36), auto_size_text=True, key="-FILE LIST-"
        )
    ],
]

sql_output = [
    [
        sg.Text("Look Into The Esports Data To Stay Updated!", font=('Times New Roman', 20)),
    ],

    [

        sg.Table(

            values=data, headings=headings,
            auto_size_columns=True,
            display_row_numbers=True,
            justification='right',
            num_rows=20,
            alternating_row_color='black',
            key='-TABLE-',
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
        print("submit button pressed!")

        if values['-FILE LIST-'][0][:2] == "01":
            result = sqlDatabase.performTextQuery(values['-inputArgs-'])
            window['-TABLE-'].update([list(result) for result in result])
        elif values['-FILE LIST-'][0][:2] == "02":
            result = sqlDatabase.performInternalQuery("02.sql", values['-inputArgs-'])
            prepend = (values['-inputArgs-'], 'Total Plays')
            result.insert(0, prepend)
            window['-TABLE-'].update([list(result) for result in result])
        elif values['-FILE LIST-'][0][:2] == "03":
            result = sqlDatabase.performInternalQuery("03.sql", values['-inputArgs-'])
            prepend = ('Team', 'Total Wins')
            result.insert(0, prepend)
            window['-TABLE-'].update([list(result) for result in result])
        elif values['-FILE LIST-'][0][:2] == "04":
            result = sqlDatabase.performInternalQuery("04.sql", values['-inputArgs-'])
            prepend = ('result', 'Team', 'Top', 'Jungle', 'Mid', 'ADC', 'Support')
            result.insert(0, prepend)
            window['-TABLE-'].update([list(result) for result in result])
        elif values['-FILE LIST-'][0][:2] == "05":
            result = sqlDatabase.performInternalQuery("05.sql", values['-inputArgs-'])
            prepend = ('Name', 'MoveSpeed')
            result.insert(0, prepend)
            window['-TABLE-'].update([list(result) for result in result])
        elif values['-FILE LIST-'][0][:2] == "06":
            result = sqlDatabase.performInternalQuery("06.sql", values['-inputArgs-'])
            prepend = ('Name', 'Difficulty')
            result.insert(0, prepend)
            window['-TABLE-'].update([list(result) for result in result])
        elif values['-FILE LIST-'][0][:2] == "07":
            result = sqlDatabase.performInternalQuery("07.sql", values['-inputArgs-'])
            prepend = ('Name', 'HP')
            result.insert(0, prepend)
            window['-TABLE-'].update([list(result) for result in result])
        elif values['-FILE LIST-'][0][:2] == "08":
            result = sqlDatabase.performInternalQuery("08.sql", values['-inputArgs-'])
            prepend = ('Name', 'Mana')
            result.insert(0, prepend)
            window['-TABLE-'].update([list(result) for result in result])
        elif values['-FILE LIST-'][0][:2] == "09":
            result = sqlDatabase.performInternalQuery("09.sql", values['-inputArgs-'])
            prepend = ('Name', 'Move Speed')
            result.insert(0, prepend)
            window['-TABLE-'].update([list(result) for result in result])
        elif values['-FILE LIST-'][0][:2] == "10":
            result = sqlDatabase.performInternalQuery("10.sql", values['-inputArgs-'])
            prepend = ('Name', 'Attack Damage')
            result.insert(0, prepend)
            window['-TABLE-'].update([list(result) for result in result])
        elif values['-FILE LIST-'][0][:2] == "11":
            result = sqlDatabase.performInternalQuery("11.sql", values['-inputArgs-'])
            prepend = ('Name', 'Attack Range')
            result.insert(0, prepend)
            window['-TABLE-'].update([list(result) for result in result])
        elif values['-FILE LIST-'][0][:2] == "12":
            result = sqlDatabase.performInternalQuery("12.sql", values['-inputArgs-'])
            prepend = ('Name', 'Attack Speed')
            result.insert(0, prepend)
            window['-TABLE-'].update([list(result) for result in result])
        elif values['-FILE LIST-'][0][:2] == "13":
            result = sqlDatabase.performInternalQuery("13.sql", values['-inputArgs-'])
            prepend = ('Name', 'Armor')
            result.insert(0, prepend)
            window['-TABLE-'].update([list(result) for result in result])
        elif values['-FILE LIST-'][0][:2] == "14":
            result = sqlDatabase.performInternalQuery("14.sql", values['-inputArgs-'])
            prepend = ('Name', 'Magic Resist')
            result.insert(0, prepend)
            window['-TABLE-'].update([list(result) for result in result])
        elif values['-FILE LIST-'][0][:2] == "15":
            result = sqlDatabase.performInternalQuery("15.sql", values['-inputArgs-'])
            prepend = ('Name', 'Type', 'HP', 'Mana', 'Move Speed', 'Armor', "Magic Resist", 'Attack Range', 'Health '
                                                                                                            'Regen',
                       'Mana Regen', 'Attack Damage', 'Attack Speed')
            result.insert(0, prepend)
            window['-TABLE-'].update([list(result) for result in result])
        elif values['-FILE LIST-'][0][:2] == "16":
            result = sqlDatabase.performInternalQuery("16.sql", values['-inputArgs-'])
            prepend = (
            'Name', 'attack', 'defense', 'magic', 'difficulty', 'tags', 'hp', 'hpperlevel', 'mp', 'mpperlevel',
            'movespeed', 'armor', 'armorperlevel', 'spellblock', 'spellblockperlevel', 'attackrange',
            'hpregen', 'hpregenperlevel', 'mpregen', 'mpregenperlevel', 'crit', 'critperlevel',
            'attackdamage', 'attackdamageperlevel', 'attackspeedperlevel', 'attackspeed')
            result.insert(0, prepend)
            window['-TABLE-'].update([list(result) for result in result])
        elif values['-FILE LIST-'][0][:2] == "17":
            result = sqlDatabase.performInternalQuery("17.sql", values['-inputArgs-'])
            prepend = (
            'Game ID', 'Result', 'Total Team 1 Wins', ' Total Team 2 Wins', 'red top', 'red jungle', 'red mid',
            'red adc', 'red support', 'blue top', 'blue jungle', 'blue mid', 'blue adc', 'blue support')
            result.insert(0, prepend)
            window['-TABLE-'].update([list(result) for result in result])

        else:
            print("error!")
            window['-TABLE-'].update("Sorry, but the selection you entered is not acceptable. Please try again!")

window.close()
