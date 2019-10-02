# kindly adapted from @jsenecal - https://talonvoice.slack.com/archives/C9MHQ4AGP/p1568388969067200

from talon.voice import Context, Rep, talon, generic
from ..utils import parse_words_as_integer
class MyRep(generic):
   def __call__(self, m):
       tmp = []
       if self.ctx.last_action:
           for action, rule in self.ctx.last_action:
               for i in range(self.data):
                   act = action(rule) or (action, rule)
               tmp.append(act)
       return tmp
ctx = Context("repeater")
def repeat(m):
   repeat_count = parse_words_as_integer(m._words[1:])
   if repeat_count != None and repeat_count >= 1:
       repeater = MyRep(repeat_count)
       repeater.ctx = talon
       return repeater(None)
ctx.keymap({
   "wink": MyRep(1),
   "soup": MyRep(2),
   "trace": MyRep(3),
   "quarr": MyRep(4),
   "fypes": MyRep(5),
   "repeat (0 | oh | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)++": repeat,
})
