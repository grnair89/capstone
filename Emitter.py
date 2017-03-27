from calvin.actor.actor import Actor, manage, condition, guard, ActionResult
import random

class Emitter(Actor):
    """
    Pass on given _data_ every _tick_ seconds
    Inputs:

    Outputs:
        data
    """

    @manage(['tick', 'started', 'low', 'high'])
    def init(self):
        self.tick = 0.01
        self.data = []
        self.timer = None
        self.started = False
        self.low = 30
        self.high = 35
        self.type = 'train'
        self.setup()

    def setup(self):
        self.use('calvinsys.events.timer', shorthand='timer')

    def start(self):
        self.timer = self['timer'].repeat(self.tick)
        self.started = True

    def will_migrate(self):
        if self.timer:
            self.timer.cancel()

    # div.temp1
    # div.result >
    #div : Math.AverageActor()
    def did_migrate(self):
        self.setup()
        if self.started:
            self.start()

    def rand_generator(self, low, high):
        return random.uniform(low, high)

    @guard(lambda self: not self.started)
    @condition([], ['data'])
    def start_timer(self):
        self.start()
        result = self.rand_generator(self.low, self.high)
        return ActionResult(production=([result, self.type],))

    @guard(lambda self: self.timer and self.timer.triggered)
    @condition([], ['data'])
    def trigger(self):
        self.low += 0.1
        self.high += 0.1
        if(self.high > 80):
            self.high = 10
            self.high = 15
            self.type = 'validate'
        result = self.rand_generator(self.low, self.high)
        self.started = False
        return ActionResult(production=([result, self.type],))

    action_priority = (start_timer, trigger)
    requires = ['calvinsys.events.timer']