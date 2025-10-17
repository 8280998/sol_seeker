# sol_seeker
sol手机seeker刷活跃脚本 声明：运行前自行检查代码安全。运行后产生任何问题均与本脚本无关。

solana手机seeker上线了钱包活跃面板，有可能空投加成。脚本是钱包地址自转0，间隔时间可以自定义，默认为1小时一次。


## 1 运行环境安装

    pip3 install base58
    pip3 install solana solders
## 2 添加私匙和RPC

修改脚本内的私匙为seerker钱包私匙，以及rpc地址。

## 3 运行
    python3 seeker.py
