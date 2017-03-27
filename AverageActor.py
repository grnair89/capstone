from calvin.actor.actor import Actor, condition, guard, ActionResult
from calvin.runtime.north.calvin_token import ExceptionToken


class AverageActor(Actor):

    """
    Divides input on port 'dividend' with input on port 'divisor'
    Inputs :
        temp1 :
    Output :
        result:
    """

    def init(self):
        self.counter = 0
        self.result = 0
        self.type = ''

    @guard(lambda self: self.counter <= 10)
    @condition(action_input=['temp1'], action_output=['result'])
    def divide(self, temperatures):
        self.result = (( self.result * self.counter ) + temperatures[0] )/ (self.counter + 1)
        self.counter += 1
        self.type = temperatures[1]
        return ActionResult(production=(['ignore','train'],))
        #print(str(self.result),str(temperatures), str(self.counter))

    @guard(lambda self: self.counter > 10)
    @condition(action_input=[], action_output=['result'])
    def answer(self):
        result = self.result
        self.counter = 0
        self.result = 0
        return ActionResult(production=([result, self.type],))

    action_priority = (divide,answer)