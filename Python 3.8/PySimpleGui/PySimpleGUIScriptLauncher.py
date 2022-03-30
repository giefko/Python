import PySimpleGUI as sg

sg.theme('DarkGrey14')

layout = [
    [sg.Text('Script output....', size=(40, 1))],
    [sg.Output(size=(88, 20), font='Courier 10')],
    [sg.Button('script1'), sg.Button('script2'), sg.Button('EXIT')],
    [sg.Text('Manual command', size=(15, 1)), sg.Input(focus=True, key='-IN-'), sg.Button('Run', bind_return_key=True), sg.Button('Run No Wait')]
]

window = sg.Window('Script launcher', layout)

# ---===--- Loop taking in user input and using it to call scripts --- #

while True:
    event, values = window.read()
    if event == 'EXIT'  or event == sg.WIN_CLOSED:
        break # exit button clicked
    if event == 'script1':
        sp = sg.execute_command_subprocess('pip', 'list', wait=True)
        print(sg.execute_get_results(sp)[0])
    elif event == 'script2':
        print(f'Running python --version')
        # For this one we need to wait for the subprocess to complete to get the results
        sp = sg.execute_command_subprocess('python', '--version', wait=True)
        print(sg.execute_get_results(sp)[0])
    elif event == 'Run':
        args = values['-IN-'].split(' ')
        print(f'Running {values["-IN-"]} args={args}')
        sp = sg.execute_command_subprocess(args[0], *args[1:])
        # This will cause the program to wait for the subprocess to finish
        print(sg.execute_get_results(sp)[0])
    elif event == 'Run No Wait':
        args = values['-IN-'].split(' ')
        print(f'Running {values["-IN-"]} args={args}', 'Results will not be shown')
        sp = sg.execute_command_subprocess(args[0], *args[1:])