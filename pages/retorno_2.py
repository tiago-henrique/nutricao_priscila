import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')
url = ("https://lmu.famerp.br/tiago/indicadores_2.csv")
df = pd.read_csv(url)

rt = df['data_v2'].count()

topografias = {
    1: 'Aparelho digestivo alto',
    2: 'Aparelho digestivo baixo',
    3: 'Bilio pancreática',
    4: 'Fígado',
    5: 'Ginecologia',
    6: 'Hematologia',
    7: 'Mastologia',
    8: 'Otorrino',
    9: 'Pulmão',
    10: 'Urologia',
    11: 'Neurologia',
    12: 'Pele/Melanoma',
    13: 'Outros oncológicos',
    14: 'Não oncológicos'
}

modalidade_tratamento = {
    1: 'Estadiamento',
    2: 'Clínico',
    3: 'Cirúrgico (até 45 dias pré ou pós)',
    4: 'Reestadiamento',
    5: 'Seguimento clínico',
    6: 'Cuidados paliativo pleno'
}

ganho_ponderal = {
    1: 'Ganho intencional',
    2: 'Manutenção',
    3: 'Falha do emagrecimento'
}

perda_ponderal = {
    1: 'Intencional',
    2: 'Perda Ponderal não Intencional'
}

asg = {
    1: 'Bem nutrido',
    2: 'Desnutrição suspeita ou moderada',
    3: 'Gravemente desnutrido'
}

via_alimentar = {
    1: 'Oral',
    2: 'Oral e suplementação nutricional',
    3: 'Oral e enteral',
    4: 'Enteral'
}

modalidade = {
    1: 'Presencial',
    2: 'Telemedicina'
}

tipo_via = {
    1: 'SNE',
    2: 'Gastrostomia',
    3: 'Jejunostomia'
}

tomo = {
    0: 'Não',
    1: 'Sim'
}

col0, col01 = st.columns([4,1])
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)
col7, col8 = st.columns(2)
col9, col10 = st.columns(2)
col11, col12 = st.columns(2)
col13, col14 = st.columns(2)
col14_1, col14_2 = st.columns(2)
col14_3, col14_4 = st.columns(2)
col15, col16 = st.columns([4,1])
col15_0, col15_1 = st.columns([1,7])
col17, col18 = st.columns(2)
col19, col20 = st.columns(2)
col21, col22 = st.columns(2)
col23, col24 = st.columns(2)
col25, col26 = st.columns(2)
col27, col28 = st.columns(2)
col29, col30 = st.columns(2)
col31, col32 = st.columns(2)

#Criando os Gráficos dos Pacientes em Primeira Consulta
col0.title('Retorno')
col1.subheader('Atendimentos')
col1.text(rt)

df['topografia_v2'] = df['topografia_v2'].map(topografias)
df['analise_tc_v2'] = df['analise_tc_v2'].map(tomo)

freq_topografias = df['topografia_v2'].value_counts().reset_index()
freq_topografias.columns = ['Topografia', 'Frequência']

graf_topografia = px.bar(freq_topografias, x='Frequência', y='Topografia', color='Frequência', title='Topografias - Primeira consulta', text_auto=True, orientation='h')
col3.plotly_chart(graf_topografia, use_container_width=True)

df['modalidade_tratamento_v2'] = df['modalidade_tratamento_v2'].map(modalidade_tratamento)
freq_modalidade = df['modalidade_tratamento'].value_counts().reset_index()
freq_modalidade.columns = ['Modalidade', 'Frequência']
graf_modalidade = px.pie(freq_modalidade, values='Frequência', names='Modalidade', title='Modalidade de tratamento - Primeira consulta')
col4.plotly_chart(graf_modalidade, use_container_width=True)

freq_imc_adulto = df['classificacao_imc_adulto_v2'].value_counts().reset_index()
freq_imc_adulto.columns = ['Classificação', 'Frequência']
graf_imc_adulto = px.pie(freq_imc_adulto, values='Frequência', names='Classificação', title='Classificação por IMC - Adulto')
col5.plotly_chart(graf_imc_adulto, use_container_width=True)

freq_imc_idoso = df['classificacao_imc_idosos_v2'].value_counts().reset_index()
freq_imc_idoso.columns = ['Classificação', 'Frequência']
graf_imc_idoso = px.pie(freq_imc_idoso, values='Frequência', names='Classificação', title='Classificação por IMC - Idosos')
col6.plotly_chart(graf_imc_idoso, use_container_width=True)

df['se_ganho_ponderal_v2'] = df['se_ganho_ponderal_v2'].map(ganho_ponderal)
freq_ganho_ponderal = df['se_ganho_ponderal_v2'].value_counts().reset_index()
freq_ganho_ponderal.columns = ['Classificação', 'Frequência']
graf_ganho_ponderal = px.pie(freq_ganho_ponderal, values='Frequência', names='Classificação', title='Ganho Ponderal')
col7.plotly_chart(graf_ganho_ponderal, use_container_width=True)

