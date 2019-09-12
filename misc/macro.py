"""
macros are not savable, but they are semantic in that functions are recorded,
not keypresses. This means that macros can interact with your computer state
such as by looking at what is in the clipboard, are referencing nearby text.
"""

from talon.voice import Context, talon, Key, Str, press
from talon.engine import engine

macro = []
last_actions = None
macro_recording = False


def macro_record(j):
    global macro
    global last_actions
    global macro_recording

    if macro_recording:
        if j["cmd"] == "p.end" and j["grammar"] == "talon":
            new = talon.last_actions
            macro.extend(new)
            last_actions = new


def macro_start(m):
    global macro
    global macro_recording

    macro_recording = True
    macro = []


def macro_stop(m):
    global macro
    global macro_recording

    if macro_recording:
        macro = macro[1:]
        macro_recording = False


def macro_play(m):
    global macro

    macro_stop(None)

    for item in macro:
        for action, rule in item:
            action(rule) or (action, rule)


def macro_print(m):
    global macro

    macro_stop(None)

    actions = []
    for item in macro:
        for action, rule in item:
            if isinstance(action, Key):
                actions.append('press("{}")'.format(action.data))
            elif isinstance(action, Str):
                actions.append('Str("{}")(None)'.format(action.data))
            else:
                # TODO: other conditions
                actions.append(str(action))

    for action in actions:
        Str(action)(None)
        press("enter")


engine.register("post:phrase", macro_record)

ctx = Context("macro")
ctx.keymap(
    {
        "macro (start | record)": macro_start,
        "macro stop": macro_stop,
        "macro play": macro_play,
        "macro print": macro_print,
    }
)
