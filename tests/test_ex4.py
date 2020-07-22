import pytest

from ex4.wheelme_lines import Kafka


lines = [
    "wheel.me is an exciting",
    "no wheel me line description",
    "another line",
    "wheelme is a great",
]


@pytest.fixture()
def mock_kafka() -> Kafka:
    from ex4.wheelme_lines import SubKafka
    return SubKafka()


"""
1. Normal async test
write a test_produce_wheelme_lines(mock_kafka):
which uses the `lines` above and checks the mock_kafka that the produce has been called 2 times

2. Parameterized async test
Write a parameterized `async def test_produce_wheelme_lines_param` which use
@pytest.mark.parametrize
to test the :func:`produce_wheelme_lines`
"""

lines1 = [
    "test1",
    "test2",
    "test3"
]

lines2 = [
    "wheelme is a great",
    "wheelme is a great",
    "wheelme is a great"
]


def test_produce_wheelme_lines(mock_kafka):
    from ex4.wheelme_lines import wheelme_description
    count_call = 0
    expected_call = 2
    for line in lines:
        if wheelme_description(line):
            mock_kafka.produce(topic="wheelme", message=line)
            count_call += 1

    assert count_call == expected_call


@pytest.mark.parametrize('lines, calls', [(lines1, 0), (lines2, 3)])
@pytest.mark.asyncio
async def test_produce_wheelme_lines_param(lines, calls):
    from ex4.wheelme_lines import produce_wheelme_lines
    futures = await produce_wheelme_lines(lines)
    assert len(futures) == calls
