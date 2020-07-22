from abc import ABC, abstractmethod
# DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3, and in 3.9 it will stop working
# from collections import Iterable
##
from collections.abc import Iterable
from concurrent.futures import Future


import re
import time
from typing import Optional

wheelme_regex = re.compile("(^wheel.me|^wheelme) ")


def wheelme_description(line: str) -> Optional[str]:
    """
    >>> wheelme_description('wheelme is a great')
    'is a great'
    >>> wheelme_description('wheel.me is an exciting')
    'is an exciting'
    """
    m = re.search(wheelme_regex, line)
    if m:
        return re.sub(wheelme_regex, '', line)


class Kafka(ABC):
    @abstractmethod  # Or we can delete @abstractmethod to not define SubKafka
    def produce(self, topic: str, message: bytes):
        pass

    def flush(self):
        time.sleep(1)

# Needed to define class SubKafka to able to use produce method of class Kafka
class SubKafka(Kafka):

    def produce(self, topic: str, message: bytes):
        super().produce(topic, message)


def get_kafka() -> Kafka:
    return SubKafka()


# Replace Iterable[str] to Iterable (type chacking problem)
async def produce_wheelme_lines(lines: Iterable) -> Future:
    """
    use :func:`wheelme_description` to find "wheelme" lines and produce them with Kafka (use :func:`get_kafka`)
    Returns:
        a concurrent.futures.Future with the kafka.flush called
    """
    
    from concurrent.futures import ThreadPoolExecutor
    
    k = get_kafka()
    to_produce = []
    for line in lines:
        wheelme_line = wheelme_description(line)
        if wheelme_line:
            k.produce(topic="wheelme", message=wheelme_line)
            to_produce.append(wheelme_line)

    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(k.flush) for line in to_produce]

    return futures
