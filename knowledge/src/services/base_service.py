from idlelib.window import add_windows_to_menu
from typing import List,TypeVar,Generic,Type
from pydantic import BaseModel
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.dao.base_dao import BaseDAO

DTOType = TypeVar('DTOType',bound=BaseModel)

class BaseService(Generic[DTOType]):
    def __init__(self,dao:BaseDAO,dto_class:Type[DTOType]):
        """
        初始化BaseService
        :param dao:
        :param dto_class:
        """
        self.dao = dao
        self.dto_class = dto_class

    async def create(self,**kwargs) -> DTOType:
        """通用创建方法"""
        instance = self.dao.create(**kwargs)
        return self.dto_class.model_validate(instance)

    async def batch_create(self,objects: List[DTOType],**kwargs) -> List[DTOType]:
        """批量创建方法"""
        instance = await self.dao.batch_create(objects)
        return [self.dto_class.model_validate(instance) for instance in instance]

    async def get_by_id(self,id) -> DTOType:
        """通过主键获取记录"""
        instance = await self.dao.get_by_primary_key(id)
        if instance:
            return self.dto_class.model_validate(instance)
        return None




