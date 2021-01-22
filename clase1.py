# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 16:20:19 2021

@author: Carlos Fabian Anagarita
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import flopy

#Se ingresan los datos 
name = "tutorial01_mf6"
h1 = 100
h2 = 90
Nlay = 10
N = 101
L = 400.0
H = 50.0
k = 1.0

#Busca mf6 en la carpeta seleccionada y guarda archivos
sim = flopy.mf6.MFSimulation(
    sim_name=name, exe_name="C:/Users/Owner/Desktop/Universidad/DIPLOMADO GEOCIENCIA/mf6.2.0/bin/mf6",
    version="mf6", sim_ws="WorkSpace"
)

#Create the Flopy TDIS object
tdis = flopy.mf6.ModflowTdis(
    sim, pname="tdis", time_units="DAYS", nper=1, perioddata=[(1.0, 1, 1.0)])

#Create the Flopy IMS Package object# # IMS es el solver
ims = flopy.mf6.ModflowIms(sim, pname="ims", complexity="SIMPLE")

#Create the Flopy groundwater flow (gwf) model object
model_nam_file = "{}.nam".format(name)
gwf = flopy.mf6.ModflowGwf(sim, modelname=name, model_nam_file=model_nam_file)










