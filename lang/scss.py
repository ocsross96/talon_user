from talon.voice import Context, Key, press
import talon.clip as clip
from ..utils import (
    text,
    parse_words,
    parse_words_as_integer,
    insert,
    word,
    join_words,
    is_filetype,
)

SCSS_EXTENSIONS = (".scss")

context = Context("scss", func=is_filetype(SCSS_EXTENSIONS))


context.keymap(
    {
      "responsive medium and above": ["@include responsiveMediumAndAbove() {}", Key("left"), Key("enter")],
      "responsive large and above": ["@include responsiveLargeAndAbove() {}", Key("left"), Key("enter"), Key("enter")]
    }
)