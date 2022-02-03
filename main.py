import PySimpleGUI as sg


sg.theme('DarkBlack1')

layout = [
    [sg.Text('Your Weight on Other Planets')],
          [sg.Input(size=(6,1), key='-WEIGHT-'), sg.Button('Calculate')],
          [
              [sg.Text("Mercury:"),sg.Text(size=(15,1), key='-MERCURY_OUTPUT-')],
              [sg.Text("Mars:     "),sg.Text(size=(15,1), key='-MARS_OUTPUT-')],
              [sg.Text("Jupiter:   "),sg.Text(size=(15,1), key='-JUPITER_OUTPUT-')],
              [sg.Text("Pluto:     "),sg.Text(size=(15,1), key='-PLUTO_OUTPUT-')],
          ],
          [sg.Button('Exit')]
          ]

window = sg.Window('Weight on Planets Calculator', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Calculate':
        # Update the "output" text element to be the value of "input" element
        window['-MERCURY_OUTPUT-'].update(values['-WEIGHT-'])
        window['-MARS_OUTPUT-'].update(values['-WEIGHT-'])
        window['-JUPITER_OUTPUT-'].update(values['-WEIGHT-'])
        window['-PLUTO_OUTPUT-'].update(values['-WEIGHT-'])

window.close()