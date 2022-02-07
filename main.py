import PySimpleGUI as sg
import controller 

sg.theme('DarkBlack1')

layout = [
    [sg.Text('Your Weight on Other Planets')],
          [sg.Input(size=(6,1), key='-WEIGHT-'), sg.Button('Calculate')],
          [
              [sg.Text("Mercury:"),sg.Text(size=(15,1), key='-MERCURY_OUTPUT-')],
              [sg.Text("Venus:   "),sg.Text(size=(15,1), key='-VENUS_OUTPUT-')],
              [sg.Text("Mars:     "),sg.Text(size=(15,1), key='-MARS_OUTPUT-')],
              [sg.Text("Jupiter:   "),sg.Text(size=(15,1), key='-JUPITER_OUTPUT-')],
              [sg.Text("Saturn:  "),sg.Text(size=(15,1), key='-SATURN_OUTPUT-')],
              [sg.Text("Uranus:  "),sg.Text(size=(15,1), key='-URANUS_OUTPUT-')],
              [sg.Text("Neptune:"),sg.Text(size=(15,1), key='-NEPTUNE_OUTPUT-')],
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
        weight = values['-WEIGHT-']
        
        mercury_weight = controller.mercury_weight(weight)
        window['-MERCURY_OUTPUT-'].update(mercury_weight)

        venus_weight = controller.venus_weight(weight)
        window['-VENUS_OUTPUT-'].update(venus_weight)
       
        mars_weight = controller.mars_weight(weight)
        window['-MARS_OUTPUT-'].update(mars_weight)
        
        jupiter_weight = controller.jupiter_weight(weight)
        window['-JUPITER_OUTPUT-'].update(jupiter_weight)
        
        saturn_weight = controller.saturn_weight(weight)
        window['-SATURN_OUTPUT-'].update(saturn_weight)

        uranus_weight = controller.uranus_weight(weight)
        window['-URANUS_OUTPUT-'].update(uranus_weight)

        neptune_weight = controller.neptune_weight(weight)
        window['-NEPTUNE_OUTPUT-'].update(neptune_weight)

        pluto_weight = controller.pluto_weight(weight)
        window['-PLUTO_OUTPUT-'].update(pluto_weight)

window.close()