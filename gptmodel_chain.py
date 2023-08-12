from langchain.llms  import  OpenAI
myllm = OpenAI( 
    model = 'text-davinci-003' , 
    temperature=1,
    openai_api_key=mygptkey
)

from langchain.prompts import PromptTemplate
mylwprompt = PromptTemplate(
    template="tell me 2 best {item} in {country}." ,  
    input_variables=["item", "country"] )

from langchain.chains import LLMChain
mychain = LLMChain(
    llm=myllm, 
    prompt=mylwprompt
)
mychain.run(item="food" , country="europe")
