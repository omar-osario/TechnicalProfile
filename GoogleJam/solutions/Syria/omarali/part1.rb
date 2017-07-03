#!/usr/bin/env ruby
STDIN.readline.to_i.times.each { |i| puts "Case \##{i+1}: #{STDIN.readline.gsub(/[a-z]/,'y'=>'a','n'=>'b','f'=>'c','i'=>'d','c'=>'e','w'=>'f','l'=>'g','b'=>'h','k'=>'i','u'=>'j','o'=>'k','m'=>'l','x'=>'m','s'=>'n','e'=>'o','v'=>'p','z'=>'q','p'=>'r','d'=>'s','r'=>'t','j'=>'u','g'=>'v','t'=>'w','h'=>'x','a'=>'y','q'=>'z')}" }
