class Cube:
  def __init__(self, color, num):
    self.color = color
    self.num = num
    
  def __repr__(self):
    return "{}: {}".format(self.color, self.num)

class CubeSet:
  def __init__(self):
    self.red_cubes = 0
    self.green_cubes = 0
    self.blue_cubes = 0

  def add_cube(self, cube):
    if cube.color == 'red':
      self.red_cubes = int(cube.num)
    elif cube.color == 'green':
      self.green_cubes = int(cube.num)
    elif cube.color == 'blue':
      self.blue_cubes = int(cube.num)
  
  def __str__(self):
    return "___\nred_cubes: {},\ngreen_cubes: {},\nblue_cubes: {}\n".format(self.red_cubes, self.green_cubes, self.blue_cubes)

class Game:
  def __init__(self, id, sets):
    self.id = int(id)
    self.sets = sets

  def __str__(self):
    return "{}: {}".format(self,id, self.sets)
  
def calculate_power(game):
  red_cubes = []
  green_cubes = []
  blue_cubes = []
  for cube_set in game.sets:
    red_cubes.append(cube_set.red_cubes)
    green_cubes.append(cube_set.green_cubes)
    blue_cubes.append(cube_set.blue_cubes)

  red_cubes = [num for num in red_cubes if num != 0]
  min_red = max(red_cubes)
  green_cubes = [num for num in green_cubes if num != 0]
  min_green = max(green_cubes)
  blue_cubes = [num for num in blue_cubes if num != 0]
  min_blue = max(blue_cubes)

  power = min_red * min_green * min_blue
  return power


def parse_game_data(line):
  parts = line.split(':')
  game_id = parts[0].split()[1]
  set_of_cubesets = []

  parts = parts[1].split(';')
  for cube_set in parts:
    cube_set_str = cube_set.strip()
    
    cube_set = CubeSet()
    
    cubes = cube_set_str.split(',')
    for cube in cubes:
      cube = cube.strip()
      parts = cube.split()
      cube = Cube(parts[1], parts[0])
      cube_set.add_cube(cube)

    set_of_cubesets.append(cube_set) 
    
  return Game(game_id, set_of_cubesets)


with open("input.txt", 'r', encoding="utf-8") as f:
  result = 0
  for line in f:
    game = parse_game_data(line)
    power = calculate_power(game)
    result += power
  print(str(result))