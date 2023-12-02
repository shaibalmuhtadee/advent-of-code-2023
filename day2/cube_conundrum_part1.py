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
  

MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14

def is_game_possible(game):
  red_cubes = green_cubes = blue_cubes = 0
  for cube_set in game.sets:
    red_cubes = cube_set.red_cubes
    green_cubes = cube_set.green_cubes
    blue_cubes = cube_set.blue_cubes

    if (red_cubes > MAX_RED_CUBES or green_cubes > MAX_GREEN_CUBES or blue_cubes > MAX_BLUE_CUBES):
      return False
  return True



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
    if(is_game_possible(game)):
      result += game.id

  print(result)