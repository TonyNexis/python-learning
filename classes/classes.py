from dataclasses import dataclass

class Test: 
    def __init__(
            self,
            side_text,
            main_color,
            additional_colors,
            autopilot
    ):
        self.side_text = side_text
        self.main_color = main_color
        self.additional_colors = additional_colors
        self.autopilot = autopilot

    def view_info(self):
        print(f'some info ==> {self.side_text}')

@dataclass(frozen=True)
class Plane:
    side_text: str
    main_color: str
    additional_colors: str
    autopilot: bool

raptor = Test(
    side_text='Raptor 323',
    main_color='red',
    additional_colors=['black', 'white'],
    autopilot='false'
)

boing = Plane('boing 123', 'white', 'blue', True)

print(f'Raptor colors ->> {', '.join(raptor.additional_colors)}')
print(f'Boing ->> {boing}')
