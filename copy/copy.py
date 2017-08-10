__author__ = 'berserker5000'

import shutil, os, hashlib

master_dir = "e:\\old"
copy_dir = "e:\\new"


def md5sum(filename, blocksize=65536):
    hash = hashlib.md5()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(blocksize), b""):
            hash.update(block)
    return hash.hexdigest()


for p in os.listdir(master_dir):
    copyfile(p, copy_dir)

    '''
    for l in os.listdir(copy_dir):
        print(l)

        if md5sum(str(p)) == md5sum(str(l)):
            pass
        else:
            shutil.copyfile(p,copy_dir)
                    '''
