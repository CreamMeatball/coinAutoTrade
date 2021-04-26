import pyupbit

access = "TfXKG8U1ixCw6Uxv16vUpro6WiOkymqDmaVBIOsN"          # 본인 값으로 변경
secret = "jxffIaSwwOJgEL7e5VNqGKmep3cNFH89hNixp8pO"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회