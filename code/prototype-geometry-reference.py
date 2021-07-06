#!/usr/bin/env python3

# A short script containing representations of the variables that are used in
# the geometry description. Useful for testing and calculations.
#
# Note that all units are in mm

import numpy as np
# Constants
center=np.array([0.,0.,0.])
identity=np.array([0.,0.,0.])
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
numLayersFront_vert = 4
numLayersFront_hori = 5
numLayersFront=numLayersFront_vert + numLayersFront_hori
numDoubleLayersBack=5
numLayers = numLayersFront + 2 * numDoubleLayersBack
back_start=numLayersFront * layer_thick
scint_width=50.
numBarsFront=8
numBarsBack=12
scint_FrontV_x=numBarsFront * scint_width
scint_FrontV_y=scint_bar_length
scint_FrontH_x=scint_bar_length
scint_FrontH_y=numBarsFront * scint_width
scint_BackV_x=numBarsBack * scint_width
scint_BackV_y=scint_bar_length
scint_BackH_x=scint_bar_length
scint_BackH_y=numBarsBack * scint_width
dx=3000.
dy=3000.
dz=numLayersFront * layer_thick + numDoubleLayersBack * double_layer_thick

# Solids
frontV_ScintBox = {"width": scint_FrontV_x, "height": scint_FrontV_y}
frontH_ScintBox = {"width": scint_FrontH_x, "height": scint_FrontH_y}
backV_ScintBox = {"width": scint_BackV_x, "height": scint_BackV_y}
backH_ScintBox = {"width": scint_BackH_x, "height": scint_BackH_y}
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
    for i in range(1, numLayers + 1)
]
position_of_first_frontH_scint_layer = np.array([0.,0., -dz/2 + absorber_thickness + air_thick + scint_thick/2 ])
position_of_first_frontV_scint_layer = position_of_first_frontH_scint_layer + [0., 0., layer_thick]
position_of_first_backV_scint_layer =  position_of_first_frontH_scint_layer + [0., 0., back_start]
position_of_first_backH_scint_layer = position_of_first_backV_scint_layer + [0., 0., layer_thick]
distance_to_subsequent_scint_layer=np.array([0., 0., double_layer_thick])
frontH_scint_physvols=[
    physical_volume(position=position_of_first_frontH_scint_layer + (i - 1) * distance_to_subsequent_scint_layer,
                    name="frontH_scint_physvol", CopyNumber=2*i - 1
                    )
    for i in range(1,numLayersFront_hori + 1)
]
frontV_scint_physvols=[
    physical_volume(position=position_of_first_frontV_scint_layer + (i - 1) * distance_to_subsequent_scint_layer,
                    name="frontV_scint_physvol", CopyNumber=2*i
                    )
    for i in range(1,numLayersFront_vert + 1)
]
backV_scint_physvols=[
    physical_volume(position=position_of_first_backV_scint_layer + (i - 1) * distance_to_subsequent_scint_layer,
                    name="backV_scint_physvol", CopyNumber=2*i + numLayersFront - 1
                    )
    for i in range(1,numDoubleLayersBack+ 1)
]

backH_scint_physvols=[
    physical_volume(position=position_of_first_backH_scint_layer + (i - 1) * distance_to_subsequent_scint_layer,
                    name="backH_scint_physvol", CopyNumber=2*i + numLayersFront
                    )
    for i in range(1,numDoubleLayersBack+ 1)
]

def absorber_copynumbers():
    return [absorber_physvols[i].CopyNumber  for i in range(0, numLayers)]

def frontH_copynumbers():
    return [frontH_scint_physvols[i].CopyNumber  for i in range(0, numLayersFront_hori)]

def frontV_copynumbers():
    return [frontV_scint_physvols[i].CopyNumber  for i in range(0, numLayersFront_vert)]

def backH_copynumbers():
    return [backH_scint_physvols[i].CopyNumber  for i in range(0, numDoubleLayersBack)]

def backV_copynumbers():
    return [backV_scint_physvols[i].CopyNumber  for i in range(0, numDoubleLayersBack)]


def frontH_depths():
    return [frontH_scint_physvols[i].depth  for i in range(0, numLayersFront_hori)]

def frontV_depths():
    return [frontV_scint_physvols[i].depth  for i in range(0, numLayersFront_vert)]

def backH_depths():
    return [backH_scint_physvols[i].depth  for i in range(0, numDoubleLayersBack)]

def backV_depths():
    return [backV_scint_physvols[i].depth  for i in range(0, numDoubleLayersBack)]
