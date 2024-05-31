from langchain.chains import LLMChain
from langchain.llms.bedrock import Bedrock
from langchain.prompts import PromptTemplate
import boto3
import os


os.environ["AWS_PROFILE"] = "bedrock"

# bedrock client

bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

# one can try haiku or opus as well.
modelID = "anthropic.claude-v2"

llm = Bedrock(
    model_id=modelID,
    client=bedrock_client,
    model_kwargs={"max_tokens_to_sample": 2000, "temperature": 0.9}
)


def my_chatbot(language, Question):

    prompt = PromptTemplate(
        input_variables=["language", "Question"],
        template="You are a chatbot. You are in {language}.\n\n{Question}"
    )

    bedrock_chain = LLMChain(llm=llm, prompt=prompt)

    response = bedrock_chain({'language': language, 'freeform_text': Question})
    return response


# print(my_chatbot("english","Give me list of medical colleges in New York City?"))

