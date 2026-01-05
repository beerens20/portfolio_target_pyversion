import streamlit as st

def calculate_bonds(age, total_portfolio_value):
    """Calculate recommended bond allocation: age % of total portfolio"""
    bond_percentage = age / 100
    bond_amount = bond_percentage * total_portfolio_value
    return bond_amount, bond_percentage

def calculate_stocks(remaining_value, domestic_ratio=0.7):
    """
    Split remaining value (after bonds) into domestic and international.
    Default: 70% domestic, 30% international of the stock portion.
    """
    domestic_amount = remaining_value * domestic_ratio
    international_amount = remaining_value * (1 - domestic_ratio)
    return domestic_amount, international_amount

def main():
    st.title("Rebalance Your Portfolio")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("### Your Current Portfolio")
        age = st.slider("How old are you?", 18, 100, 40)
        st.divider()

        domestic_current = st.number_input("Current Domestic Stocks/Mutual Funds ($)", min_value=0.0, value=50000.0)
        international_current = st.number_input("Current International Stocks/Mutual Funds ($)", min_value=0.0, value=20000.0)
        bonds_current = st.number_input("Current Bonds ($)", min_value=0.0, value=30000.0)

    # Calculate total
    total_portfolio_value = domestic_current + international_current + bonds_current

    # Recommended allocations
    bond_amount, bond_pct = calculate_bonds(age, total_portfolio_value)
    remaining_after_bonds = total_portfolio_value - bond_amount

    domestic_target, international_target = calculate_stocks(remaining_after_bonds, domestic_ratio=0.7)

    with col2:
        st.markdown("### Recommended Target Allocation")
        st.write(f"**Total Portfolio Value:** ${total_portfolio_value:,.2f}")
        st.divider()

        st.markdown("**Summary**")
        
        st.markdown(f"- Domestic Stocks: ${domestic_target:,.2f} ({70}% of stocks)")
        st.markdown(f"- International Stocks: ${international_target:,.2f} ({30}% of stocks)")
        st.markdown(f"- Bonds: ${bond_amount:,.2f} ({age}%)")

if __name__ == "__main__":
    main()