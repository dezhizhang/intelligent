from dataclasses import dataclass
from typing import Optional, List

from app.domain.shared.vo import UserId


@dataclass
class GetOrdersQuery:
    user_id: UserId
    limit: Optional[int] = 10
    offset: Optional[int] = 0

@dataclass
class OrderDTO:
    """订单数据传输对像"""
    id: int
    order_number:str
    total_amount:float
    status:str
    created_at:str
    updated_at:str

@dataclass
class GetOrdersResult:
    """获取用户订单结果"""
    orders: List[OrderDTO]
    total: int

class GetOrdersHandler:
    """获取订单查询处理器"""
    def __init__(self):
        pass

    async def handle(self,query:GetOrdersQuery) -> GetOrdersResult:
        """处理获取订单查询"""
        if query.user_id.value <=0:
            raise ValueError("用户id必须大于0")
        if query.limit <=0 or query.limit >100:
            raise ValueError("限制数量必须大于0且小于100")
        if query.offset <0:
            raise ValueError("偏移量不能为负数")

        orders = [
            OrderDTO(id=1,order_number="orm",total_amount=99,status="待处理",created_at="2030-05-01",updated_at="2030-05-01"),
        ]

        start = query.offset or 0
        end = start + (query.limit or 100)

        page_order = orders[start:end]

        return GetOrdersResult(orders=page_order, total=len(orders))








    