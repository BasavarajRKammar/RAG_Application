from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_groq import ChatGroq
from langchain_community.chat_message_histories import ChatMessageHistory
import os
from dotenv import load_dotenv
from app.services.retrieval_service import get_vectorDb
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.chains import create_history_aware_retriever,create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
groq_api_key = os.getenv('GROQ_API_KEY')
message: str
store = {}
def get_question(msg: str):
    global message
    message = msg
    print('message by the user', message)
    # get_response(message)
def get_response():
    question = 'meaning of attention all you needed?'
    vector_db = get_vectorDb()
    retriever = vector_db.as_retriever(search_kwargs={"k": 3})

    llm = ChatGroq(model="llama-3.3-70b-versatile",temperature=0, groq_api_key=groq_api_key)
    prompt = ChatPromptTemplate.from_messages([
        ('system','hey your special assistant for the answer the question based on the document that user uploaded'),
        MessagesPlaceholder(variable_name='chat_history'),
        ('user','{input}')
    ])
    # prompt = ChatPromptTemplate.from_template("""
    # You are a helpful assistant.

    # <context>
    # {context}
    # </context>

    # Question: {input}
    # Answer:
    # """)
    contextual_q_system_prompt = (
            "Given a chat history and the latest user question"
            "which might reference context in the history"
            "formulate a standalone question which can be understood"
            "without the chat history.Do not answer the question,"
            "just reformulted if it is needed othewise return as it is" 
        )
    contextual_q_prompt = ChatPromptTemplate.from_messages(
            [
                ('system',contextual_q_system_prompt),
                 MessagesPlaceholder('chat_history'),
                 ('user',"{input}")

            ]
        )
    histroy_aware_retriever =create_history_aware_retriever(llm,retriever,contextual_q_prompt)
     # Create a question and answer prompt
    system_prompt = (
    "You are an assistant answering questions based on uploaded documents "
    "and previous conversation.\n"
    "Use the provided document context if relevant.\n"
    "If the user asks about previous discussion topics, use the chat history.\n"
    "If the answer is not found, say you don't know.\n\n"
    "Document Context:\n{context}"
    "{context}"
        )

    question_answer_prompt = ChatPromptTemplate.from_messages(
            [
                ('system',system_prompt),
                MessagesPlaceholder('chat_history'),
                ('user','{input}')
                
            ]
        )
    
    def get_sessionid(session_id: str):
        if session_id not in store:
            store[session_id]=ChatMessageHistory()
        return store[session_id]
    question_answer_chain = create_stuff_documents_chain(llm,question_answer_prompt)
    rag_chain = create_retrieval_chain(histroy_aware_retriever,question_answer_chain)
    conversational_rag_history = RunnableWithMessageHistory(
            rag_chain,get_sessionid,
            input_messages_key='input',
            history_messages_key='chat_history',
            output_messages_key='answer',
        )
   
    response = conversational_rag_history.invoke(
    {"input": message},
    config={"configurable": {"session_id": "user1"}}
)
    history = store["user1"].messages
    chat_history = [
    {
        "role": msg.type,
        "content": msg.content
    }
    for msg in history
]
    return {
    "question": message,
    "answer": response["answer"],
    "history": chat_history
}
#     response = conversational_rag_history.invoke(
#                 {'input': message},
#                 config={
#                     "configurable":{"session_id":'user1'}
#                 },
#             )

#     # response = rag_chain.invoke(message)
# #     result = [
# #     {
# #         "page_content": response.page_content,
# #         "metadata": response.metadata
# #     }
# #     for doc in response
# # ]
#     print(response)
#     return response



