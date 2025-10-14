# async def : declare a coroutine(a special function that can be paused and resumed)
# await : pause the coroutine until the awaited task is complete
# asyncio : built-in library for writing concurrent code using the async/await syntax
# Event loop : the engine that runs and schedules co-routines in python
import asyncio  
async def brew_chai():
    print("Brewing Chai ...")
    await asyncio.sleep(3)
    print("Chai is ready!")

asyncio.run(brew_chai())