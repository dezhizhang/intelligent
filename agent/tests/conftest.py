import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture(scope="session")
def client() -> TestClient:
    """创建一个可供所有测试用例使用的TestClient客户端"""
    with TestClient(app) as c:
        yield c