df['se_perda_ponderal_v2'] = df['se_perda_ponderal_v2'].map(perda_ponderal)
freq_perda_ponderal = df['se_perda_ponderal_v2'].value_counts().reset_index()
freq_perda_ponderal.columns = ['Classificação', 'Frequência']
graf_perda_ponderal = px.pie(freq_perda_ponderal, values='Frequência', names='Classificação', title='Perda Ponderal')
col8.plotly_chart(graf_perda_ponderal, use_container_width=True)

freq_cp_cm_homens = df['classificacao_cp_homens_v2'].value_counts().reset_index()
freq_cp_cm_homens.columns = ['Classificação', 'Frequência']
graf_cp_cm_homens = px.pie(freq_cp_cm_homens, values='Frequência', names='Classificação', title='Classificação Circunferência Panturrilha - Homens')
col9.plotly_chart(graf_cp_cm_homens, use_container_width=True)

freq_cp_cm_mulheres = df['classificacao_cp_mulheres_v2'].value_counts().reset_index()
freq_cp_cm_mulheres.columns = ['Classificação', 'Frequência']
graf_cp_cm_mulheres = px.pie(freq_cp_cm_mulheres, values='Frequência', names='Classificação', title='Classificação Circunferência Panturrilha - Mulheres')
col10.plotly_chart(graf_cp_cm_mulheres, use_container_width=True)

df['asg_v2'] = df['asg_v2'].map(asg)
freq_asg = df['asg_v2'].value_counts().reset_index()
freq_asg.columns = ['Classificação', 'Frequência']
freq_asg = px.pie(freq_asg, values='Frequência', names='Classificação', title='Avaliação Subjetiva Global do Estado Nutricional')
col11.plotly_chart(freq_asg, use_container_width=True)

df['modalidade_consulta_v2'] = df['modalidade_consulta_v2'].map(modalidade)
freq_modalidade = df['modalidade_consulta_v2'].value_counts().reset_index()
freq_modalidade.columns = ['Classificação', 'Frequência']
freq_modalidade = px.pie(freq_modalidade, values='Frequência', names='Classificação', title='Modalidade de Atendimento')
col12.plotly_chart(freq_modalidade, use_container_width=True)

df['via_alimentar_v2'] = df['via_alimentar_v2'].map(via_alimentar)
freq_via_alimentar = df['via_alimentar_v2'].value_counts().reset_index()
freq_via_alimentar.columns = ['Classificação', 'Frequência']
freq_via_alimentar = px.pie(freq_via_alimentar, values='Frequência', names='Classificação', title='Via Alimentar')
col13.plotly_chart(freq_via_alimentar, use_container_width=True)

df['tipo_via_alimentar_v2'] = df['tipo_via_alimentar_v2'].map(tipo_via)
freq_tipo_via = df['tipo_via_alimentar_v2'].value_counts().reset_index()
freq_tipo_via.columns = ['Classificação', 'Frequência']
freq_tipo_via = px.bar(freq_tipo_via, x='Frequência', y='Classificação', color='Frequência', title='Tipo de Via Alimentar', text_auto=True, orientation='h')
col14.plotly_chart(freq_tipo_via, use_container_width=True)

tomografia = df['analise_tc_v2'].value_counts().reset_index()
tomografia.columns = ['Classificação', 'Frequência']
graf_tomografia = px.bar(tomografia, x='Classificação', y='Frequência', color='Frequência', title='Análise por Tomografia', text_auto=True)
col14_1.plotly_chart(graf_tomografia, use_containter_width=True)

dinamometria_homens = df['dinamometria_homens_v2'].value_counts().reset_index()
dinamometria_homens.columns = ['Classificação', 'Frequência']
graf_dinamometria_homens = px.pie(dinamometria_homens, values='Frequência', names='Classificação', title='Dinamometria Homens')
col14_3.plotly_chart(graf_dinamometria_homens, use_container_width=True)

dinamometria_mulheres = df['dinamometria_mulheres_v2'].value_counts().reset_index()
dinamometria_mulheres.columns = ['Classificação', 'Frequência']
graf_dinamometria_mulheres = px.pie(dinamometria_mulheres, values='Frequência', names='Classificação', title='Dinamometria Mulheres')
col14_4.plotly_chart(graf_dinamometria_mulheres, use_container_width=True)

