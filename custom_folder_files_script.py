import os
os.system('touch file_unsynced')
if not os.path.exists('custom'):
        os.makedir('custom')
os.system('cd custom')
os.system('touch custom_file_synced')
os.system('touch hello.text')
