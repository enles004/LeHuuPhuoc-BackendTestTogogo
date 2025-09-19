class BusCommand:
    def __init__(self):
        self._handler = {}

    def register(self, command, handler):
        command_name = command.__name__
        self._handler[command_name] = handler

    async def execute(self, command):
        command_name = command.__class__.__name__
        if command_name not in self._handler:
            raise ValueError(f"Command {command_name} not registered")
        handler = self._handler[command_name]
        return await handler.execute(command)
