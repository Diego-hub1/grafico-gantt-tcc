import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

atividades = [
    "Definir Tema e Delimitar Escopo",
    "Levantamento de Referências",
    "Desenvolvimento do Capítulo 1",
    "Desenvolvimento do Capítulo 2",
    "Elaboração de Conclusões",
    "Revisão e Ajustes Finais",
    "Preparação da Defesa",
    "Defesa do TCC"
]

inicio = [
    "2025-05-15", "2025-05-19", "2025-05-24", "2025-05-29", "2025-06-03", "2025-06-07", "2025-06-11", "2025-06-14"
]
fim = [
    "2025-05-18", "2025-05-23", "2025-05-28", "2025-06-02", "2025-06-06", "2025-06-10", "2025-06-13", "2025-06-14"
]

inicio = pd.to_datetime(inicio)
fim = pd.to_datetime(fim)

df = pd.DataFrame({'Atividade': atividades, 'Início': inicio, 'Fim': fim})
df['Duração'] = (df['Fim'] - df['Início']).dt.days

fig, ax = plt.subplots(figsize=(10, 6))
for i, row in df.iterrows():
    ax.barh(row['Atividade'], row['Duração'], left=row['Início'], height=0.6)

ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
plt.xticks(rotation=45)
plt.title('Cronograma de Atividades - TCC', fontsize=16)
plt.xlabel('Datas', fontsize=12)
plt.ylabel('Atividades', fontsize=12)
plt.tight_layout()
plt.show()
