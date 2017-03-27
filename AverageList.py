from calvin.actor.actor import Actor, condition, guard, ActionResult
from calvin.runtime.north.calvin_token import ExceptionToken

class AverageList(Actor):

    """
    Divides input on port 'dividend' with input on port 'divisor'
    Inputs :
        temp1 : int
    Output :
        ip:string
    """

    def init(self):
        pass

    @condition(action_input=['temp1'], action_output=['ip'])
    def avg(self, temperatures):
        if(temperatures != 'ignore'):
            self.result = sum(temperatures)/ len(temperatures)
        else:
            self.result = ExceptionToken("Division by 0")
        return ActionResult(production=(self.result,))
        #print(str(self.result),str(temperatures), str(self.counter))


    action_priority = (divide,answer)