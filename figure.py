#!/usr/local/bin/python
import sdf
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from numpy import ma
from matplotlib import colors, ticker, cm
from matplotlib.mlab import bivariate_normal
from optparse import OptionParser
import os
import xml.etree.ElementTree
import numpy as np

font = {'family' : 'monospace',  
        'color'  : 'black',  
        'weight' : 'normal',  
        'size'   : 20,  
        }  




path_from = './electron.xml'
to_path   = './jpg_electron1/'


e = xml.etree.ElementTree.parse(path_from).getroot()

for hist1d in e.findall('histogram1d'): ## big loop
    name  = hist1d.get('name')
    title = hist1d.get('title')
    print('histogram1d! name:',name,' title:',title)
    for annotation in hist1d.findall('annotation'): ## this loop is for annotation
        for item in annotation.findall('item'):  
            key   = item.get('key')
            value = item.get('value')
            print('annotation! key:',key,' value',value)
    for axis in hist1d.findall('axis'):   ## this loop is for axis 
        direction    = axis.get('direction')
        numberOfBins = axis.get('numberOfBins')
        bin_min      = axis.get('min')
        bin_max      = axis.get('max')
        print('axis! direction:',direction,' numberofbins:',numberOfBins,' bin_min:',bin_min,' bin_max:',bin_max)
    gz_data_x = np.linspace(int(bin_min),int(bin_max),int(numberOfBins)+1)
    gz_data_y = np.zeros_like(gz_data_x)
    for data1d in hist1d.findall('data1d'):  ## this loop is for data
        for bin1d in data1d.findall('bin1d'):
            binNum  = bin1d.get('binNum')
            entries = bin1d.get('entries')
            print('data1d! binNum:',binNum,' entries:',entries)
            gz_data_y[int(binNum)] = float(entries)
   
    plt.plot(gz_data_x,gz_data_y,'-k',linewidth=3)
    plt.yscale('log')
    plt.grid(which='major',color='k', linestyle='--', linewidth=0.3)
    #### manifesting colorbar, changing label and axis properties ####
    plt.xlabel('Energy '+value,fontdict=font)
    plt.ylabel('N',fontdict=font)
    plt.xticks(fontsize=20); plt.yticks(fontsize=20);
    plt.title(title,fontdict=font)
    fig = plt.gcf()
    fig.set_size_inches(8.5, 6)
    fig.savefig(to_path+name+title[:10]+'.png',format='png',dpi=160)
    plt.close("all") 
   
    print('==================end of this hist====================')
    print('======================================================')
