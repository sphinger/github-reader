from fastapi import FastAPI, BackgroundTasks
import httpx

app = FastAPI()

async def send_pushover_message_in_background(payload):
    url = 'https://api.pushover.net/1/messages.json'
    async with httpx.AsyncClient() as client:
        response = await client.post(url, data=payload)
        print(response.json())  # 将调用结果输出到控制台

@app.get("/redpack")
async def sendMsg(background_tasks: BackgroundTasks):
    payload = {
        'token': 'ah9rsvq9qmza47o3hj9nh83fqk6uuj',
        'user': 'ucvybysmpj5qmuu4ngip6hm1fh6e1x',
        'message': '您有新的家族红包'
    }

    # 将任务添加到后台
    background_tasks.add_task(send_pushover_message_in_background, payload)

    # 立即返回响应
    return {"message": "红包发送请求已接收"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=80)
