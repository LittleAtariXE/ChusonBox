from .config_emu import EmuSystem
import os

def make_emulators():
    emulators = {}
    for emu in os.listdir(EmuSystem.dir_config()):
        system = emu[0:emu.find('.json')]
        emulators[system] = EmuSystem(system)
    return emulators



