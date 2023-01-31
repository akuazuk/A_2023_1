import streamlit as st

def calculate_probability(prior_a, prior_b, likelihood_a, likelihood_b, evidence):
    posterior_a = (prior_a * likelihood_a) / evidence
    posterior_b = (prior_b * likelihood_b) / evidence
    return posterior_a, posterior_b

def main():
    st.title("Bayes Theorem Probability Calculator")
    st.write("Enter prior probabilities and likelihood ratios:")
    prior_a = st.number_input("Prior probability of Hypothesis A", 0.5, min_value=0, max_value=1)
    prior_b = st.number_input("Prior probability of Hypothesis B", 0.5, min_value=0, max_value=1)
    likelihood_a = st.number_input("Likelihood ratio of Hypothesis A", 1, min_value=0)
    likelihood_b = st.number_input("Likelihood ratio of Hypothesis B", 1, min_value=0)
    evidence = prior_a * likelihood_a + prior_b * likelihood_b
    posterior_a, posterior_b = calculate_probability(prior_a, prior_b, likelihood_a, likelihood_b, evidence)
    st.write("Posterior probabilities:")
    st.write("Posterior probability of Hypothesis A: ", posterior_a)
    st.write("Posterior probability of Hypothesis B: ", posterior_b)

if __name__ == '__main__':
    main()

