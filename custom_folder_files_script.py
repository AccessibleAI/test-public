import os
os.system('touch file_unsynced')
if not os.path.exists('custom'):
        os.makedirs('custom')
os.system('cd custom')
os.system('touch custom_file_synced')
os.system('touch hello.text')
