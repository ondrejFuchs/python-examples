from ex1.id_generator import unique_id
from ex1.instance_filter import filter_on


def test_unique_id():
    ids = set()
    unique_id_count = 10000
    for _ in range(unique_id_count):
        ids.add(unique_id())
    assert len(ids) == unique_id_count


def test_filter_on_generator():
    inp = [1, 0.0, "zero", 100_000, object(), "friend"]
    out = ["zero", "friend"]
    assert list(filter_on(inp, str)) == out
