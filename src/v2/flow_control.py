import time
import board
import countio

class FlowControl:
    def __init__(self, flow_pin):
        self.counter = countio.Counter(flow_pin, edge=countio.Edge.RISE)
        self.ml_count = 2.3

    def wait_until(self,expected_ml, limit = 600):
        current = 0
        expected_counts = expected_ml / self.ml_count
        current_time = time.monotonic()
        self.counter.reset()
        while current < expected_counts and (time.monotonic() - current_time < limit):
            current = self.counter.count
            time.sleep(0.1)
        self.counter.reset()
