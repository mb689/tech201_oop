# Methods

class MethodExamples:

    def __init__(self):
        self._this_can_be_accessed_easily = "Hi, I am easily found!"


x = MethodExamples()

print(x.get_this_can_be_accessed_easily)
x.set_this_can_be_accessed_easily = "I have been changed!"
print(x.get_this_can_be_accessed_easily)