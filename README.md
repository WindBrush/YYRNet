# 脚本说明

## run_zmap.sh

注意为了方便，ip 和子网掩码直接硬编码了。

运行方式：

```
# 在默认常用端口上进行 zmap
bash run_zmap.sh

# 在指定端口上进行 zmap
bash run_zmap.sh <port1> [port2, ...]
```

运行时会询问是否跳过已有输出文件的端口，若不跳过则会向输出文件名后加 `_<ind>` 以避免文件冲突。
