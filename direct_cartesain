"""
POSCAR 파일을 읽어 Cartesian인 파일은 Direct로 Direct인 파일은 Cartesian으로 변환
"""


import numpy as np
import sys

file_name = sys.argv[1]

# POSCAR file read
POSCAR = open(file_name,'r')
name = POSCAR.readline() # NAME
latt_const =float(POSCAR.readline())
latt_original = np.zeros([3,3])
for i in range(3):
	latt_original[i] = np.array([float(x) for x in POSCAR.readline().split()])
latt = latt_original*latt_const
at_name = np.array(POSCAR.readline().split())
n_atoms = np.array([int(x) for x in POSCAR.readline().split()])
coord = POSCAR.readline().strip() # Direct or Cartesian
ntot = 0
for i in range(len(n_atoms)):
	ntot += n_atoms[i]
pos = np.zeros([ntot,3])
for i in range(ntot):
		pos[i] = np.array([float(x) for x in POSCAR.readline().split()])
POSCAR.close()

latt_transpose = latt.transpose()

if coord == "Cartesian" or coord == "cartesian":
    # transform cartesian into direct
    direct = np.zeros([ntot,3])
    for i in range(ntot):
        direct[i] = np.linalg.solve(latt_transpose,pos[i])
    print('Direct')
    for i in range(ntot):
        print(f"{direct[i,0]:24.16f}{direct[i,1]:24.16f}{direct[i,2]:24.16f}")
elif coord == "Direct" or coord == "direct":
    # transform direct into cartesian
    cartesian = np.zeros([ntot,3])
    for i in range(ntot):
        cartesian[i] = pos[i,0]*latt[0] + pos[i,1]*latt[1] + pos[i,2]*latt[2]
    print('Cartesian')
    for i in range(ntot):
        print(f"{cartesian[i,0]:24.16f}{cartesian[i,1]:24.16f}{cartesian[i,2]:24.16f}")
else:
    print("change 8th line into 'Cartesian' or 'Direct'")
