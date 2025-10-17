import time
import asyncio
import base58  # 需要安装：pip install base58
from solana.rpc.async_api import AsyncClient  # 需要安装： pip install solana solders
from solders.system_program import transfer, TransferParams
from solders.keypair import Keypair
from solders.message import MessageV0
from solders.transaction import VersionedTransaction

# 替换为你的 Solana RPC 端点
RPC_ENDPOINT = "https://solana-mainnet.g.alchemy.com/v2/xxxxxxxxxx"

# 替换为你的私钥（Base58 编码）
PRIVATE_KEY = "seeker地址的私匙"  # sol手机seeker地址的私匙

async def send_zero_transfer():
    # 初始化异步客户端
    client = AsyncClient(RPC_ENDPOINT)
    
    # 从私钥加载密钥对
    private_key_bytes = base58.b58decode(PRIVATE_KEY)
    keypair = Keypair.from_bytes(private_key_bytes)
    from_pubkey = keypair.pubkey()
    to_pubkey = from_pubkey  # 发送给自己
    
    # 创建转账指令：0 SOL
    transfer_instruction = transfer(
        TransferParams(
            from_pubkey=from_pubkey,
            to_pubkey=to_pubkey,
            lamports=0  # 0 金额转账
        )
    )
    
    # 获取最新块哈希
    recent_blockhash_resp = await client.get_latest_blockhash()
    recent_blockhash = recent_blockhash_resp.value.blockhash
    
    # 编译消息
    msg = MessageV0.try_compile(
        payer=from_pubkey,
        instructions=[transfer_instruction],
        address_lookup_table_accounts=[],
        recent_blockhash=recent_blockhash,
    )
    
    # 创建并签名交易
    transaction = VersionedTransaction(msg, [keypair])
    
    # 发送交易
    try:
        tx_sig = await client.send_transaction(transaction)
        print(f"交易签名: {tx_sig.value}")
        # 等待确认（可选）
        await client.confirm_transaction(tx_sig.value)
        print("交易已确认")
    except Exception as e:
        print(f"发送交易失败: {e}")
    finally:
        await client.close()

def main():
    while True:
        print("发送 0 SOL 转账...")
        asyncio.run(send_zero_transfer())
        print("等待下一个小时...")
        time.sleep(3600)  # 每小时一次 (3600 秒)

if __name__ == "__main__":
    main()
