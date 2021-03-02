require 'fileutils'    
FileUtils.touch "file_unsynced"
FileUtils.mkdir "custom" unless File.exists?('custom')
Dir.chdir ("custom")
FileUtils.touch "custom_file_synced"
FileUtils.touch "hello.text"
