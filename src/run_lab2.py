from spatial import PointSet

pointset = PointSet.from_csv("data/points.csv")
print(f"Loaded {pointset.count()} points.")

bbox = pointset.bbox()
bbox_lon_lat = {
    "min_lon": bbox[0],
    "min_lat": bbox[1],
    "max_lon": bbox[2],
    "max_lat": bbox[3],
}
print(f"Bounding box: {bbox_lon_lat}")

pois = pointset.filter_by_tag("poi")
print(f"Found {pois.count()} POIs.")