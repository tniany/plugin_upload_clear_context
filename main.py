from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from astrbot.api.message_components import Markdown

@register("clear_context", "Author", "一个用于清除模型上下文的插件", "1.0.0")
class ClearContextPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """插件初始化方法"""
        logger.info("ClearContextPlugin initialized")

    # 注册清除上下文指令
    @filter.command("clear")
    async def clear_context(self, event: AstrMessageEvent):
        """清除模型上下文"""
        # 尝试清除上下文
        try:
            # 获取当前会话的上下文管理器
            session = event.get_session()
            if session:
                # 清除上下文
                await session.clear_context()
                yield event.plain_result("✅ 上下文已成功清除")
            else:
                yield event.plain_result("❌ 无法获取会话信息")
        except Exception as e:
            logger.error(f"清除上下文失败: {e}")
            yield event.plain_result(f"❌ 清除上下文失败: {str(e)}")

    # 注册查看上下文指令
    @filter.command("context")
    async def show_context(self, event: AstrMessageEvent):
        """查看当前上下文信息"""
        try:
            session = event.get_session()
            if session:
                context = session.get_context()
                if context:
                    # 构建 Markdown 消息
                    md_content = f"""
## 当前上下文信息

### 上下文长度
{len(str(context))} 字符

### 上下文内容
```
{str(context)[:500]}...
```
                    """
                    yield event.result([Markdown(md_content)])
                else:
                    yield event.plain_result("当前无上下文信息")
            else:
                yield event.plain_result("❌ 无法获取会话信息")
        except Exception as e:
            logger.error(f"查看上下文失败: {e}")
            yield event.plain_result(f"❌ 查看上下文失败: {str(e)}")

    # 注册帮助指令
    @filter.command("clear_help")
    async def show_help(self, event: AstrMessageEvent):
        """显示插件帮助信息"""
        md_content = f"""
## 清除上下文插件帮助

### 指令列表
- `/clear` - 清除当前模型上下文
- `/context` - 查看当前上下文信息
- `/clear_help` - 显示此帮助信息

### 功能说明
此插件用于管理模型上下文，可帮助解决上下文过长导致的问题，提高模型响应质量。
        """
        yield event.result([Markdown(md_content)])

    async def terminate(self):
        """插件销毁方法"""
        logger.info("ClearContextPlugin terminated")
