import streamlit as st

st.title("Análise de funil")

tab1, tab2 = st.tabs(["Funil Padrão", "Funil Invertido"])


with tab1:
    col1, col2, col3 = st.columns(3)    
    with col1:
        visitors = st.number_input("Escolha o número de visitantes", step=1)
        # leads = st.number_input("Escolha o número de leads gerados pelo MKT", step=1)
        # qualified_leads = st.number_input("Escolha o número de leads", step=1)
        # meetings = st.number_input("Escolha o número de reuniões agendadas", step=1)
        # deals = st.number_input("Escolha o número de negócios fechados", step=1)

    with col2:
        tx_visitors_to_leads = st.number_input("Taxa: Visitantes > Leads", min_value=0.0, max_value=100.0, value=5.0, step=0.1) / 100
        tx_leads_to_qualified_leads =  st.number_input("Taxa: Leads > Leads qualificados", min_value=0.0, max_value=100.0, value=16.2, step=0.1) / 100
        tx_qualified_leads_to_meetings =  st.number_input("Taxa: Leads qualificados > Reunião agendada", min_value=0.0, max_value=100.0, value=40.0, step=0.1) / 100
        tx_meetings_to_deal =  st.number_input("Taxa: Reuniões > Negócio fechado", min_value=0.0, max_value=100.0, value=15.0, step=0.1) / 100

    with col3:
        leads = round(visitors * tx_visitors_to_leads)
        st.write('Leads gerados')
        st.write(leads)

        qualified_leads = round(leads * tx_leads_to_qualified_leads)
        st.write('Leads qualificados')
        st.write(qualified_leads)

        meetings = round(qualified_leads * tx_qualified_leads_to_meetings)
        st.write('Reuniões agendadas')
        st.write(meetings)

        deals = round(meetings *  tx_meetings_to_deal)
        st.write('Negócios fechados')
        st.write(deals)

with tab2:
    col1, col2, col3 = st.columns(3)    
    with col1:
        # visitors = st.number_input("Escolha o número de visitantes", step=1)
        # leads = st.number_input("Escolha o número de leads gerados pelo MKT", step=1)
        # qualified_leads = st.number_input("Escolha o número de leads", step=1)
        # meetings = st.number_input("Escolha o número de reuniões agendadas", step=1)
        deals_inv = st.number_input("Escolha a quantidade de vendas", step=1)

    with col2:
        tx_meetings_to_deal_inv =  st.number_input("Taxa: Reuniões > Vendas", min_value=0.0, max_value=100.0, value=15.0) / 100
        tx_qualified_leads_to_meetings_inv =  st.number_input("Taxa: Qualificação > Reunião agendada", min_value=0.0, max_value=100.0, value=40.0) / 100
        tx_leads_to_qualified_leads_inv =  st.number_input("Taxa: Leads > Qualificação", min_value=0.0, max_value=100.0, value=16.2) / 100
        tx_visitors_to_leads_inv = st.number_input("Taxa: Visitantes > Leads ", min_value=0.0, max_value=100.0, value=5.0) / 100

    with col3:
        meetings_inv = int(round(deals_inv / tx_meetings_to_deal_inv, 2))
        st.write('Reuniões agendadas')
        st.write(meetings_inv)

        qualified_leads_inv = int(round(meetings_inv / tx_qualified_leads_to_meetings_inv, 2))
        st.write('Leads enviados para Qualificação')
        st.write(qualified_leads_inv)

        leads_inv = int(round(qualified_leads_inv / tx_leads_to_qualified_leads_inv, 2))
        st.write('Leads gerados pelo Marketing')
        st.write(leads_inv)

        visitors_inv = int(round(leads_inv / tx_visitors_to_leads_inv, 2))
        st.write('Visitantes no site')
        st.write(visitors_inv)


with st.expander("As taxas apresentadas acima são valores de mercado. Mais informações:"):
    st.write("Taxa de visitantes para leads - 5% (Fonte: RD Station, segmento Serviços de RH e Coaching)")
    st.write("Taxa de leads para oportunidades (qualificação) - 16,20% (Fonte: RD Station, segmento Serviços de RH e Coaching)")
    st.write("Taxa de leads enviados para qualificação para reuniões agendadas - 40% (Fonte: Time de qualificação e dados de inbound)")
    st.write("Taxa de reuniões para vendas - 15% (Fonte: Time de vendas e consultoria SC)")