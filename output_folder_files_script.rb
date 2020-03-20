require 'fileutils'
FileUtils.touch "file_unsynced"
FileUtils.mkdir "output" unless File.exists?('output')
Dir.chdir ("output")
FileUtils.touch "output_file_synced"
FileUtils.touch "hello.text"

