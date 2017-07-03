#!/usr/bin/env ruby
def recycled?(n, m)
  n_ary = n.to_s.split('')
  n_ary.count.times { |x| return true if m == n_ary.rotate(-x-1).join.to_i }
  false
end
STDIN.readline.to_i.times.each do |i|
  a, b = STDIN.readline.split.map { |x| x.to_i }
  count = 0
  (a..b-1).each { |n| (n+1..b).each { |m| count = count + 1 if recycled?(n, m) } }
  puts "Case \##{i+1}: #{count}"
end
