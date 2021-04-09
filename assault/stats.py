from typing import List, Dict
from statistics import mean


class Results:
    def __init__(self, total_time: float, requests: List[Dict]):
        self.total_time = total_time
        self.requests = sorted(requests, key=lambda r: r["time"])

    def slowest(self) -> float:
        """
        Returns the slowest request completion time.

        >>> results = Results(10.6, [
        ... {
        ... "status":200,
        ... "time":3.4
        ... },
        ... {
        ... "status":200,
        ... "time":3.9
        ... },
        ... {
        ... "status":200,
        ... "time":3.1
        ... },
        ... {
        ... "status":200,
        ... "time":3.1
        ... },
        ... ])
        >>> results.slowest()
        3.9
        """
        return self.requests[-1]["time"]

    def fastest(self) -> float:
        """
        Returns the fastest request completion time.

        >>> results = Results(10.6, [
        ... {
        ... "status":200,
        ... "time":3.4
        ... },
        ... {
        ... "status":200,
        ... "time":3.9
        ... },
        ... {
        ... "status":200,
        ... "time":3.1
        ... },
        ... {
        ... "status":200,
        ... "time":3.1
        ... },
        ... ])
        >>> results.fastest()
        3.1
        """
        return self.requests[0]["time"]

    def average(self) -> float:
        """
        Returns the average request completion time.

        >>> results = Results(10.6, [
        ... {
        ... "status":200,
        ... "time":3.4
        ... },
        ... {
        ... "status":200,
        ... "time":3.9
        ... },
        ... {
        ... "status":200,
        ... "time":3.1
        ... },
        ... {
        ... "status":200,
        ... "time":3.1
        ... },
        ... ])
        >>> results.average()
        3.375
        """
        return mean(r["time"] for r in self.requests)

    def successful(self) -> int:
        """
        Returns the total number of 200 requests.

        >>> results = Results(10.6, [
        ... {
        ... "status":200,
        ... "time":3.4
        ... },
        ... {
        ... "status":200,
        ... "time":3.9
        ... },
        ... {
        ... "status":200,
        ... "time":3.1
        ... },
        ... {
        ... "status":403,
        ... "time":3.1
        ... },
        ... ])
        >>> results.successful()
        3
        """
        return len([r for r in self.requests if r["status"] in range(200, 299)])

    def requests_per_minute(self) -> int:
        """
        Returns the average requests per minute speed of the run.

        >>> results = Results(7, [
        ... {
        ... "status":200,
        ... "time":1
        ... },
        ... {
        ... "status":200,
        ... "time":4
        ... },
        ... {
        ... "status":200,
        ... "time":1
        ... },
        ... {
        ... "status":403,
        ... "time":1
        ... },
        ... ])
        >>> results.requests_per_minute()
        34
        """
        return round(60 * len(self.requests)/ self.total_time)


    def requests_per_second(self) -> int:
        """
        Returns the average requests per second speed of the run.

        >>> results = Results(7.5, [
        ... {
        ... "status":200,
        ... "time":3.4
        ... },
        ... {
        ... "status":200,
        ... "time":3.9
        ... },
        ... {
        ... "status":200,
        ... "time":0.1
        ... },
        ... {
        ... "status":403,
        ... "time":0.1
        ... },
        ... ])
        >>> results.requests_per_second()
        1
        """
        return  round(len(self.requests) / self.total_time)
