import asyncio
import logging
from typing import Callable, Any, Optional

logger = logging.getLogger("PyFluxSync")

class AsyncSyncManager:
    """一個用於管理非同步任務執行與安全重試機制的原創輕量工具類別。"""

    def __init__(self, max_retries: int = 3, delay: float = 1.0):
        self.max_retries = max_retries
        self.delay = delay

    async def execute_with_retry(self, coro_func: Callable[..., Any], *args: Any, **kwargs: Any) -> Optional[Any]:
        attempts = 0
        while attempts < self.max_retries:
            try:
                result = await coro_func(*args, **kwargs)
                return result
            except Exception as e:
                attempts += 1
                logger.warning(f"執行失敗 (嘗試次數 {attempts}/{self.max_retries}): {e}")
                if attempts >= self.max_retries:
                    logger.error("已達到最大重試次數，任務終止。")
                    raise
                await asyncio.sleep(self.delay * attempts)
        return None