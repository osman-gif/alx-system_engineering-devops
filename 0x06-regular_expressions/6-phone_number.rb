#!/usr/bin/env ruby
puts ARGV[0].scan(/\A\d{9,9}\d\Z/).join
