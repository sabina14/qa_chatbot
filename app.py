import streamlit as st
import openai
from  langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv

load_dotenv()

