# Enum to provide the options that status may be in the Task class

from enum import Enum

class ValueOptions(Enum):

    # Options
    todo = "todo"
    in_progress = "in-progress"
    done = "done"
