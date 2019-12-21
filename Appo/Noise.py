from sys import exit
import random
from array import array
import numpy as np                                                                                                                                                                                        
import h5py
import ROOT                                                                                                                                                                                                                                                                                            
import os

#if os.path.exists('Outfile_TopoClusterTotal.h5'):                                                                                                                                                          
#    os.remove('Outfile_TopoClusterTotal.h5')                                                                                                                                                               
#else:                                                                                                                                                                                                      
#    print("Can not delete the file as it doesn't exists")



f = h5py.File('Outfile_CellInformation_HomDet_2to5GeV.h5','r')

hist1=ROOT.TH1D("layer1","layer1",200,-100,100)
hist2=ROOT.TH1D("layer2","layer2",200,-100,100)
hist3=ROOT.TH1D("layer3","layer3",200,-150,150)
hist4=ROOT.TH1D("layer4","layer4",200,-400,400)
hist5=ROOT.TH1D("layer5","layer5",200,-400,400)
hist6=ROOT.TH1D("layer6","layer6",200,-800,800)

h=[hist1,hist2,hist3,hist4,hist5,hist6]

noises={}
layers=[32,64,32,16,16,8]

for lay in range(6):
    noises["layer_"+str(lay+1)]=[]
    for ev in range(1000):
    
        T=f["RealRes_TotalEnergy_Layer"+str(lay+1)][ev][0][:,:]-f["RealRes_NeutralEnergy_Layer"+str(lay+1)][ev][0][:,:]-f["RealRes_ChargedEnergy_Layer"+str(lay+1)][ev][0][:,:]

        for X in range(layers[lay]):
            for Y in range(layers[lay]):
                noises["layer_"+str(lay+1)].append(T[X][Y])

print(len(noises["layer_1"]))
            
for lay in range(6):
    for n in noises["layer_"+str(lay+1)]:
        h[lay].Fill(n)

f_o=ROOT.TFile("Noise.root","recreate")
for lay in range(6):
    h[lay].Write()

f_o.Close()
