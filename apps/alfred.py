from talon.voice import Context, Key
from ..utils import text

ctx = Context("alfred")

keymap = {
    # scrolling
    "alfred (jira|jury|juror)": [Key("alt-space"), Key("j"), Key("i"), Key("r"), Key("a")],
    "alfred": Key("alt-space"),
}

ctx.keymap(keymap)