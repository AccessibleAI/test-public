import uuid
import time
uuid = str(uuid.uuid4())
f = open("output/{}.txt".format(uuid), "a")
f.write("Now the file has more content! {}".format(uuid))
f.close()
time.sleep(45)
