import PySimpleGUI as sg


class MyApp:
    def __init__(self):
        # Create the layout
        options = ['docs', 'ppt', 'xls']
        layout = [
                    [sg.Column(layout=[
                        [sg.Image(filename='src/res/word_icon.jpg')],
                    ]),
                    sg.Column(layout=[
                        [sg.Text(text="Pdf Converter", background_color='teal',font=('arial', 25, 'bold'))],
                        [sg.Input(size=20), sg.FileBrowse(change_submits=True)],
                        [sg.Button('Convert'), sg.Text('target_type:', background_color='teal'),sg.Combo(options, tooltip="convert to", key='combo', enable_events=True)],
                        ],background_color="teal")],
                ]

        # Create the window
        self.window = sg.Window('Pdf Converter', layout, resizable=False, grab_anywhere=True, icon="src/res/icon.jpg", background_color="teal")

    def run(self):
        # Loop forever reading the window's values, updating the window
        while True:
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, 'Quit'):
                break
            elif event == 'Convert':
                selected_files = values[1]
                print(f'Selected file: {selected_files}')
            elif event == 'combo':
                selected_file_type = values['combo']
                print(f'{selected_file_type}')

        # Close the window
        self.window.close()

# Create the app and start it
app = MyApp()
app.run()
