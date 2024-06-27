In Pyhton, an __init__ class method must never return a value, always having a None as return value. But we can experience the use case where we need to use an asynchronous function inside such method, as to populate an attribute for example. The problem with that is that an asynchronous function automatically returns a Coroutine that needs to be awaited.

To solve this problem, we can define a create() method that overrides the __init__, calling it when we want to instantiate the class, passing to it the class and any other arguments we need.
