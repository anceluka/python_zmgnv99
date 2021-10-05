import os
if os.path.exists('teksts.txt'):
    os.remove('teksts.txt')
else:
    print('fails neeksistē!')
os.rmdir('bildes')