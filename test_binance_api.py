import ccxt

try:
    # 初始化 Binance 实例，连接正式环境
    binance = ccxt.binance({
        'rateLimit': 1200,
        'enableRateLimit': True,  # 启用速率限制
        'urls': {
            'api': 'https://api.binance.com'  # 使用正式 API URL
        }
    })
    
    # 加载交易对信息
    markets = binance.load_markets()
    
    # 打印结果
    print(f"交易对数量: {len(markets)}")
    print(f"是否包含 BTC/USDT: {'BTC/USDT' in markets}")
except Exception as e:
    print(f"错误：{e}")
