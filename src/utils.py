

def update_counter(count, limit=10000):
    if(count>=limit):
        return 1
    else:
        return count + 1
    
def execute_every(counter, period, fun):
    if(counter % period == 0):
        fun()