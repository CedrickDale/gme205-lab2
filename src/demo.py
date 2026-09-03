from spatial import Point 

p = Point("A", 121.0, 14.6)
print(p.id, p.lon, p.lat)
print(p.to_tuple())

q = Point("X", 122.0, 14.0) # change lon to 122.0 to proceed to distance test
print(q.id, q.lon, q.lat)


# ----------------------------------
# Distance Test
# ----------------------------------

print("------------------------------")
print("Distance Test")

p = Point("A", 121.0, 14.6)
print(p.id, p.lon, p.lat)

q = Point("B", 129.0, 17.0)
print(q.id, q.lon, q.lat)

print(p.distance_to(q))

