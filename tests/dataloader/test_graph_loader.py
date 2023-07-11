import pytest
from spatialdata.dataloader import build_graph
from spatialdata.datasets import blobs

sdata = blobs()


@pytest.mark.parametrize(
    "method, kwargs", [("knn", {"k": 2}), ("radius", {"max_distance": 50}), ("expansion", {"max_distance": 50}), ("expansion", {"percentile": 50})]
)
def test_build_graph(method, kwargs):
    gdf = sdata["blobs_circles"]
    build_graph(gdf=gdf, method=method, **kwargs)


@pytest.mark.parametrize(
    "method, kwargs", [("knn", {"k": 2}), ("radius", {"max_distance": 50}), ("expansion", {"max_distance": 50}), ("invalid")]
)
def test_build_graph_invalid_arguments(method, kwargs):
    gdf = sdata["blobs_circles"]
    if method == "invalid":
        with pytest.raises(AssertionError):
            build_graph(gdf=gdf, method=method, **kwargs)



