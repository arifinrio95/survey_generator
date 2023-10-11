import streamlit as st
import openai

# Set API key dari OpenAI (Anda mungkin ingin menyembunyikannya atau menggunakan environment variables)
openai.api_key = st.secrets['user_api']

def generate_survey_questions(prompt):
    """
    Fungsi untuk menghasilkan list pertanyaan survey dari input user dengan bantuan ChatGPT.
    """
    
    messages = [
        {"role": "system", "content": "Aku akan membuatkan pertanyaan2 survey."},
        {"role": "user", "content": f"""Buatkan pertanyaan2 survey dari objective berikut: {prompt}"""}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        max_tokens=4000,
        temperature=0
    )
    questions = response.choices[0].message['content']
    
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=f"Suggest some survey questions based on: {prompt}",
#         max_tokens=150  # Anda dapat menyesuaikan ini sesuai kebutuhan
#     )
#     questions = response.choices[0].text.strip().split('\n')
    return questions

def main():
    st.title('Survey Question Generator')

    # User input penjelasan survey
    explanation = st.text_area("Provide a description of your survey:")
    
    if st.button('Generate Survey Questions'):
        questions = generate_survey_questions(explanation)
        st.write(questions)
        
        # if explanation:
        #     # Mendapatkan list pertanyaan survey
        #     questions = generate_survey_questions(explanation)
            
        #     st.subheader('Suggested Survey Questions:')
        #     for idx, question in enumerate(questions, 1):
        #         st.write(f"{idx}. {question}")
        # else:
        #     st.warning("Please provide a description for your survey.")

if __name__ == "__main__":
    main()
