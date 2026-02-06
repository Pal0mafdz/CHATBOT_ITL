from langchain_community.chains import PebbloRetrievalQA
from langchain_community.llms.huggingface_hub import HuggingFaceHub
from langchain_core.prompts import PromptTemplate

import os 
from dotenv import load_dotenv

load_dotenv()

def get_llm_chain(retriever):
    llm= HuggingFaceHub(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
         model_kwargs={
            "temperature": 0.2,
            "max_new_tokens": 512
        }
    )

    prompt=

