import os
import subprocess

from pathlib import Path


def make_paths():
    venv_python_path = Path(__file__).absolute().parents[1]
    venv_subdir, exe_ext = ('bin', '') if os.name == 'posix' else ('Scripts', '.exe')
    venv_python_path = venv_python_path.joinpath('venv', venv_subdir, f'python{exe_ext}')
    usb_app_path = Path(__file__).absolute().parent
    db_merge_module_path = usb_app_path.joinpath('db_merge', 'db_merge.py')
    usb_server_module_path = usb_app_path.joinpath('usb_server', 'usb_server.py')
    return venv_python_path, db_merge_module_path, usb_server_module_path


def make_commands_to_run_usb(venv_python_path, db_merge_module_path, usb_server_module_path):
    db_merge_command = f'{venv_python_path} {db_merge_module_path}'
    usb_server_command = f'{venv_python_path} {usb_server_module_path}'
    return db_merge_command, usb_server_command


def launch_usb():
    venv_python_path, db_merge_module_path, usb_server_module_path = make_paths()
    db_merge_command, usb_server_command = make_commands_to_run_usb(venv_python_path,
                                                                    db_merge_module_path,
                                                                    usb_server_module_path,
                                                                    )
    subprocess.run(db_merge_command)
    subprocess.run(usb_server_command)


if __name__ == '__main__':
    launch_usb()
