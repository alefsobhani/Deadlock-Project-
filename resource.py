class Resource:
    def __init__(self, name, total_units):
        self.name = name
        self.total_units = total_units
        self.allocated_units = 0

    def allocate(self, units):
        if self.allocated_units + units <= self.total_units:
            self.allocated_units += units
            return True
        return False

    def release(self, units):
        if units <= self.allocated_units:
            self.allocated_units -= units
            return True
        return False

    def is_available(self, units):
        return (self.total_units - self.allocated_units) >= units

import threading
import time

class Process(threading.Thread):
    def __init__(self, name, resources_needed):
        threading.Thread.__init__(self)
        self.name = name
        self.resources_needed = resources_needed

    def run(self):
        while True:
            acquired = all([resource.allocate(units) for resource, units in self.resources_needed.items()])
            if acquired:
                print(f"{self.name} acquired all resources and is executing.")
                time.sleep(1)
                for resource, units in self.resources_needed.items():
                    resource.release(units)
                print(f"{self.name} released all resources.")
                break
            else:
                for resource, units in self.resources_needed.items():
                    resource.release(units)
                print(f"{self.name} could not acquire all resources, retrying.")
                time.sleep(1)

resource1 = Resource('Resource1', 2)
resource2 = Resource('Resource2', 1)

p1 = Process('Process1', {resource1: 1, resource2: 1})
p2 = Process('Process2', {resource1: 1, resource2: 1})

p1.start()
p2.start()

p1.join()
p2.join()
