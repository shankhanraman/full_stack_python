# Coroutines in Python are a key component of asynchronous programming, enabling efficient cooperative multitasking. Unlike regular functions (subroutines) which execute from start to finish without interruption, coroutines can be paused during execution and resumed later from where they left off. This allows for non-blocking operations, particularly useful for I/O-bound tasks where a program might otherwise spend significant time waiting for external resources.
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()
    
async def main():
    urls = ["https://httpbin.org/delay/2" ]*3
    async with aiohttp.ClientSession() as session:
        tasks =[fetch_url(session,url) for url in urls]
        await asyncio.gatther(*tasks) # *tasks shorthand nottaion for unopackig things as e getting an array [t1,t2,t3]

asyncio.run(main())

# Blocking  vs Non-Blocking
# Blocking operations halt the execution of a program until a particular task is completed. 
# For example, when a program reads data from a file or waits for a network response, it cannot proceed to the next line of code until that operation finishes. 
# This can lead to inefficiencies, especially in I/O-bound applications where waiting times can be significant.
# Non-blocking operations, on the other hand, allow a program to initiate a task and then move on to other tasks without waiting for the initial task to complete.
# In Python, this is often achieved using asynchronous programming techniques, such as coroutines with the `async` and `await` keywords. 
# Non-blocking code can improve performance and responsiveness, particularly in applications that handle multiple I/O operations concurrently.

