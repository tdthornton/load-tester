import asyncio
import time
import os
import requests


def fetch(url):
    """Make the request and return the result"""
    start_time = time.monotonic()
    response = requests.get(url)
    request_time = time.monotonic() - start_time

    return {"status": response.status_code, "time": request_time}


async def worker(name, queue, results):
    """ Take unmade requests from a queue and perform the work, add it to results """
    loop = asyncio.get_event_loop()
    while True:

        url = await queue.get()
        if os.getenv("DEBUG"):
            print(f"{name} fetching {url}")

        future_result = loop.run_in_executor(None, fetch, url)
        result = await future_result
        results.append(result)
        queue.task_done()


async def distribute_work(url, requests, concurrency, results):
    """ Divide up the work and collect final results """

    queue = asyncio.Queue()

    for _ in range(requests):
        queue.put_nowait(url)

    tasks = []

    for i in range(concurrency):
        task = asyncio.create_task(worker(f"worker {i+1}", queue, results))
        tasks.append(task)

    start = time.monotonic()
    await queue.join()
    total_time = time.monotonic() - start

    for task in tasks:
        task.cancel()

    print(
        f"{concurrency} workers took {total_time} seconds to complete {len(results)} jobs"
    )

    return total_time


def assault(url, requests, concurrency):
    """ Orchestrates making requests """

    results = []

    total_time = asyncio.run(distribute_work(url, requests, concurrency, results))
    return (total_time, results)
