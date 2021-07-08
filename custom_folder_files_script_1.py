import os
arr =["file_unsynced","custom_file_synced","hello.text"] 
if not os.path.exists("custom"):
  os.mkdir("custom")
  for i in arr:
    f = open("custom/{}.txt".format(i), "a")
    f.write("Now the file has more content! {}".format(i))
    f.close()