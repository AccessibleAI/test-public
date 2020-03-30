Dir.chdir("test_files")
a= Dir.glob("*")[0]
time = (Time.now).strftime("%H:%M:%S_%d/%m/%y")
File.rename(a, "file_#{time}.txt")
