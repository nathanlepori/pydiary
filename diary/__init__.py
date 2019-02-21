import os
import traceback


class Diary:
    _default_filename = 'diary.py'

    _diary_on = True
    _filename = None

    def __init__(self, filename=_default_filename):
        # Allows calling diary.off()
        diary = self

        self._filename = filename

        f = open(self._filename, 'a+')

        while True:
            self._print_command_line()
            cmd = input()

            try:
                exec(cmd)
            except Exception:
                traceback.print_exc()

            if not self._diary_on:
                break
            f.write(cmd + '\n')

    def _print_command_line(self):
        print('[{}] >>> '.format(os.path.basename(self._filename)), end='')

    def off(self):
        self._diary_on = False


if __name__ == '__main__':
    Diary()
