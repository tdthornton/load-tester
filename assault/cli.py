import click
import json
import sys
from .http import assault
from .stats import Results
from typing import io


@click.command()
@click.option("--requests", "-r", default=500, help="number of requests")
@click.option("--concurrency", "-c", default=1, help="number of concurrent requests")
@click.option("--json-file", "-j", default=None, help="path to output json file")
@click.argument("url")
def cli(requests, concurrency, json_file, url):
    output_file = None
    if json_file:
        try:
            output_file = open(json_file, "w")
        except:
            print(f"Unable to open file {json_file}")
            sys.exit(1)
    print(f"requests:  {requests}")
    print(f"concurrency:  {concurrency}")
    print(f"json-file:  {json_file}")
    print(f"url:  {url}")
    total_time, request_dicts = assault(url, requests, concurrency)

    results = Results(total_time, request_dicts)
    display(results, output_file)


def display(results: Results, json_file: io):
    if json_file:
        json.dump(
            {
                "successful_requests": results.successful(),
                "slowest": results.slowest(),
                "fastest": results.fastest(),
                "average": results.average(),
                "per_minute": results.requests_per_minute(),
                "per_second": results.requests_per_second(),
            },
            json_file
        )
        json_file.close()
        print(".... done! Completed output to json.")
    else:
        print(".... done!")
        print("--- results ---")
        print(f"Successful requests:\t {results.successful()}")
        print(f"Fastest response:\t {results.fastest()}")
        print(f"Slowest response:\t {results.slowest()}")
        print(f"Average response:\t {results.average()}")
        print(f"Requests per minute:\t {results.requests_per_minute()}")
        print(f"Requests per second:\t {results.requests_per_second()}")
    pass
