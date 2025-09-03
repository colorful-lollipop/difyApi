from fastapi import FastAPI, Body, HTTPException, Header
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class InputData(BaseModel):
    point: str
    params: dict = {}

@app.post("/now")
async def dify_receive(data: InputData = Body(...), authorization: str = Header(None)):
    """
    接收来自 Dify 的 API 查询数据
    """
    point = data.point
    
    # 处理 ping 验证请求
    if point == "ping":
        return {"result": "pong"}
    
    # 处理您的时间查询请求
    if point == "app.external_data_tool.query":
        return handle_time_query(params=data.params)
    
    raise HTTPException(status_code=400, detail="Not implemented")

def handle_time_query(params: dict):
    # 获取当前时间
    current_time = datetime.now()
    
    # 格式化日期和星期
    year = current_time.year
    month = current_time.month
    day = current_time.day
    
    weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    weekday = weekdays[current_time.weekday()]
    
    result = f"{year}年{month}月{day}日 {weekday}"
    
    return {"result": result}