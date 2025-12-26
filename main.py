import streamlit as st

def main():
    st.title("Rebalance Your Portfolio")
    col1, col2 = st.columns(2, gap="large", border=True)
   

    with col1:
        age = st.slider("How old are you?", 18,100)
        domestic = st.text_input("Domestic mutual funds ($):", value="0")
        international = st.text_input("International mutual funds ($)", value="0")
        bonds = st.text_input("Bonds ($)", value="0")

    with col2:
        st.markdown("**Recommended Target Allocation**", width="content")
        st.divider()
        domestic_output = calculate_domestic(age, domestic)
        international_output = calculate_international(age, international)
        bonds_output = calculate_bonds(age, bonds)
        st.markdown(domestic_output)
        st.markdown(international_output)
        st.markdown(bonds_output)
        
    

def calculate_domestic(domestic, age):
    return "Domestic Target: $75,000 (70%)"

def calculate_international(international, age):
    return "International Target: $75,000 (70%)"

def calculate_bonds(bonds, age):
    return "Bonds Target: $75,000 (70%)"

if __name__ == "__main__":
    main()