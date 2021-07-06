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
double_layer_thick=2 * layer_thick
num_layers_front_vert = 4
num_layers_front_hori = 5
num_layers_front=num_layers_front_vert + num_layers_front_hori
num_double_layers_back=5
num_layers = num_layers_front + 2 * num_double_layers_back
back_start=num_layers_front * layer_thick
scint_width=50.
numBarsFront=8
numBarsBack=12
scint_front_vertical_x=numBarsFront * scint_width
scint_front_vertical_y=scint_bar_length
scint_front_horizontal_x=scint_bar_length
scint_front_horizontal_y=numBarsFront * scint_width
scint_back_vertical_x=numBarsBack * scint_width
scint_back_vertical_y=scint_bar_length
scint_back_horizontal_x=scint_bar_length
scint_back_horizontal_y=numBarsBack * scint_width
dx=3000.
dy=3000.
dz=num_layers_front * layer_thick + num_double_layers_back * double_layer_thick

# Solids
front_vertical_scint_box = {"width": scint_front_vertical_x, "height": scint_front_vertical_y}
front_horizontal_scint_box = {"width": scint_front_horizontal_x, "height": scint_front_horizontal_y}
back_vertical_scint_box = {"width": scint_back_vertical_x, "height": scint_back_vertical_y}
back_horizontal_scint_box = {"width": scint_back_horizontal_x, "height": scint_back_horizontal_y}
air_box = {"width": dx, "height": dy, "depth": air_thick}
prototype_Box={"width": dx, "height": dy, "depth": dz}
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
distance_to_subsequent_scint_layer=np.array([0., 0., double_layer_thick])
front_horizontal_scint_physvols=[
    physical_volume(position=position_of_first_front_horizontal_scint_layer + (i - 1) * distance_to_subsequent_scint_layer,
                    name="front_horizontal_scint_physvol", CopyNumber=2*i - 1
                    )
    for i in range(1,num_layers_front_hori + 1)
]
front_vertical_scint_physvols=[
    physical_volume(position=position_of_first_front_vertical_scint_layer + (i - 1) * distance_to_subsequent_scint_layer,
                    name="front_vertical_scint_physvol", CopyNumber=2*i
                    )
    for i in range(1,num_layers_front_vert + 1)
]
back_vertical_scint_physvols=[
    physical_volume(position=position_of_first_back_vertical_scint_layer + (i - 1) * distance_to_subsequent_scint_layer,
                    name="back_vertical_scint_physvol", CopyNumber=2*i + num_layers_front - 1
                    )
    for i in range(1,num_double_layers_back+ 1)
]

back_horizontal_scint_physvols=[
    physical_volume(position=position_of_first_back_horizontal_scint_layer + (i - 1) * distance_to_subsequent_scint_layer,
                    name="back_horizontal_scint_physvol", CopyNumber=2*i + num_layers_front
                    )
    for i in range(1,num_double_layers_back+ 1)
]

def absorber_copynumbers():
    return [absorber_physvols[i].CopyNumber  for i in range(0, num_layers)]

def front_horizontal_copynumbers():
    return [front_horizontal_scint_physvols[i].CopyNumber  for i in range(0, num_layers_front_hori)]

def front_vertical_copynumbers():
    return [front_vertical_scint_physvols[i].CopyNumber  for i in range(0, num_layers_front_vert)]

def back_horizontal_copynumbers():
    return [back_horizontal_scint_physvols[i].CopyNumber  for i in range(0, num_double_layers_back)]

def back_vertical_copynumbers():
    return [back_vertical_scint_physvols[i].CopyNumber  for i in range(0, num_double_layers_back)]


def front_horizontal_depths():
    return [front_horizontal_scint_physvols[i].depth  for i in range(0, num_layers_front_hori)]

def front_vertical_depths():
    return [front_vertical_scint_physvols[i].depth  for i in range(0, num_layers_front_vert)]

def back_horizontal_depths():
    return [back_horizontal_scint_physvols[i].depth  for i in range(0, num_double_layers_back)]

def back_vertical_depths():
    return [back_vertical_scint_physvols[i].depth  for i in range(0, num_double_layers_back)]
