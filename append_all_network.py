# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 09:00:08 2017

@author: hjh
"""

import os

frlist = os.listdir(r'F:\hejunhao\study\work\string database\all_interaction')
fw = open('networks.tab','w')

fw.write('interactorA' + '\t' + 'interactorB' + '\n')
for each in frlist:
    if each != '10090.txt':
        fr = open(r'F:\hejunhao\study\work\string database\all_interaction\%s' %each,'r')
        proteins = fr.readlines()
        for each1 in proteins:
            protein = each1.strip().split(' ')
            A = protein[0][5:]
            B = protein[1][5:]
            fw.write(A + '\t' + B + '\n')
            
    else:
        fr = open(r'F:\hejunhao\study\work\string database\all_interaction\%s' %each,'r')
        proteins = fr.readlines()
        for each1 in proteins:
            protein = each1.strip().split(' ')
            A = protein[0][6:]
            B = protein[1][6:]
            fw.write(A + '\t' + B + '\n')
        
        
    fr.close()
    
fw.close()