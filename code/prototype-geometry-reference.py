#!/usr/bin/env python3

# A short script containing representations of the variables that are used in
# the geometry description. Useful for testing and calculations.
#
# Note that all units are in mm

import numpy as np
# Constants
center = np.array([0., 0., 0.])
hadron_calorimeter_pos = np.array([0., 0., 0.])
world_dim = 10000.
absorber_width = 665.
absorber_height = 700.
absorber_thickness = 20.
absorber_hole_radius = 6.5
absorber_hole_distance_from_edge = 16.
bar_mounting_plate_thickness = 3.
scint_thickness = 20.
scint_bar_length = 2000.
scint_bar_width = 50.
scint_bar_cover_thickness = 0.5

layer_thickness = 45.  # Note hardcoded
air_thickness = layer_thickness - (
    absorber_thickness +
    bar_mounting_plate_thickness +
    scint_thickness +
    scint_bar_cover_thickness)  # Derived from other variables now

num_bars_front = 8
num_bars_back = 12
num_layers_front_vertical = 4
num_layers_front_horizontal = 5
num_layers_front = num_layers_front_vertical + num_layers_front_horizontal
num_layers_back_vertical = 5
num_layers_back_horizontal = 5
num_layers_back = num_layers_back_vertical + num_layers_back_horizontal
num_layers = num_layers_front + num_layers_back
num_absorbers = num_layers + 1  # 1 Extra plate in the back
back_start = num_layers_front * layer_thickness

dx = 3000.
dy = 3000.
dz = num_layers * layer_thickness

first_layer_zpos = -dz / 2
first_layer_absorber_zpos = first_layer_zpos + absorber_thickness / 2
first_layer_scint_cover_zpos = first_layer_zpos + \
    absorber_thickness + \
    scint_bar_cover_thickness / 2
assert (first_layer_scint_cover_zpos ==
        first_layer_absorber_zpos +
        absorber_thickness / 2 +
        scint_bar_cover_thickness / 2)
first_layer_scint_zpos = first_layer_zpos + \
    absorber_thickness + \
    scint_bar_cover_thickness + \
    scint_thickness / 2
assert (first_layer_scint_zpos ==
        first_layer_scint_cover_zpos +
        scint_bar_cover_thickness / 2 +
        scint_thickness / 2)
first_layer_bar_mounting_plate_zpos = first_layer_zpos + \
    absorber_thickness + \
    scint_bar_cover_thickness + \
    scint_thickness + \
    bar_mounting_plate_thickness / 2
assert (first_layer_bar_mounting_plate_zpos ==
        first_layer_scint_zpos +
        scint_thickness / 2 +
        bar_mounting_plate_thickness / 2)

first_back_layer_zpos = first_layer_zpos + back_start

absorber_first_layer_zpos = first_layer_zpos

scint_front_vertical_x = num_bars_front * scint_bar_width
scint_front_vertical_y = scint_bar_length

scint_front_horizontal_x = scint_bar_length
scint_front_horizontal_y = num_bars_front * scint_bar_width

scint_back_vertical_x = num_bars_back * scint_bar_width
scint_back_vertical_y = scint_bar_length

scint_back_horizontal_x = scint_bar_length
scint_back_horizontal_y = num_bars_back * scint_bar_width


bar_mounting_plate_horizontal_x = scint_back_horizontal_x
bar_mounting_plate_horizontal_y = scint_back_horizontal_y
bar_mounting_plate_vertical_x = scint_back_vertical_x
bar_mounting_plate_vertical_y = scint_back_vertical_y

trigger_bar_gap = 0.3
trigger_bar_dx = 40.
trigger_bar_dy = 3.
trigger_bar_dz = 2.
number_of_trigger_bars = 6
trigger_layer_distance_from_detector = 300.

lyso_bar_gap = 0.3
lyso_bar_dx = 30
lyso_bar_dy = 2.1
lyso_bar_dz = 0.6
number_of_lyso_bars = 8

lyso_plate_dx = 30
lyso_plate_dy = 20
lyso_plate_dz = 1.2


prototype_extra_space = 1000.
trigger_dz = trigger_layer_distance_from_detector + \
    trigger_bar_dz + \
    trigger_bar_gap

prototype_box_dz = dz + 2 * trigger_dz + prototype_extra_space

# Solids
front_vertical_scint_box = {"width": scint_front_vertical_x,
                            "height": scint_front_vertical_y}
front_horizontal_scint_box = {"width": scint_front_horizontal_x,
                              "height": scint_front_horizontal_y}
back_vertical_scint_box = {"width": scint_back_vertical_x,
                           "height": scint_back_vertical_y}
back_horizontal_scint_box = {"width": scint_back_horizontal_x,
                             "height": scint_back_horizontal_y}
air_box = {"width": dx,
           "height": dy,
           "depth": air_thickness}
prototype_box = {"width": dx,
                 "height": dy,
                 "depth": dz}
world_box = {"width": world_dim,
             "height": world_dim,
             "depth": world_dim}

trigger_bar_box = {"width": trigger_bar_dx,
                   "height": trigger_bar_dy,
                   "depth": trigger_bar_dz}


class physical_volume:
    def __init__(self, position, name="", CopyNumber=None):
        self.position = position
        if CopyNumber is not None:
            self.CopyNumber = CopyNumber
            self.depth = position[2]

    def __repr__(self):
        return str(self.__dict__)


# Physical volumes
absorber_first_layer_pos = np.array([0.,
                                     0.,
                                     -dz/2])
bar_mounting_plate_horizontal_first_layer_pos = np.array(
    [0, 0,
     absorber_first_layer_pos[2] +
     absorber_thickness/2.0 +
     bar_mounting_plate_thickness/2.0])
