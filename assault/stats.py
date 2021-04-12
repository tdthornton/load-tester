from typing import List, Dict
from statistics import mean


class Results:
    def __init__(self, total_time: float, requests: List[Dict]):
        self.total_time = total_time
        self.requests = sorted(requests, key=lambda r: r["time"])

    def slowest(self) -> float:
        """
        Returns the slowest request completion time.
        """
        if len(self.requests) == 0:
            return 0
        return self.requests[-1]["time"]

    def fastest(self) -> float:
        """
        Returns the fastest request completion time.
        """
        if len(self.requests) == 0:
            return 0
        return self.requests[0]["time"]

    def average(self) -> float:
        """
        Returns the average request completion time.
        """
        if len(self.requests) == 0:
            return 0
        return mean(r["time"] for r in self.requests)

    def successful(self) -> int:
        """
        Returns the total number of 200 requests.
        """
        if len(self.requests) == 0:
            return 0
        return len([r for r in self.requests if r["status"] in range(200, 300)])

    def requests_per_minute(self) -> int:
        """
        Returns the average requests per minute speed of the run.
        """
        if len(self.requests) == 0 or self.total_time == 0:
            return 0
        return round(60 * len(self.requests) / self.total_time)

    def requests_per_second(self) -> int:
        """
        Returns the average requests per second speed of the run.
        """
        if len(self.requests) == 0 or self.total_time == 0:
            return 0
        return round(len(self.requests) / self.total_time)
