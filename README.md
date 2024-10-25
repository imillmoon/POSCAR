POSCAR 변환을 바탕으로 구조 분석을 용이하게 만들어줌

1. CONTCAR_POSCAR
   VASP 계산 후 나온 CONTCAR 파일의 구조가 외견 상 POSCAR과 다르다면, CONTCAR의 optimization 이후 구조는 그대로 유지하되 POSCAR 파일처럼 원자 위치를 조정
   
2. POSCAR_dorting
   POSCAR 파일의 원자 순서를 오름차순으로 정렬하고 싶을 때 사용

3. direct_cartesian
   direct(cartesian) 기준 POSCAR 파일의 원자 정보를 cartesian(direct) 기준 원자 정보로 변환시킬 때 사용
