import os
from .emu_config import check_config_dirs, EmuSystem


class Emulators:
    def __init__(self):
        check_config_dirs()
        self.emulators = self.load_emulators()
        self.add_emu()


    def load_emulators(self):
        emulators = {}
        for emu in os.listdir(EmuSystem.dir_config()):
            system = emu[0:emu.find('.json')]
            emulators[system] = EmuSystem(system)
        self.emulators = emulators
        self.add_emu()
        return emulators

    def add_emu(self):
        for x in self.emulators:
            setattr(self, x, self.emulators[x])

    def add_new_emulator(self, name):
        if name in self.emulators:
            return False
        new = EmuSystem(name)
        self.emulators[name] = new
        self.add_emu()

    def __repr__(self):
        print('*' * 100)
        for system in self.emulators:
            print(f'***** {system} *****\n {self.emulators[system].system_conf}')
            print('-' * 100)
        return '*' * 100



