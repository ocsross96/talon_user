from talon.voice import Context, Key, press, Str
from ..utils import parse_words_as_integer, repeat_function, optional_numerals, text

context = Context("VSCode", bundle="com.microsoft.VSCode")


def jump_to_line(m):
    line_number = parse_words_as_integer(m._words[1:])

    if line_number is None:
        return

    # Zeroth line should go to first line
    if line_number == 0:
        line_number = 1

    press("cmd-g")
    Str(str(line_number))(None)
    press("enter")


def jump_tabs(m):
    line_number = parse_words_as_integer(m._words[1:])

    if line_number is None:
        return

    for i in range(0, line_number):
        press("cmd-alt-right")


def jump_to_next_word_instance(m):
    press("escape")
    press("cmd-f")
    Str(" ".join([str(s) for s in m.dgndictation[0]._words]))(None)
    press("return")


def select_lines_function(m):
    divider = 0
    for word in m._words:
        if str(word) == "until":
            break
        divider += 1
    line_number_from = int(str(parse_words_as_integer(m._words[2:divider])))
    line_number_until = int(str(parse_words_as_integer(m._words[divider + 1 :])))
    number_of_lines = line_number_until - line_number_from

    press("cmd-g")
    Str(str(line_number_from))(None)
    press("enter")
    for i in range(0, number_of_lines + 1):
        press("shift-down")


context.keymap(
    {
        # Selecting text
        "select line"
        + optional_numerals
        + "until"
        + optional_numerals: select_lines_function,
        # Finding text
        "find": Key("cmd-f"),
        "find next <dgndictation>": jump_to_next_word_instance,
        # Clipboard
        "clone": Key("alt-shift-down"),
        # Navigation
        "line" + optional_numerals: jump_to_line,
        "Go to line": Key("ctrl-g"),
        # "line up" + optional_numerals: repeat_function(2, "alt-up"),
        # "line down" + optional_numerals: repeat_function(2, "alt-down"),
        # Navigating Interface
        "explore tab": Key("shift-cmd-e"),
        "search tab": Key("shift-cmd-f"),
        "debug tab": Key("shift-cmd-d"),
        "source control tab": Key("shift-ctrl-g"),
        "extensions tab": Key("shift-cmd-x"),
        "go to file <dgndictation>": [Key("cmd-p"), text],
        "master": Key("cmd-p"),
        # tabbing
        # "stiffy": Key("cmd-alt-left"),
        "next tab | goneck": Key("cmd-alt-right"),
        # "stippy": Key("cmd-alt-right"),
        "last tab | gopreev": Key("cmd-alt-left"),
        "new tab | new file": Key("cmd-n"),
        "jump" + optional_numerals: jump_tabs,
        # Menu
        "save": Key("cmd+s"),
        "open": Key("cmd+o"),
        "close": Key("cmd-w"),
        # editing
        # "bracken": [Key("cmd-shift-ctrl-right")],

        "[switch] line up" + optional_numerals: repeat_function(2, "alt-up"),
        "[switch] line down" + optional_numerals: repeat_function(2, "alt-down"),
        "copy [line] down": Key('shift-alt-down'),
        "copy [line] up": Key('shift-alt-up'),
        "delete line": Key('cmd-shift-k'),
        "line below": Key('cmd-enter'),
        "line above": Key('cmd-shift-enter'),  
        "indent": [Key('cmd-left'), Key('tab')],
        "outdent": [Key('cmd-left'), Key('shift-tab')],
        "match (bracket | pair)": Key('cmd-shift-\\'),

        # Rich languages editing
        "[trigger] suggestion": Key('ctrl-space'),
        "format document": Key('shift-alt-f'),
        "format selection": Key('cmd-k cmd-f'),

        # Editor management
        "new window": Key('shift-cmd-n'),
        # "close editor": Key('cmd-w'),
        "close folder": Key('cmd-k f'),
        "split (editor | screen)": Key('cmd-/'),
        "first (pane | group)": Key('cmd-1'),
        "second (pane | group)": Key('cmd-2'),
        "third (pane | group)": Key('cmd-3'),
        "next pane": Key('cmd-k cmd-shift-right'),
        "(prior | previous | un) pane": Key('cmd-k cmd-shift-left'),
        # "push pane left": Key('ctrl-cmd-left'),
        # "push pane right": Key('ctrl-cmd-right'),

        # various
        "comment": Key("cmd-/"),
        "search all": Key("cmd-shift-f"),
        "(drop-down | drop)": Key("ctrl-space"),

        # terminal
        "terminal": Key('ctrl-`'),
        #"npm start": "npm start",
        #"npm run develop": "npm run dev",
    }
)
