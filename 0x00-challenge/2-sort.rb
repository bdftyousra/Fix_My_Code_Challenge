#!/usr/bin/env ruby

def sort_array(array)
  numbers = array.select { |item| item.is_a?(Numeric) }
  strings = array.select { |item| item.is_a?(String) }

  sorted_numbers = numbers.sort
  sorted_strings = strings.sort

  sorted_numbers.each { |num| puts num }
  sorted_strings.each { |str| puts str }
end

if __FILE__ == $0
  if ARGV.empty?
    puts "Usage: #{$0} <list_of_elements>"
    exit(1)
  end

  array = ARGV.map { |item| item.to_i.to_s == item ? item.to_i : item }
  sort_array(array)
end

