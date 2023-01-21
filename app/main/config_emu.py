import os
import json

if __name__ == '__main__':
    from emu_config import EMU_CONFIG
else:
    from .emu_config import EMU_CONFIG


class EmuSystem:

    basedir = os.path.dirname(os.path.abspath(__file__))
    configdir = basedir + '/emu_config/'

    def __init__(self, config, name):
        self.name = name
        self.system = config['system']
        self.file_type = config['extensions']
        self.emulator1 = config['emulator1']
        self.file_dirs = config['rom_dirs']
        self.file_list = config['rom_list']
        self._rom_dirs = []
        self.rom_list = self.load_rom_list()

    @property
    def rom_dirs(self):
        self._rom_dirs = self.load_rom_dirs()
        return self._rom_dirs

    def add_rom_dir(self, path):
        if path in self.rom_dirs:
            return False
        else:
            self._rom_dirs.append(path)
            self.save_rom_list()
            return True





    def load_rom_dirs(self):
        dirs = []
        with open(self.configdir + self.file_dirs, 'r') as f:
            for line in f.readlines():
                if line == '\n':
                    continue
                dirs.append(line.rstrip('\n'))
        return dirs

    def load_rom_list(self):
        try:
            with open(self.configdir + self.file_list, 'r') as f:
                output = json.loads(f.read())
            return output
        except:
            return {}

    def scan_dirs(self):
        char_filename = {' ': '\\ ', '(': '\(', ')': '\)'}
        # char_filename = {'(': '\(', ')': '\)'}
        output = {}
        for d in self.rom_dirs:
            try:
                for rom in os.listdir(d):

                    if rom[rom.find('.'):] in self.file_type:
                        name = rom[:rom.find('.')]
                        path = (d + rom)
                        for k in char_filename:
                            path = path.replace(k, char_filename[k])
                        text = ''
                        output[name] = {'path': path, 'text': text}
            except FileNotFoundError:
                continue


        with open(self.configdir + self.file_list, 'w') as f:
            f.write(json.dumps(output, indent=3))

        self.rom_list = output

        return output

    def save_rom_list(self):
        with open(self.configdir + self.file_dirs, 'w') as f:
            for path in self._rom_dirs:
                f.write(str(path) + '\n')

    def update_roms(self):
        self.rom_list = self.scan_dirs()



    def find_rom(self, text):
        output = []
        for game in self.rom_list:
            if text.lower() in game.lower():
                output.append(game)
        return output

    def run_game(self, name):
        os.system(f"{self.emulator1} {self.rom_list[name]['path']}")



####CONFIG
emulators = {
    'nes': EmuSystem(EMU_CONFIG['nes'], 'nes'),
    'c64': EmuSystem(EMU_CONFIG['c64'], 'c64')
}


##### TEST




















