import os
os.system('touch file_unsynced')
if not os.path.exists('output'):
        os.makedirs('output')
os.system('cd output')
os.system('touch output_file_synced')
os.system('touch hello.text')
