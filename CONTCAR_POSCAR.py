"""
VASP 계산후 나오는 CONTCAR 파일의 경우 POSCAR 파일과 상관없이 항상 Direct로 변환되어서 결과가 출력됨.
이 과정에서 모든 원자의 위치를 0<=x,y,z<=1로 바꾸어서 출력하기 때문에 기존의 POSCAR 파일에서 보았던 원자 구조와 달라 보이는 현상이 발생함.
이러한 문제를 해결하기 위해 CONTCAR와 POSCAR의 각 원자 위치를 비교하여 위치가 달라진 원자의 위치를 바꿔 POSCAR처럼 보이도록 변환시킴.(optimization은 유지함)
"""

import numpy as np

before = open("POSCAR",'r')
name = before.readline() # NAME
latt_const =float(before.readline())
latt_original = np.zeros([3,3])
for i in range(3):
	latt_original[i] = np.array([float(x) for x in before.readline().split()])
latt = latt_original*latt_const
at_name = np.array(before.readline().split())
n_atoms = np.array([int(x) for x in before.readline().split()])
coord = before.readline().strip() # Direct or Cartesian
ntot = 0
for i in range(len(n_atoms)):
	ntot += n_atoms[i]
pos = np.zeros([ntot,3])
for i in range(ntot):
		pos[i] = np.array([float(x) for x in before.readline().split()])
before.close()

after = np.genfromtxt("CONTCAR", skip_header=8, dtype=float)


latt_transpose = latt.transpose()
if coord == "Cartesian" or coord == "cartesian":
    direct = np.zeros([ntot,3])
    for i in range(ntot):
        direct[i] = np.linalg.solve(latt_transpose,pos[i])
    before = direct.copy()

    pos = np.zeros([before.shape[0],before.shape[1]])

    for i in range(int(np.max(before)+2)):
        for i in range(before.shape[0]):
            for j in range(before.shape[1]):
                if abs(after[i,j] - before[i,j]) < 0.5:
                    pos[i,j] = after[i,j]
                elif after[i,j] - before[i,j] > 0.5:
                    pos[i,j] = after[i,j] - 1
                elif after[i,j] - before[i,j] < -0.5:
                    pos[i,j] = after[i,j] + 1
        after = pos
    for i in range(before.shape[0]):
        print(f"{pos[i,0]:24.16f}{pos[i,1]:24.16f}{pos[i,2]:24.16f}")
else:
    before = pos.copy()
    pos = np.zeros([before.shape[0],before.shape[1]])

    for i in range(int(np.max(before)+2)):
        for i in range(before.shape[0]):
            for j in range(before.shape[1]):
                if abs(after[i,j] - before[i,j]) < 0.5:
                    pos[i,j] = after[i,j]
                elif after[i,j] - before[i,j] > 0.5:
                    pos[i,j] = after[i,j] - 1
                elif after[i,j] - before[i,j] < -0.5:
                    pos[i,j] = after[i,j] + 1
        after = pos
    for i in range(before.shape[0]):
        print(f"{pos[i,0]:24.16f}{pos[i,1]:24.16f}{pos[i,2]:24.16f}")
