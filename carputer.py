import console


def read_init_state():
    # TODO - read from file
    init_dict = {'climate': {'power': False, 'temp_step': 0, 'fan_stop': 0, 'vent_buttons': 1}}

    return init_dict


def write_init_state(init_state):
    # TODO - write to file
    pass


class Carputer(object):

    def __init__(self):
        self.__view = None

    def set_view(self, view):
        self.__view = view


if __name__ == '__main__':
    _carputer = Carputer()

    _console = console.ConsoleApp()
    _console.set_controller(_carputer)

    _carputer.set_view(_console)

    _console.startup(read_init_state())
    _console.run()