#Criando os Gŕafico com os Resultados filtrados por Topologia
col15.title('Dados filtrados por topografia')
topo = st.sidebar.selectbox('Selecione a Topografia', df['topografia_v2'].unique())
df_filtered = df[df['topografia_v2'] == topo]
freq_modalidade_filtered = df_filtered['modalidade_tratamento_v2'].value_counts().reset_index()
freq_modalidade_filtered.columns = ['Modalidade', 'Frequência']
graf_modalidade_filtered = px.pie(freq_modalidade_filtered, values='Frequência', names='Modalidade', title='Modalidade de Tratamento')
col17.plotly_chart(graf_modalidade_filtered, use_container_width=True)
col15_0.write("Filtrando dados por: ")
col15_1.write(topo)

freq_imc_adulto_f = df_filtered['classificacao_imc_adulto_v2'].value_counts().reset_index()
freq_imc_adulto_f.columns = ['Classificação', 'Frequência']
graf_imc_adulto_f = px.pie(freq_imc_adulto_f, values='Frequência', names='Classificação', title='Classificação IMC - Adulto')
col19.plotly_chart(graf_imc_adulto_f, use_container_width=True)

freq_imc_idosos_f = df_filtered['classificacao_imc_idosos_v2'].value_counts().reset_index()
freq_imc_idosos_f.columns = ['Classificação', 'Frequência']
graf_imc_idosos_f = px.pie(freq_imc_idosos_f, values='Frequência', names='Classificação', title='Classificação IMC - Idosos')
col20.plotly_chart(graf_imc_idosos_f, use_container_width=True)

fgp = df_filtered['se_ganho_ponderal_v2'].value_counts().reset_index()
fgp.columns = ['Classificação', 'Frequência']
graf_fgp = px.pie(fgp, values='Frequência', names='Classificação', title='Ganho Ponderal')
col21.plotly_chart(graf_fgp, use_container_width=True)

fpp = df_filtered['se_perda_ponderal_v2'].value_counts().reset_index()
fpp.columns = ['Classificação', 'Frequência']
graf_fpp = px.pie(fpp, values='Frequência', names='Classificação', title='Perda Ponderal')
col22.plotly_chart(graf_fpp, use_container_width=True)

fcpcmm = df_filtered['classificacao_cp_homens_v2'].value_counts().reset_index()
fcpcmm.columns = ['Classificação', 'Frequência']
graf_ccpcmm = px.pie(fcpcmm, values='Frequência', names='Classificação', title='Circunferência Panturrilha Homens')
col23.plotly_chart(graf_ccpcmm, use_container_width=True)

fcpcmw = df_filtered['classificacao_cp_mulheres_v2'].value_counts().reset_index()
fcpcmw.columns = ['Classificação', 'Frequência']
graf_fcpcmw = px.pie(fcpcmw, values='Frequência', names='Classificação', title='Circunferência Panturrilha Mulheres')
col24.plotly_chart(graf_fcpcmw, use_container_width=True)

fasg = df_filtered['asg_v2'].value_counts().reset_index()
fasg.columns = ['Classificação', 'Frequência']
graf_fasg = px.pie(fasg, values='Frequência', names='Classificação', title='Avaliação Subjetiva Global do Estado Nutricional')
col25.plotly_chart(graf_fasg, use_container_width=True)

fmc = df_filtered['modalidade_consulta_v2'].value_counts().reset_index()
fmc.columns = ['Classificação', 'Frequência']
graf_fmc = px.pie(fmc, values='Frequência', names='Classificação', title='Modalidade de Consulta')
col26.plotly_chart(graf_fmc, use_container_width=True)

fva = df_filtered['via_alimentar_v2'].value_counts().reset_index()
fva.columns = ['Classificação', 'Frequência']
graf_fva = px.pie(fva, values='Frequência', names='Classificação', title='Via Alimentar')
col27.plotly_chart(graf_fva, use_container_width=True)

ftva = df_filtered['tipo_via_alimentar_v2'].value_counts().reset_index()
ftva.columns = ['Classificação', 'Frequência']
graf_ftva = px.bar(ftva, x='Frequência', y='Classificação', color='Frequência', title='Tipo de Via Alimentar')
col28.plotly_chart(graf_ftva, use_container_width=True)

ftc = df_filtered['analise_tc_v2'].value_counts().reset_index()
ftc.columns = ['Classificação', 'Frequência']
graf_ftc = px.bar(ftc, x='Classificação', y='Frequência', color='Frequência', title='Análise Tomografia')
col29.plotly_chart(graf_ftc, use_container_width=True)

fdh = df_filtered['dinamometria_homens_v2'].value_counts().reset_index()
fdh.columns = ['Classificação', 'Frequência']
graf_fdh = px.pie(fdh, values='Frequência', names='Classificação', title='Dinamometria Homens')
col31.plotly_chart(graf_fdh, use_container_width=True)

fdw = df_filtered['dinamometria_mulheres_v2'].value_counts().reset_index()
fdw.columns = ['Classificação', 'Frequência']
graf_fdw = px.pie(fdh, values='Frequência', names='Classificação', title='Dinamometria Mulheres')
col32.plotly_chart(graf_fdw, use_container_width=True)
