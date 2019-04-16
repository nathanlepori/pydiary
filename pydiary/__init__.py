__version__ = '1.0.2'

import os
import traceback


class Diary:
    """
    MatLab style commands logger for the Python interpreter, with added feature. Construct a new instance to enable
    logging and call diary.off() to disable it.
    """
    _default_filename = 'diary.py'

    _diary_on = False
    _filename = None

    def __init__(self, filename=_default_filename):
        """
        Initializes and starts a new Diary, with the given or default filename.

        :param filename: Name of the file where the commands are logged
        """
        self._filename = filename
        self.on()

    def _print_command_line(self, secondary=False):
        if secondary:
            print('[{}] ... '.format(os.path.basename(self._filename)), end='')
        else:
            print('[{}] >>> '.format(os.path.basename(self._filename)), end='')

    def _check_and_start_secondary_prompt(self, cmd):
        if cmd[-1:] == ':':
            cmd += '\n'

            while True:
                self._print_command_line(True)

                current_cmd = input()
                cmd += current_cmd + '\n'

                if not current_cmd[:1] == ' ' and not current_cmd[:1] == '\t' and not current_cmd[-1:] == ':':
                    break
        return cmd

    def _start_prompt(self):
        # Allows calling diary.off()
        diary = self

        f = open(self._filename, 'a+')

        while True:
            self._print_command_line()

            cmd = None
            try:
                cmd = input()

                # Check if expression need continuation and eventually start a prompt
                cmd = self._check_and_start_secondary_prompt(cmd)

                code = compile(cmd, filename='<string>', mode='single')
                exec(code)
            except EOFError:
                self.off()
            except KeyboardInterrupt:
                print('\nKeyboardInterrupt')
                continue
            except Exception:
                traceback.print_exc()
                continue

            if not self._diary_on:
                break

            f.write(cmd + '\n')

    def on(self) -> None:
        """
        Turns this Diary instance on, logging any command typed afterwards. Call diary.off() to disable logging.
        """
        if self._diary_on:
            return

        self._diary_on = True
        self._start_prompt()

    def off(self) -> None:
        """
        Turns this Diary instance off, disabling logging and flushing any buffered command to the file, if needed. As
        long as the Diary is enabled, diary.off() is an alias for self.off().
        """
        self._diary_on = False


if __name__ == '__main__':
    Diary()
