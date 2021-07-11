import os
arr =["output_file_synced","hello.text"]
f = open("file_unsynced", "a")
f.close()
if not os.path.exists("custom"):
  os.mkdir("custom")
for i in arr:
  f = open("custom/{}".format(i), "a")
  f.write("Now the file has more content! {}".format(i))
  f.close()
