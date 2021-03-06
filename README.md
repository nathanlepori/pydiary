# pydiary
MatLab style commands logger for the Python interpreter, with added features.

## Usage
Import the Diary class from the package and create a new instance. The commands you type in from now on will be logged into a file. Call `diary.off()` to disable logging.
```python
from pydiary import Diary

Diary()                 # Turns diary on, saving commands to the default file diary.py

...

# The current active diary is automatically assigned to a variable called "diary"
diary.off()             # Turns diary off
```

You can pass a custom path for the diary file and save the instance to re-enable it afterwards:
```python
# Turns diary on, saving commands to a file called mydiary.py in the current directory
my_diary = Diary('mydiary.py')      # You can save a reference to the Diary instance to use it later

...

my_diary.off()

...

my_diary.on()           # Turns on the previously created diary
```

## Advanced usage

### Buffered mode
By default pydiary uses an internal string buffer to keep the diary file free for manual changes, and only writes to it when you turn off the diary.
You can force pydiary to flush commands to the file by calling `diary.flush()`.

Call `diary.discard()` if you want to discard all commands not yet written to the diary file.

### Direct mode
You can force pydiary to operate in direct mode by setting the `buffered` parameter to `False` when creating an instance.

```python
Diary(buffered=False)
```

In this mode pydiary will write commands directly to the diary file. Note that due to the way Python handles writing to files, the commands may not be written immediately and you may still need to call `diary.off()` to see them in the file.

## Improvement, Issues report
Suggest improvements or features, report bugs at [https://github.com/nathanlepori/pydiary/issues](https://github.com/nathanlepori/pydiary/issues)

## Authors
* Nathan Lepori
