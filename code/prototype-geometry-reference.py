#!/usr/bin/env python3

# A short script containing representations of the variables that are used in
# the geometry description. Useful for testing and calculations.
#
# Note that all units are in mm

import numpy as np
# Constants
center=np.array([0.,0.,0.])
hadron_calorimeter_pos=np.array([0.,0.,0.])
world_dim=10000.
air_thick=2.
absorber_width=800.
absorber_ears=50.
absorber_thickness=25
scint_thick=20.
scint_bar_length=2000.
layer_thick = absorber_thickness + scint_thick + 2 * air_thick
num_layers_front_vertical = 4
num_layers_front_horizontal = 5
num_layers_front=num_layers_front_vertical + num_layers_front_horizontal
num_layers_back_vertical = 5
num_layers_back_horizontal = 5
num_layers_back=num_layers_back_vertical + num_layers_back_horizontal
num_layers = num_layers_front + num_layers_back
back_start=num_layers_front * layer_thick
scint_bar_width=50.
num_bars_front=8
num_bars_back=12
scint_front_vertical_x=num_bars_front * scint_bar_width
scint_front_vertical_y=scint_bar_length
scint_front_horizontal_x=scint_bar_length
scint_front_horizontal_y=num_bars_front * scint_bar_width
scint_back_vertical_x=num_bars_back * scint_bar_width
scint_back_vertical_y=scint_bar_length
scint_back_horizontal_x=scint_bar_length
scint_back_horizontal_y=num_bars_back * scint_bar_width
dx=3000.
dy=3000.
dz=num_layers * layer_thick

# Solids
front_vertical_scint_box = {"width": scint_front_vertical_x, "height": scint_front_vertical_y}
front_horizontal_scint_box = {"width": scint_front_horizontal_x, "height": scint_front_horizontal_y}
back_vertical_scint_box = {"width": scint_back_vertical_x, "height": scint_back_vertical_y}
back_horizontal_scint_box = {"width": scint_back_horizontal_x, "height": scint_back_horizontal_y}
air_box = {"width": dx, "height": dy, "depth": air_thick}
prototype_box={"width": dx, "height": dy, "depth": dz}
world_box={"width": world_dim, "height": world_dim, "depth": world_dim}

class physical_volume:
    def __init__(self, position, name="", CopyNumber=None):
        self.position=position
        self.name=name
        if CopyNumber is not None:
            self.CopyNumber = CopyNumber
        self.depth=position[2]
    def __repr__(self):
        return str(self.__dict__)

# Physical volumes
position_of_first_absorber_layer= np.array([-absorber_width/2, -absorber_width/2, -dz/2])
distance_to_subsequent_absorber_layer = np.array([0.,0., layer_thick])
first_absorber = physical_volume(position_of_first_absorber_layer)
absorber_physvols=[
    physical_volume(position=position_of_first_absorber_layer + distance_to_subsequent_absorber_layer * i ,
                    name="absorber_physvol", CopyNumber=i)
    for i in range(1, num_layers + 1)
]
position_of_first_front_horizontal_scint_layer = np.array([0.,0., -dz/2 + absorber_thickness + air_thick + scint_thick/2 ])
position_of_first_front_vertical_scint_layer = position_of_first_front_horizontal_scint_layer + [0., 0., layer_thick]
position_of_first_back_vertical_scint_layer =  position_of_first_front_horizontal_scint_layer + [0., 0., back_start]
position_of_first_back_horizontal_scint_layer = position_of_first_back_vertical_scint_layer + [0., 0., layer_thick]
distance_to_subsequent_scint_layer=np.array([0., 0., 2. * layer_thick])
front_horizontal_scint_physvols=[
    physical_volume(position=position_of_first_front_horizontal_scint_layer + (i - 1) * distance_to_subsequent_scint_layer,
                    name="front_horizontal_scint_physvol", CopyNumber=2*i - 1
                    )
    for i in range(1,num_layers_front_horizontal + 1)
]
front_vertical_scint_physvols=[
    physical_volume(position=position_of_first_front_vertical_scint_layer + (i - 1) * distance_to_subsequent_scint_layer,
                    name="front_vertical_scint_physvol", CopyNumber=2*i
                    )
    for i in range(1,num_layers_front_vertical + 1)
]
back_vertical_scint_physvols=[
    physical_volume(position=position_of_first_back_vertical_scint_layer + (i - 1) * distance_to_subsequent_scint_layer,
                    name="back_vertical_scint_physvol", CopyNumber=2*i + num_layers_front - 1
                    )
    for i in range(1,num_layers_back_vertical+ 1)
]

back_horizontal_scint_physvols=[
    physical_volume(position=position_of_first_back_horizontal_scint_layer + (i - 1) * distance_to_subsequent_scint_layer,
                    name="back_horizontal_scint_physvol", CopyNumber=2*i + num_layers_front
                    )
    for i in range(1,num_layers_back_horizontal+ 1)
]

def absorber_copynumbers():
    return [absorber_physvols[i].CopyNumber  for i in range(0, num_layers)]

def front_horizontal_copynumbers():
    return [front_horizontal_scint_physvols[i].CopyNumber  for i in range(0, num_layers_front_horizontal)]

def front_vertical_copynumbers():
    return [front_vertical_scint_physvols[i].CopyNumber  for i in range(0, num_layers_front_vertical)]

def back_horizontal_copynumbers():
    return [back_horizontal_scint_physvols[i].CopyNumber  for i in range(0, num_layers_back_horizontal)]

def back_vertical_copynumbers():
    return [back_vertical_scint_physvols[i].CopyNumber  for i in range(0, num_layers_back_vertical)]


def front_horizontal_depths():
    return [front_horizontal_scint_physvols[i].depth  for i in range(0, num_layers_front_horizontal)]

def front_vertical_depths():
    return [front_vertical_scint_physvols[i].depth  for i in range(0, num_layers_front_vertical)]

def back_horizontal_depths():
    return [back_horizontal_scint_physvols[i].depth  for i in range(0, num_layers_back_horizontal)]

def back_vertical_depths():
    return [back_vertical_scint_physvols[i].depth  for i in range(0, num_layers_back_vertical)]
