# MCCC

A C to Minecraft Commands compiler.

To use, write
```bash
python3 src/compile.py <src>.c [--file-input] 
```

Including `--file-input` makes the script's stdin be `input.txt`, otherwise it expects
a reverse array of byte values in `storage` `mccc:main input`.

Since following the entire C specifications is hard, the compiler is currently incomplete.
If you see any feature which is missing, please create an issue about it.