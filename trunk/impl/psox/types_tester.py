import psoxtypes as types

print types.VARG(types.STRING).fromtype("\x01\x01a\x00\x00")

print types.VARG(types.FBYTES(1)).fromtype("\x01b\x01c\x01d\x00")

print types.VARG(types.VARG(types.STRING)).fromtype("\x01\x01a\x00\x01b\x00\x01c\x00\x00\x01\x011\x00\x012\x00\x0134\x00\x00\x00")
