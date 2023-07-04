#!/usr/bin/env ruby
input = ARGV[0]
matches = input.scan(/hb(t{2,})n/)
puts matches.join("\n")

