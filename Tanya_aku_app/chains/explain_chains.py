from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from prompts.explain_prompt import prompt
load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("MODEL"),
    max_tokens=int(os.getenv("MAX_TOKENS")),
    timeout=int(os.getenv("TIMEOUT"))
)

chains= prompt | llm