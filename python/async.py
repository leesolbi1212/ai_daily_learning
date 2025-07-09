import asyncio
import time


#동기 함수
def sync_func():
    print('동기 함수 시작')
    time.sleep(2)
    print('동기 함수 끝')
    
sync_func()

#비동기 함수 
async def async_func():
    print('비동기 함수 시작')
    await asyncio.sleep(2)
    print('비동기 함수 끝')
    
# 비교 실행 함수 
async def main():
    print("동기 함수 시작")
    sync_func()
    sync_func()
    
    print('비동기 함수 시작')
    await asyncio.gather(
        async_func(),
        async_func()
    )

asyncio.run(main())
