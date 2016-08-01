from blot.assets.base import Aggregate
from blot.utils import generate_cloud, _calculate_totals


def test_calculate_totals():
    ag1 = Aggregate('ag1', assets=[1])
    ag2 = Aggregate('ag2', assets=[1,2])
    totals = _calculate_totals([ag1, ag2])
    assert totals == [[ag2, 2], [ag1, 1]]


def make_aggregates(count):
    aggs = []
    for i in range(count):
        name = "ag{}".format(i)
        assets = list(range(i + 1))
        aggs.append(Aggregate(name, assets))
    return aggs


def test_generate_cloud():
    assets = make_aggregates(3)
    cloud = generate_cloud(assets)
    assert cloud == [
        (assets[2], 1.0),
        (assets[1], 0.9),
        (assets[0], 0.8)]


def test_minsize():
    assets = make_aggregates(3)
    cloud = generate_cloud(assets, minsize=0.5)
    assert cloud == [
        (assets[2], 1.0),
        (assets[1], 0.75),
        (assets[0], 0.5)
    ]


def test_maxsize():
    assets = make_aggregates(3)
    cloud = generate_cloud(assets, maxsize=1.5)
    assert cloud == [
        (assets[2], 1.5),
        (assets[1], 1.15),
        (assets[0], 0.8)
    ]