bar_mounting_plate_vertical_first_layer_pos = np.array(
    [0, 0,
     layer_thickness +
     bar_mounting_plate_horizontal_first_layer_pos[2]])


scint_front_horizontal_first_layer_pos = np.array(
    [0., 0.,
     bar_mounting_plate_horizontal_first_layer_pos[2] +
     bar_mounting_plate_thickness/2.0 +
     scint_thickness/2.0])

scint_front_vertical_first_layer_pos = (scint_front_horizontal_first_layer_pos
                                        + [0., 0., layer_thickness])
scint_back_vertical_first_layer_pos = (scint_front_horizontal_first_layer_pos
                                       + [0., 0., back_start])
scint_back_horizontal_first_layer_pos = (scint_back_vertical_first_layer_pos
                                         + [0., 0., layer_thickness])


trigger_first_layer_even_pos = np.array(
    [0,
     trigger_bar_dy*(1 - 0.5 - number_of_trigger_bars/2) +
     trigger_bar_gap*(1 - 1 - number_of_trigger_bars/2),
     - trigger_bar_dz - trigger_bar_gap - dz/2
     - trigger_layer_distance_from_detector])

trigger_first_layer_odd_pos = np.array(
    [0,
     trigger_bar_dy*(1 - 0 - number_of_trigger_bars/2) +
     trigger_bar_gap*(1 - 1 - number_of_trigger_bars/2),
     -dz/2 - trigger_layer_distance_from_detector])

distance_to_subsequent_absorber_layer = np.array(
    [0.,
     0.,
     layer_thickness])
distance_to_subsequent_scint_layer = np.array(
    [0.,
     0.,
     2. * layer_thickness])
distance_to_subsequent_trigger_layer = np.array(
    [0.,
     trigger_bar_dy + trigger_bar_gap,
     0])

first_absorber = physical_volume(absorber_first_layer_pos)
absorber_physvols = [
    physical_volume(position=absorber_first_layer_pos +
                    distance_to_subsequent_absorber_layer * i,
                    name="absorber_physvol",
                    CopyNumber=i)
    for i in range(1, num_layers + 1)
]
front_horizontal_scint_physvols = [
    physical_volume(position=scint_front_horizontal_first_layer_pos +
                    (i - 1) * distance_to_subsequent_scint_layer,
                    name="front_horizontal_scint_physvol",
                    CopyNumber=2*i - 1)
    for i in range(1, num_layers_front_horizontal + 1)
]
front_vertical_scint_physvols = [
    physical_volume(position=scint_front_vertical_first_layer_pos +
                    (i - 1) * distance_to_subsequent_scint_layer,
                    name="front_vertical_scint_physvol",
                    CopyNumber=2*i)
    for i in range(1, num_layers_front_vertical + 1)
]
back_vertical_scint_physvols = [
    physical_volume(position=scint_back_vertical_first_layer_pos +
                    (i - 1) * distance_to_subsequent_scint_layer,
                    name="back_vertical_scint_physvol",
                    CopyNumber=2*i + num_layers_front - 1)
    for i in range(1, num_layers_back_vertical + 1)
]

back_horizontal_scint_physvols = [
    physical_volume(position=scint_back_horizontal_first_layer_pos +
                    (i - 1) * distance_to_subsequent_scint_layer,
                    name="back_horizontal_scint_physvol",
                    CopyNumber=2*i + num_layers_front
                    )
    for i in range(1,num_layers_back_horizontal + 1)
]


trigger_physvols = ["placeholder" for i in range(1, number_of_trigger_bars*2)]
for i in range(1, number_of_trigger_bars):
    trigger_physvols[i*2-2] = physical_volume(
        position=trigger_first_layer_even_pos +
        (i - 1) * distance_to_subsequent_trigger_layer,
        name="trigger_physvol",
        CopyNumber=2*i-2)
    trigger_physvols[i*2-1] = physical_volume(
        position=trigger_first_layer_odd_pos +
        (i - 1) * distance_to_subsequent_trigger_layer,
        name="trigger_physvol",
        CopyNumber=2*i-1)


def absorber_copynumbers():
    return [absorber_physvols[i].CopyNumber
            for i in range(0, num_layers)]


def front_horizontal_copynumbers():
    return [front_horizontal_scint_physvols[i].CopyNumber
            for i in range(0, num_layers_front_horizontal)]


def front_vertical_copynumbers():
    return [front_vertical_scint_physvols[i].CopyNumber
            for i in range(0, num_layers_front_vertical)]

def back_horizontal_copynumbers():
    return [back_horizontal_scint_physvols[i].CopyNumber
            for i in range(0, num_layers_back_horizontal)]


def back_vertical_copynumbers():
    return [back_vertical_scint_physvols[i].CopyNumber
            for i in range(0, num_layers_back_vertical)]


def trigger_copynumbers():
    return [trigger_physvols[i].CopyNumber
            for i in range(0, number_of_trigger_bars*2)]


def front_horizontal_depths():
    return [front_horizontal_scint_physvols[i].depth
            for i in range(0, num_layers_front_horizontal)]


def front_vertical_depths():
    return [front_vertical_scint_physvols[i].depth
            for i in range(0, num_layers_front_vertical)]


def back_horizontal_depths():
    return [back_horizontal_scint_physvols[i].depth
            for i in range(0, num_layers_back_horizontal)]


def back_vertical_depths():
    return [back_vertical_scint_physvols[i].depth
            for i in range(0, num_layers_back_vertical)]


def trigger_depths():
    return [trigger_physvols[i].depth
            for i in range(0, number_of_trigger_bars*2)]
