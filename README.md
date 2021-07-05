
# Table of Contents

1.  [Structure of the geometry description](#orgd84c242)
2.  [Reference](#org0b0aa54)
    1.  [Constants](#org2461180)
    2.  [Solids](#org6caa71f)
    3.  [Logical volumes](#org8e47593)
    4.  [Physical volumes](#org39199a2)
        1.  [Notes on the CopyNumber](#orgdd24d48)
    5.  [User information](#orgf1ba2d9)
    6.  [Python code with all variables for testing](#org8fdb863)



<a id="orgd84c242"></a>

# Structure of the geometry description

The geometry is divided into several files to make working with it easier.

-   [detector.gdml](./detector.gdml) This is the entrypoint of the geometry. Contains the actual implementation of the prototype geometry using the definitions from [absorber<sub>volume.gdml</sub>](./absorber_volume.gdml) and [scintillator<sub>volume.gdml</sub>](./scintillator_volume.gdml)
-   [constants.gdml](./constants.gdml) Contains variable definitions used elsewhere in the
    geometry such as positions and geometrical properties of different volumes.
-   [materials.gdml](./materials.gdml) Contains definitions of isotopes and materials
-   [userinfo.gdml](./userinfo.gdml) Contains auxiliary information (see the
    [GDML manual](https://gdml.web.cern.ch/GDML/doc/GDMLmanual.pdf) for
    details), such as sensitive detector volumes, visualization information,
    version and author information.
-   [hcal<sub>solids.gdml</sub>](./hcal_solids.gdml) Contains definitions of the absorber, scintillator, and parent boxes
-   [absorber<sub>volume.gdml</sub>](./absorber_volume.gdml) Contains the definition of the absorber volume
-   [scintillator<sub>volume.gdml</sub>](./scintillator_volume.gdml) Contains the definition of the scintillator volumes


<a id="org0b0aa54"></a>

# Reference

The following is a list of all the variables defined in the protoype geometry description.


<a id="org2461180"></a>

## Constants

-   `center`, `identity`, and `hadron_calorimeter_pos` are positions that are all
    defined as **(x,y,z) = (0,0,0)**. `hadron_calorimeter_pos` is used to place the
    `prototype_volume` physical volume within the `World` volume.
-   `world_dim` is the size of the sides of the &ldquo;world<sub>box</sub>&rdquo; box, set to **10 m**
-   `air_thick` is the thickness (&Delta; z<sub>air</sub>) of the layers of air in between the
    absorber and scintillator bars. The thickness of each region is set to **2 mm**,
    which contributes twice to the thickness of an individual layer.
-   `absorber_width` is the width (&Delta; x<sub>absorber</sub>,&Delta; y<sub>absorber</sub>) of an absorber
    layer, set to **800 mm**
-   `absorber_ears`, TODO: Document this, set to **50 mm**
-   `absorber_thickness` is the thickness (&Delta; z<sub>absorber</sub>) of an absorber layer,
    set to **25 mm**
-   `scint_thick` is the thickness of a scintillator bar layer (&Delta;
    z<sub>scintillator</sub>). This is equivalent to the thickness of an individual
    scintillator bar and is set to **20 mm**
-   `scint_bar_length` is the length of an individual scintillator bar. In
    horizontal layers, this is equivalent to the width (&Delta; x<sub>scintillator</sub>) of the
    layer while in vertical layers it is equivalent to the height (&Delta;
    y<sub>scintillator</sub>) of the layer. It is set to **2000 mm**.
-   `layer_thick` is the combined thickness of a layer (&Delta;
    z<sub>layer</sub>). It consists of one layer of absorber,
    `absorber_thickness`, one layer of scintillators, and *two* layers and *two*
    layers of air, `air_thick`. The resulting layer thickness is thus given by
    `absorber_thickness + scint_thick + 2 * air_thick`, **49 mm**
-   `double_layer_thick` is twice the thickness of one layer, i.e. **98 mm**. It is
    currently only used in defining the total depth of the prototype, `dz`.
-   `numLayersFront` is the total number of layers in the front region of the
    prototype and is set to **9**
-   `numLayersFront_vert` and `numLayersFront_hori` are the number of
    vertical/horizontal layers in the front region. They are set to **4** and **5**
    respectively
-   `numDoubleLayersBack` is the number of horizontal or vertical layers in the
    back region. It is set to **5** so the total number of layers in the back region
    is **10**
-   `numLayers` is the total number of layers. It is set to **19** and corresponds
    to `numLayers + 2 * numDoubleLayersBack`
-   `back_start` is the location of the first layer in the back region. It is set
    to `numLayersFront * layer_thick`, i.e. **441 mm**
-   The length of the sides of the various scintillator layers are defined as
    -   Front vertical layers have `scint_FrontV_x` which is **400 mm**,
        `scint_FrontV_y` which is the bar length, **2000 mm**. The 400 mm corresponds
        to 8 bars each having a width of **50 mm**
    -   Front horizontal layers have `scint_FrontH_y` which is **400 mm**,
        `scint_FrontH_x` which is the bar length, **2000 mm**. The 400 mm corresponds
        to 8 bars each having a width of **50 mm**
    -   Back vertical layers have `scint_BackV_x` which is **600 mm**, `scint_BackV_y`
        which is the bar length, **2000 mm**. The 600 mm corresponds to 12 bars each
        having a width of **50 mm**
    -   Back horizontal layers have `scint_BackH_y` which is **600 mm**,
        `scint_BackH_x` which is the bar length, **2000 mm**. The 600 mm corresponds
        to 12 bars each having a width of **50 mm**
-   `dx` and `dy`, the width and height of the prototype respectively are both set
    to **3000 mm**
-   `dz` is the depth of the prototype and is defined as `numLayersFront *
      layer_thick + numDoubleLayersBack * double_layer_thick` which correpsonds to
    **931 mm**


<a id="org6caa71f"></a>

## Solids

Solids are objects with purely geometrical properties such as a box, a sphere,
or a more complicated geometry

-   `absorberBox` is the solid that represents the absorber layer.
    -   TODO: Document this @petergy
-   There are four boxes representing the four different types of scintillator
    layers (front vertical, front horizontal, back vertical, back horizontal).
    These are defined using the corresponding width/height from
    [Constants](#org2461180), e.g.
    -   `frontV_ScintBox` has width `scint_FrontV_x` (400 mm) and height
        `scint_FrontV_y` (2000 mm)
    -   `frontH_ScintBox` has width `scint_FrontH_x` (2000 mm) and height
        `scint_FrontH_y` (400 mm)
    -   `backV_ScintBox` has width `scint_BackV_x` (600 mm) and height
        `scint_BackV_y` (2000 mm)
    -   `backH_ScintBox` has width `scint_BackH_x` (2000 mm) and height
        `scint_BackH_y` (600 mm)
-   `air_box` is the a box representing a single air layer and has width `dx`
    (3000 mm), height `dy` (3000 mm), and depth `air_thick` (2 mm)
-   `prototype_Box` is the parent volume for the prototype and is defined as a box
    with width `dx` (3000 mm), height `dy` (3000 mm), and depth `dz` (931 mm)
-   `world_box` is the parent volume for all the other parts of the geometry and
    is defined as a box with all sides having length `world_dim` (10 m)


<a id="org8e47593"></a>

## Logical volumes

In Geant4, a logical volume can contain all of the information about a volume
except for its position. This allows you to use one logical volume to create
several distinct daughter physical volumes. The position and rotation of a
daughter volume is defined in terms for the mother volume. The logical volumes
that we use in this geometry can contain the following tags

-   `<solidref>` is a reference to one of the solids defined in
    [hcal<sub>solids.gdml</sub>](./hcal_solids.gdml)
-   `<materialref>` is a reference to a material defined in
    [materials.gdml](./materials.gdml)
-   `<auxiliary>` allows us to add any other kind of information that is used by
    the simulation, such as defining if a volume is supposed to be a sensitive
    element or how the volume should be visualized by default. Most auxiliary tags
    will be references to groups of properties defined in [[\*User information][User information]].

-   `<physvol>` any daughter volumes that are to be placed within the logical
    volume, see [Physical volumes](#org39199a2)

Furthermore, each logical volume has a name as part of the `<volume>` tag which
can be used to refer to the volume using the `<volumeref>` tag. At least one logical volume has to be the &ldquo;World&rdquo; volume. This volume determines the global coordinate system and has to completly contain all other volumes, sharing surfaces with none of them.

-   `World` is the &ldquo;World&rdquo; volume. It is defined in
    [detector.gdml](./detector.gdml)
    -   Material: `G4_AIR`
    -   Solid: `world_box`
    -   Daughter volumes:
        -   `prototype_volume`
    -   Auxiliary information:
        -   &ldquo;DetElem&rdquo;: &ldquo;Top&rdquo;
-   `prototype_volume` represents the entire prototype and is defined in
    [detector.gdml](./detector.gdml)
    -   Material: `G4_AIR`
    -   Solid: `prototype_Box`
    -   Daughter volumes:
        -   `absorber_physvol`
        -   `frontH_scint_physvol`
        -   `frontV_scint_physvol`
        -   `back_H_scint_physvol`
        -   `back_V_scint_physvol`
    -   Auxiliary information:
        -   &ldquo;Region&rdquo;: &ldquo;CalorimeterRegion&rdquo;
        -   &ldquo;VisAttributes&rdquo;: &ldquo;HcalVis&rdquo;
        -   &ldquo;DetElem&rdquo;: &ldquo;Hcal&rdquo;
-   `absorber_volume` represents one layer of the steel absorber and is defined in [absorber<sub>volume.gdml</sub>](./absorber_volume.gdml)
    -   Material: `Steel`
    -   Solid: `absorberBox`
    -   Auxiliary information:
        -   &ldquo;Color&rdquo;: &ldquo;Red&rdquo;
        -   &ldquo;VisAttributes&rdquo;: &ldquo;HcalVis&rdquo;
-   There are four volumes representing each of the four different types of
    scintillator layers called `frontV_ScintBox_volume`, `frontH_ScintBox_volume`,
    `backV_ScintBox_volume`, and `backH_ScintBox_volume`, all defined in
    [scintillator<sub>volume.gdml</sub>](./scintillator_volume.gdml). They differ in name
    and which corresponding solid they make use of
-   Material: &ldquo;Scintillator&rdquo;
-   Solid: One of `frontV_ScintBox`, `frontH_ScintBox`, `backV_ScintBox`, and
    `backH_ScintBox`
-   Auxiliary information:
    -   &ldquo;SensDet&rdquo;: &ldquo;HcalSD&rdquo;
    -   &ldquo;Color&rdquo;: &ldquo;Blue&rdquo;
    -   &ldquo;VisAttributes&rdquo;: &ldquo;HcalVis&rdquo;


<a id="org39199a2"></a>

## Physical volumes

A physical volume is a logical volume with a position and, optionally, a name
and a so-called CopyNumber. The CopyNumber should be *unique* for each physical
volume. In LDMX-sw, the CopyNumber is used to identify which readout-channels a
given physical volume corresponds to so some care must be taken when working on
the geometry to ensure that the position of the physical volume and the
corresponding CopyNumber aligns. For details see [Notes on the CopyNumber](#orgdd24d48).

-   The physical volume representing the prototype volume is unnamed
    -   Mother volume: `World`
    -   Logical volume: `prototype_volume`
    -   Position: `hadron_calorimeter_pos`
    -   Rotation: `identity`
-   `absorber_physvol`: There are 19 physical volumes representing the absorber
    layers
    -   Logical volume: `absorber_volume`
    -   Mother volume: `prototype_volume`
    -   CopyNumbers: [1 .. 19]
    -   Position of the first layer:
        -   x: **-400 mm**
        -   y: **-400 mm**
        -   z: `-dz/2`, i.e. **-465.5 mm**
    -   Distance (z) to subsequent layer: `layer_thick`, i.e. **49 mm**
-   `frontH_scint_physvol`: There are 5 physical volumes representing the
    horizontal scintillator layers in the front region. They all have odd
    CopyNumbers.
    -   Logical volume: `frontH_ScintBox_volume`
    -   Mother volume: `prototype_volume`
    -   CopyNumbers: [1,3,5,7,9]
    -   Position of the first layer:
        -   x: **0 mm**
        -   y: **0 mm**
        -   z: `-dz/2 + absorber_thickness + air_thick + scint_thick/2`, i.e. **-428.5
            mm**
    -   Distance (z) to subsequent layer: `double_layer_thick`, i.e. **98 mm**
-   `frontV_scint_physvol`: There are 4 physical volumes representing the vertical
    scintillator layers in the front region. They all have even CopyNumbers.
    -   Logical volume: `frontV_ScintBox_volume`
    -   Mother volume: `prototype_volume`
    -   CopyNumbers: [2,4,6,8]
    -   Position of the first layer:
        -   x: **0 mm**
        -   y: **0 mm**
        -   z: `-dz/2 + absorber_thickness + air_thick + scint_thick/2 + layer_thick`,
            i.e. **-379.5 mm**
    -   Distance (z) to subsequent layer: `double_layer_thick`, i.e. **98 mm**
-   `backV_scint_physvol`: There are 5 physical volumes representing the vertical
    scintillator layers in the back region. They all have even CopyNumbers.
    -   Logical volume: `backV_ScintBox_volume`
    -   Mother volume: `prototype_volume`
    -   CopyNumbers: [10, 12, 14, 16, 18]
    -   Position of the first layer:
        -   x: **0 mm**
        -   y: **0 mm**
        -   z: `-dz/2 + back_start + absorber_thickness + air_thick + scint_thick/2`,
            i.e. **12.5 mm**
    -   Distance (z) to subsequent layer: `double_layer_thick`, i.e. **98 mm**
-   `backH_scint_physvol`: There are 5 physical volumes representing the
    horizontal scintillator layers in the back region. They all have odd
    CopyNumbers.
    -   Logical volume: `backH_ScintBox_volume`
    -   Mother volume: `prototype_volume`
    -   CopyNumbers: [11, 13, 15, 17, 19]
    -   Position of the first layer:
        -   x: **0 mm**
        -   y: **0 mm**
        -   z: `-dz/2 + back_start + layer_thick + absorber_thickness + air_thick + scint_thick/2`, i.e. **61.5 mm**
    -   Distance (z) to subsequent layer: `double_layer_thick`, i.e. **98 mm**


<a id="orgdd24d48"></a>

### Notes on the CopyNumber

For the hadronic calorimeter, the CopyNumber encodes the layer number and the
section number of the scintillators. The section number refers to the five
distinct sections of the full LDMX Hcal (Back, Top, Bottom, Left, Right). The
prototype geometry consists entirely of the &ldquo;Back&rdquo; section of the Hcal which has
section number **0**. The section number is derived from the CopyNumber by taking
the modulo of the CopyNumber with **1000**

The layers of the protoype are numbered from 1 to 19 (note the non-zero based
indexing). The layer number is derived from the CopyNumber by dividing the CopyNumber with **1000** and taking the remainder.

TODO: @PeterGy, document the CopyNumber requirements for the trigger
scintillator.

Furthermore, the rotation of the layer is determined by the layer number, which
in turn depends on the CopyNumber. An even CopyNumber means a vertical layer
(length of the bars is along the y-axis) while an odd CopyNumber


<a id="orgf1ba2d9"></a>

## User information


<a id="org8fdb863"></a>

## Python code with all variables for testing

The following is a short python script containing definitions for all of the
variables used to describe the physical volumes that can be used to test or
calculate. All units are **mm**

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

