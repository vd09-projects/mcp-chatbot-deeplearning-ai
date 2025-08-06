from L4.mcp_chatbot import MCP_ChatBot
import asyncio

async def main():
    chatbot = MCP_ChatBot()
    try:
        # the mcp clients and sessions are not initialized using "with"
        # like in the previous lesson
        # so the cleanup should be manually handled
        await chatbot.connect_to_servers()
        await chatbot.chat_loop()
    finally:
        await chatbot.cleanup()
  

if __name__ == "__main__":
  asyncio.run(main())