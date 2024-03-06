def cube(top: int):
    return {number: number**3 for number in range(1, top)}


ten_cubes = cube(10)

print(ten_cubes)
