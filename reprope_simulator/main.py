
from math import sqrt

import plotly.express as px
import plotly.graph_objects as go

# df = px.data.gapminder().query("country=='Brazil'")
# print(df)


# d = ((x2 - x1)2 + (y2 - y1)2 + (z2 - z1)2)1/2
def calculate_distance_between_points(point_a, point_b):
    delta_x = point_b[0] - point_a[0]
    delta_y = point_b[1] - point_a[1]
    delta_z = point_b[2] - point_a[2]
    return sqrt(delta_x ** 2 + delta_y ** 2 + delta_z ** 2)

def line_from_points(point_a, point_b, name=None):
    line = go.Scatter3d(x=[point_a[0], point_b[0]], y=[point_a[1], point_b[1]], z=[point_a[2], point_b[2]])
    if name:
        line.name = name
    return line

max_x = 260
max_y = 260
max_z = 240

head_x = 40
head_y = 40
head_z = 40

pulley_distance_from_corner = 20 + 15 + 42/2
pulley_distance_from_frame = 15

head_pos_x = pulley_distance_from_corner
head_pos_y = pulley_distance_from_corner
head_pos_z = 0

rope_points = dict()

for c in 'abcdefgh':
    rope_points[c] = dict()

rope_points['a']['head'] = [head_pos_x, head_pos_y + head_y, head_pos_z + head_z]
rope_points['a']['top'] = [pulley_distance_from_frame, pulley_distance_from_corner, max_z]
rope_points['b']['head'] = [head_pos_x + head_x, head_pos_y, head_pos_z]
rope_points['b']['top'] = [pulley_distance_from_corner, pulley_distance_from_frame, max_z]
rope_points['c']['head'] = [head_pos_x, head_pos_y, head_pos_z + head_z]
rope_points['c']['top'] = [max_x - pulley_distance_from_corner, pulley_distance_from_frame, max_z]
rope_points['d']['head'] = [head_pos_x + head_x, head_pos_y + head_y, head_pos_z]
rope_points['d']['top'] = [max_x - pulley_distance_from_frame, pulley_distance_from_corner, max_z]
rope_points['e']['head'] = [head_pos_x + head_x, head_pos_y, head_pos_z + head_z]
rope_points['e']['top'] = [max_x - pulley_distance_from_frame, max_y - pulley_distance_from_corner, max_z]
rope_points['f']['head'] = [head_pos_x, head_pos_y + head_y, head_pos_z]
rope_points['f']['top'] = [max_x - pulley_distance_from_corner, max_y - pulley_distance_from_frame, max_z]
rope_points['g']['head'] = [head_pos_x + head_x, head_pos_y + head_y, head_pos_z + head_z]
rope_points['g']['top'] = [pulley_distance_from_corner, max_y - pulley_distance_from_frame, max_z]
rope_points['h']['head'] = [head_pos_x, head_pos_y, head_pos_z]
rope_points['h']['top'] = [pulley_distance_from_frame, max_y - pulley_distance_from_corner, max_z]

ropes = dict()

for c in 'abcdefgh':
    ropes[c] = line_from_points(rope_points[c]['head'], rope_points[c]['top'], name="Rope %s" % c)
    print("Rope %s distance: %s" % (c, calculate_distance_between_points(rope_points[c]['head'], rope_points[c]['top'])))

data=[
    # Frame
                go.Scatter3d(x=[0, max_x], y=[0, 0], z=[max_z, max_z]),
                go.Scatter3d(x=[0, 0], y=[0, max_y], z=[max_z, max_z]),
                go.Scatter3d(x=[0, max_x], y=[max_y, max_y], z=[max_z, max_z]),
                go.Scatter3d(x=[max_x, max_x], y=[max_y, 0], z=[max_z, max_z]),
                go.Scatter3d(x=[0, max_x], y=[0, 0], z=[0, 0]),
                go.Scatter3d(x=[0, 0], y=[0, max_y], z=[0, 0]),
                go.Scatter3d(x=[0, max_x], y=[max_y, max_y], z=[0, 0]),
                go.Scatter3d(x=[max_x, max_x], y=[max_y, 0], z=[0, 0]),
                go.Scatter3d(x=[0, 0], y=[0, 0], z=[0, max_z]),
                go.Scatter3d(x=[max_x, max_x], y=[0, 0], z=[0, max_z]),
                go.Scatter3d(x=[max_x, max_x], y=[max_y, max_y], z=[0, max_z]),
                go.Scatter3d(x=[0, 0], y=[max_y, max_y], z=[0, max_z]),

    # Head
                go.Scatter3d(x=[head_pos_x, head_pos_x + head_x], y=[head_pos_y, head_pos_y], z=[head_pos_z + head_z, head_pos_z + head_z]),
                go.Scatter3d(x=[head_pos_x, head_pos_x], y=[head_pos_y, head_pos_y + head_y], z=[head_pos_z + head_z, head_pos_z + head_z]),
                go.Scatter3d(x=[head_pos_x, head_pos_x + head_x], y=[head_pos_y + head_y, head_pos_y + head_y], z=[head_pos_z + head_z, head_pos_z + head_z]),
                go.Scatter3d(x=[head_pos_x + head_x, head_pos_x + head_x], y=[head_pos_y + head_y, head_pos_y], z=[head_pos_z + head_z, head_pos_z + head_z]),
                go.Scatter3d(x=[head_pos_x, head_pos_x + head_x], y=[head_pos_y, head_pos_y], z=[head_pos_z, head_pos_z]),
                go.Scatter3d(x=[head_pos_x, head_pos_x], y=[head_pos_y, head_pos_y + head_y], z=[head_pos_z, head_pos_z]),
                go.Scatter3d(x=[head_pos_x, head_pos_x + head_x], y=[head_pos_y + head_y, head_pos_y + head_y], z=[head_pos_z, head_pos_z]),
                go.Scatter3d(x=[head_pos_x + head_x, head_pos_x + head_x], y=[head_pos_y + head_y, head_pos_y], z=[head_pos_z, head_pos_z]),
                go.Scatter3d(x=[head_pos_x, head_pos_x], y=[head_pos_y, head_pos_y], z=[head_pos_z, head_pos_z + head_z]),
                go.Scatter3d(x=[head_pos_x + head_x, head_pos_x + head_x], y=[head_pos_y, head_pos_y], z=[head_pos_z, head_pos_z + head_z]),
                go.Scatter3d(x=[head_pos_x + head_x, head_pos_x + head_x], y=[head_pos_y + head_y, head_pos_y + head_y], z=[head_pos_z, head_pos_z + head_z]),
                go.Scatter3d(x=[head_pos_x, head_pos_x], y=[head_pos_y + head_y, head_pos_y + head_y], z=[head_pos_z, head_pos_z + head_z]),

    # Ropes
                ropes['a'],
                ropes['b'],
                ropes['c'],
                ropes['d'],
                ropes['e'],
                ropes['f'],
                ropes['g'],
                ropes['h'],
]

fig = go.Figure(data)
fig.show()