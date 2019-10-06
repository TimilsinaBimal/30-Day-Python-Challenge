# Jack bought a 400 hot dogs for the school picnic.
# If they were contained in packages of 8 hot dogs,
# hot many total packages did he buy?
# Create a python program without using / or % operator

totalHotDogs = 400
hotDogsPerPackage = 8
totalContainer = 0
while(totalHotDogs >= hotDogsPerPackage):
    totalHotDogs -= hotDogsPerPackage
    totalContainer += 1
print(f"He bought {totalContainer} packages.")
