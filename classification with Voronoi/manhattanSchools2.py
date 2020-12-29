from scipy.spatial import Delaunay
from scipy.spatial import cKDTree
from collections import defaultdict
import itertools
import manhattanSchools1


n = int(input('Enter the size of the city:  '))
kH = int(input('Enter the amount of horizontal streets:  '))
kV = int(input('Enter the amount of vertical streets:  '))

nschools = int(input('How many schools is going to be in the city?  '))
ncitizens = int(input('How many people are we going to track?  '))


city = manhattanSchools1.cityMaking(n, kH, kV)
city, schools, enters = manhattanSchools1.schoolMaking(nschools, city, n)
city, citizens = manhattanSchools1.citizenMaking(ncitizens, city, n)
manhattanSchools1.labyrinthOut(city, n)

voronoi_kdtree = cKDTree(schools)
closestVorDist, closestSchoolVor = voronoi_kdtree.query(citizens)

tri = Delaunay(schools)
neighbours=defaultdict(set)
for p in tri.vertices:
    for i,j in itertools.combinations(p,2):
        neighbours[i].add(j)
        neighbours[j].add(i)


for i in range(0, ncitizens):
   city = manhattanSchools1.findDaWae(citizens[i][0], citizens[i][1], 0, city, n)
   closestSchool, steps = manhattanSchools1.findClosestSchool(city, n*4, enters, closestSchoolVor[i], neighbours[closestSchoolVor[i]])
   print('Citizen ' + str(citizens[i]) + ' is at school ' + str(schools[closestSchool]) + '. He has ' + str(steps) + ' steps to walk.')
   city = manhattanSchools1.labyrinthCleaning(city, n)



