
def update_xy(x, y, dx, dy, new_level)
  x += dx
  y += dy
  if new_level
    dx = 0
    dy = 1
    new_level = false
  elsif x + y == 0
    if dx > 0  # go right to next level
      dx = 1
      dy = 0
      new_level = true
    else  # go down
      dx = 0
      dy = -1
    end
  elsif x == y  # left if upper right, right if bottom left
    dx = x > 0 ? -1 : 1
    dy = 0
  end
  [x, y, dx, dy, new_level]
end


def spiral_steps(n)
  x = -1
  y = 0
  dx = 1
  dy = 0
  new_level = false

  (1..n).each do
    x, y, dx, dy, new_level = update_xy(x, y, dx, dy, new_level)
  end
  x.abs + y.abs
end


def spiral_stress(n)
  x = -1
  y = 0
  dx = 1
  dy = 0
  coords = {}
  new_level = false

  s = 0
  i = 1
  until s > n do
    x, y, dx, dy, new_level = update_xy(x, y, dx, dy, new_level)
    s = i == 1 ? 1 : 0
    coords.values.each do |otherX, otherY, otherS|
      diffX = otherX - x
      diffY = otherY - y
      if diffX.abs < 2 and diffY.abs < 2  # in range
        s += otherS
      end
    end
    coords[i] = [x, y, s]
    i += 1
  end
  s
end


if __FILE__ == $0
  MY_INPUT = 289326
  puts 'Part 1'
  examples_1 = [1, 12, 23, 1024]
  examples_1.each do |example|
    solution = spiral_steps(example)
    puts "Solution to #{example}: #{solution}"
  end
  solution1 = spiral_steps(MY_INPUT)
  puts "Solution to part 1: #{solution1}"

  puts

  puts 'Part 2'
  examples_2 = [4, 15, 23, 800]
  examples_2.each do |example|
    solution = spiral_stress(example)
    puts "Solution to #{example}: #{solution}"
  end
  solution2 = spiral_stress(MY_INPUT)
  puts "Solution to part 2: #{solution2}"
end
