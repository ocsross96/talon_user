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

JS_EXTENSIONS = (".js", ".jsx", ".njk")

context = Context("javascript", func=is_filetype(JS_EXTENSIONS))


def remove_spaces_around_dashes(m):
    words = parse_words(m)
    s = " ".join(words)
    s = s.replace(" – ", "-")
    insert(s)


def CursorText(s):
    left, right = s.split("{.}", 1)
    return [left + right, Key(" ".join(["left"] * len(right)))]


context.keymap(
    {
        "const [<dgndictation>]": ["const ", text],
        "let [<dgndictation>]": ["let ", text],
        "static": "static ",
        "args": ["()", Key("left")],
        # "block": [" {}", Key("left enter enter up tab")],
        "empty array": "[]",
        "empty object": "{}",
        # "call": "()",
        "state func": "function ",
        "state return": "return ",
        "state constructor": "constructor ",
        "state if": ["if ()", Key("left")],
        "state else": " else ",
        "state else if": [" else if ()", Key("left")],
        "state while": ["while ()", Key("left")],
        "state for": ["for ()", Key("left")],
        "state switch": ["switch ()", Key("left")],
        "state case": ["case \nbreak;", Key("up")],
        "state goto": "goto ",
        "state important": "import ",
        "state class": "class ",
        "state extends": "extends ",
        "state super": "super",
        "comment js": "// ",
        "word no": "null",
        "arrow": " => ",
        "assign": " = ",
        "asink": " async ",
        "op (minus | subtract)": " - ",
        "op (plus | add)": " + ",
        "op (times | multiply)": " * ",
        "op divide": " / ",
        "op mod": " % ",
        "[op] (minus | subtract) equals": " -= ",
        "[op] (plus | add) equals": " += ",
        "[op] (times | multiply) equals": " *= ",
        "[op] divide equals": " /= ",
        "[op] mod equals": " %= ",
        "(op | is) greater [than]": " > ",
        "(op | is) less [than]": " < ",
        "(op | is) equal": " === ",
        "(op | is) not equal": " !== ",
        "(op | is) greater [than] or equal": " >= ",
        "(op | is) less [than] or equal": " <= ",
        "(op (power | exponent) | to the power [of])": " ** ",
        "op and": " && ",
        "op or": " || ",
        # utility snippets
        "log": "log",
        "class name": "className",

        # commands for vanilla dom interaction
        "document query selector": "document.querySelector",

        # commands for es6 imports
        "import react helmet": "import Helmet from 'react-helmet';",
        "import react router": "import { } from 'react-router-dom';",
        "import react": "import React from 'react';",

        "import prop types": "import PropTypes from 'prop-types';",
        "import CSS module": "import style from './style.module.scss';",
        "import classNames": "import classNames from 'classnames';",
        "import <dgndictation>": ["import ", text, " from ", Key("command right")],
        "import": "import",

        # commands for react
        "react fragment": ["<></>", Key("left left left")],
        "react tag": ["< />", Key("left left left")],
        "react clack": "onClick",

        "react component": ["React.Component ", Key("left")],
        "react prop <dgndictation>": [text, "="],
        "react you state ": "useState",
        "react (use reducer | use reducer)": "useReducer",
        "react (use context | theseContact)": "useContext",

        "prop types upper": "PropTypes",
        "prop types lower": "propTypes",

        # misc
        "new regular expression constructor": ["new RegExp()", Key("left")],
        "(console.log | console log)": ["console.log();", Key("left"), Key("left")]
    }
)
