import os
import json
import subprocess

basedir = os.path.dirname(os.path.abspath(__file__))
sys_config = basedir + '/systems/'
config_dir = basedir + '/config/'


def check_config_dirs():
    if not os.path.isdir(sys_config):
        os.makedirs(sys_config)

    if not os.path.isdir(config_dir):
        os.makedirs(config_dir)





def load_system(path):
    try:
        with open(path, 'r') as f:
            system = json.loads(f.read())
    except FileNotFoundError:
        system = {'name': None,
                'system': None,
                'extensions': [],
                'file_rom_dirs': None,
                'file_rom_list': None,
                'emulator1': None,
                'option1': '',
                'emulator2': None,
                'option2': '',
                'info': ''
            }


    return system


class EmuConfig:

    def __init__(self, name, emu_sys_conf=sys_config, emu_config=config_dir):
        self._name = name
        self.emu_sys_conf = emu_sys_conf
        self.config_path = self.emu_sys_conf + self.name + '.json'
        self.emu_config_path = emu_config
        self.system_conf = load_system(self.config_path)
        self._file_rom_dirs = self.system_conf['file_rom_dirs']
        self._file_rom_list = self.system_conf['file_rom_list']
        self._emu1 = self.system_conf['emulator1']
        self._emu2 = self.system_conf['emulator2']
        self._option1 = self.system_conf['option1']
        self._option2 = self.system_conf['option2']
        self.ext = set(self.system_conf['extensions'])
        self._system = self.system_conf['system']
        self._info = self.system_conf['info']
        self.name = name

    @staticmethod
    def dir_config():
        return sys_config

    @property
    def name(self):
        return self._name

    @property
    def file_rom_dirs(self):
        return self._file_rom_dirs

    @property
    def file_rom_list(self):
        return self._file_rom_list

    @property
    def emu1(self):
        return self._emu1

    @property
    def emu2(self):
        return self._emu2

    @property
    def system(self):
        return self._system

    @property
    def info(self):
        return self._info

    @property
    def option1(self):
        return self._option1

    @property
    def option2(self):
        return self._option2



    @name.setter
    def name(self, new):
        self._name = new
        self.system_conf['name'] = new
        self.config_path = self.emu_sys_conf + new + '.json'

    @file_rom_dirs.setter
    def file_rom_dirs(self, file_path):
        self._file_rom_dirs = file_path
        self.system_conf['file_rom_dirs'] = file_path

    @file_rom_list.setter
    def file_rom_list(self, file_path):
        self._file_rom_list = file_path
        self.system_conf['file_rom_list'] = file_path

    @emu1.setter
    def emu1(self, new):
        self._emu1 = new
        self.system_conf['emulator1'] = new

    @emu2.setter
    def emu2(self, new):
        self._emu2 = new
        self.system_conf['emulator2'] = new

    @system.setter
    def system(self, new):
        self._system = new
        self.system_conf['system'] = new

    @info.setter
    def info(self, new):
        self._info = new
        self.system_conf['info'] = new

    @option1.setter
    def option1(self, new):
        self._option1 = new
        self.system_conf['option1'] = new

    @option2.setter
    def option2(self, new):
        self._option2 = new
        self.system_conf['option2'] = new


    def add_ext(self, ext):
        self.ext.add(ext)
        self.system_conf['extensions'] = list(self.ext)





    def make_conf_file(self):
        # if not self.system_conf['name'] or not self.system_conf['rom_dirs'] or not self.system_conf['rom_list']:
        #     return False

        if not self.system_conf['name']:
            return False

        if not os.path.exists(self.emu_config_path + f'{self.name}_dirs.txt'):
            with open(self.emu_config_path + f'{self.name}_dirs.txt', 'w') as f:
                f.write('')
            self.file_rom_dirs = self.emu_config_path + f'{self.name}_dirs.txt'

        if not os.path.exists(self.emu_config_path + f'{self.name}_roms.json'):
            with open(self.emu_config_path + f'{self.name}_roms.json', 'w') as f:
                f.write(json.dumps({}))
            self.file_rom_list = self.emu_config_path + f'{self.name}_roms.json'

        if not os.path.exists(self.config_path):
            with open(self.config_path, 'w') as f:
                f.write(json.dumps(self.system_conf, indent=3))



    def delete_system(self):
        files = [self.config_path, self.file_rom_dirs, self.file_rom_list]
        for f in files:
            try:
                os.remove(f)
            except Exception as e:
                print('error: ', e)
                continue

    def save_emu_config(self):
        with open(self.config_path, 'w') as f:
            f.write(json.dumps(self.system_conf, indent=3))



class EmuSystem(EmuConfig):
    def __init__(self, name):
        super().__init__(name)
        self.make_conf_file()
        self.rom_dirs = self.load_rom_dirs()
        self.rom_list = self.load_roms_list()


    def load_rom_dirs(self):
        if not self.file_rom_dirs:
            return None
        else:
            rom_dirs = []
            try:
                with open(self.file_rom_dirs, 'r') as f:
                    for line in f.readlines():
                        if line == '\n':
                            continue
                        rom_dirs.append(line.rstrip('\n'))
                return rom_dirs
            except (FileNotFoundError, IsADirectoryError):
                return []


    def add_rom_dir(self, path):
        if not str(path).endswith('/'):
            path = path + '/'
        self.rom_dirs.append(path)
        with open(self.file_rom_dirs, 'w') as f:
            for p in self.rom_dirs:
                f.write(p + '\n')

    def load_roms_list(self):
        with open(self.file_rom_list, 'r') as f:
            roms_list = json.loads(f.read())

        return roms_list

    def scan_dirs(self):
        char_filename = {' ': '\\ ', '(': '\(', ')': '\)'}
        output = {}
        for d in self.rom_dirs:
            try:
                for rom in os.listdir(d):

                    if rom[rom.find('.'):] in self.ext:
                        name = rom[:rom.find('.')]
                        path = (d + rom)
                        for k in char_filename:
                            path = path.replace(k, char_filename[k])
                        text = ''
                        output[name] = {'path': path, 'text': text}
            except FileNotFoundError:
                continue

        self.rom_list = output
        with open(self.file_rom_list, 'w') as f:
            f.write(json.dumps(self.rom_list, indent=3))

        return output

    def run_game(self, name):
        machine = subprocess.run(f"{self.emu1} {self.option1} {self.rom_list[name]['path']}", shell=True, capture_output=True, text=True)
        if machine.returncode == 0:
            return 0






###### TEST


















