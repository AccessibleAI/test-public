require 'fileutils'    
FileUtils.cp_r '.', '../custom'
FileUtils.cp_r '../custom', 'custom'
FileUtils.rm_r '../custom'
