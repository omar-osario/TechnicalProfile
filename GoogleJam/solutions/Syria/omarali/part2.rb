#!/usr/bin/env ruby
def normal(n)
  a = (n/3).round
  a = a + 1 if n%3 > 0
  b = (n/3).round
  b = b + 1 if n%3 == 2
  c = (n/3).round
  return [a, b, c]
end

def exceptional(n)
  return normal(n) if n<2 or n>28
  return [2, 0, 0] if n == 2
  return [10, 10, 8] if n == 28
  n = n - 3
  a = (n/3).round + 2
  a = a + 1 if n%3 > 0
  b = (n/3).round + 1
  b = b + 1 if n%3 == 2
  c = (n/3).round
  return [a, b, c]
end

STDIN.readline.to_i.times.each do |i|
  scores = STDIN.readline.split.map { |i| i.to_i }
  n = scores.shift
  s = scores.shift
  p = scores.shift
  a=0 and b=0 and c=0 and d=0
  count = 0
  scores.each do |s|
    n = normal(s).keep_if { |x| x >= p }.count > 0
    e = exceptional(s).keep_if { |x| x >= p }.count > 0
    a = a + 1 if n and e
    b = b + 1 if n and not e
    c = c + 1 if not n and e
    d = d + 1 if not n and not e
  end
  count = s < c ? a + b + s : a + b + c
  puts "Case \##{i+1}: #{count}"
end
