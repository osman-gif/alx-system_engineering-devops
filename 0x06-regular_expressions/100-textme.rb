#!/usr/bin/env ruby
output = ARGV[0].split(' ')

puts output[14].scan(/\f(?=\r)\.+/).join
puts output[15].scan(/^+.+/).join
puts output[16].scan(/\d+./).join
