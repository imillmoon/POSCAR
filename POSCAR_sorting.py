"""
파일명 뒤에 x, y, z 중 하나를 선택하여 실행시키면 선택된 것을 기준으로 오름차순으로 sorting
"""


import numpy as np
import sys

file_name = sys.argv[1]
xyz = sys.argv[2]

# read POSCAR
POSCAR = open(file_name,'r')
POSCAR.readline() # NAME
latt_const =float(POSCAR.readline())
latt = np.zeros([3,3])
for i in range(3):
	latt[i] = np.array([float(x) for x in POSCAR.readline().split()])
latt = latt*latt_const
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

if xyz == "x" or xyz == "X":
    R = 0
elif xyz == "y" or xyz == "Y":
    R = 1
elif xyz == "z" or xyz == "Z":
    R = 2

sorted_pos = np.zeros([ntot,3])
min = 0
max = 0
for i in range(len(at_name)):
    max +=n_atoms[i]
    atom = pos[min:max]
    sort = np.argsort(atom[:,R])
    atom = atom[sort]
    sorted_pos[min:max] = atom
    min += n_atoms[i]

for i in range(ntot):
    print(f"{sorted_pos[i,0]:24.16f}{sorted_pos[i,1]:24.16f}{sorted_pos[i,2]:24.16f}")
