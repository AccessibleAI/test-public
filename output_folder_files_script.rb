require 'fileutils'    
FileUtils.cp_r '.', '../output'
FileUtils.cp_r '../output', 'output'
FileUtils.rm_r '../output'
FileUtils.rm_r 'output/.git'
