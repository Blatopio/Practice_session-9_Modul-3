from langchain_core.prompts  import PromptTemplate

prompt = PromptTemplate(
    input_variables=["input_user"],
    template="jelaskan berdasarkan {input_user} dengan bahasa yang mudah dipahami oleh user dengan umur 10 tahun",

)