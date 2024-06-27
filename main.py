import logging


#  Here we define the class, assigning it to the cls parameter,
# and then returning that instance.
class ExampleClass:
    async def create(cls, *args, **kwargs):
        self = cls()
        self.logger = kwargs.get("logger", logging.getLogger("main_logger"))
        self.asynchronous_result = await self.get_async_result()
        return self

    async def get_async_result(self):
        pass

    def normal_method(self):
        pass


if __name__ == "__main__":
    # Then, we instantiate such class into an object calling that method,
    # passing it the class and any other parameter we need
    example_object = ExampleClass(ExampleClass,
                                  logging.getLogger("main_logger"))

    # Then we can use the object normally
    example_object.normal_method()
