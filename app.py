import streamlit as st
from cases import CASES
from prompts import PROMPTS
from evaluator import evaluate_all
from runner import combine, call_model, parse_answer

st.title("Prompt Evaluation Harness")

tab1, tab2 = st.tabs(["Classify a message", "Compare prompts"])

with tab1:
    st.write("Type a message and see how the model classifies it.")

    text = st.text_input("Message:", "cancel my order")
    prompt_name = st.selectbox("Prompt variant:", list(PROMPTS.keys()))

    if st.button("Classify"):
        template = PROMPTS[prompt_name]
        prompt = combine(template, text)
        raw = call_model(prompt)
        category = parse_answer(raw)
        st.success(f"Category: {category}")
        st.caption(f"Raw model output: {raw}")


with tab2:
    st.write("Run all prompts over all test cases and compare metrics.")

    if st.button("Run evaluation"):
        with st.spinner("Running, this may take a while..."):
            results = evaluate_all(PROMPTS, CASES)
        st.subheader("Results")
        for name, scores in results.items():
            st.write(
                f"**{name}** — accuracy: {scores['accuracy']:.2f}, "
                f"consistency: {scores['consistency']:.2f}"
            )