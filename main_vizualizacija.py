import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Nostalgija (Crveno), Kritika (Plavo), Neutralno (Sivo)
custom_palette = {
    "Nostalgija": "#d62728", 
    "Kritika": "#1f77b4",    
    "Neutralno": "#999999"   
}

df = pd.read_json("data/result/articles/results_labeled_articles_title.jsonl", lines=True)

# mapiranje labela
label_map = {0: "Nostalgija", 1: "Kritika", 2: "Neutralno"}
df['label_name'] = df['pred_label'].map(label_map)


# --- UKUPNA DISTRIBUCIJA ---
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

ax = sns.countplot(data=df, x='label_name', hue='label_name', palette=custom_palette, legend=False)

total = len(df)
for p in ax.patches:
    height = p.get_height()
    if height > 0:
        percentage = f'{100 * height / total:.1f}%'
        label_text = f'{int(height)}\n({percentage})'
        
        ax.annotate(label_text, 
                    (p.get_x() + p.get_width() / 2., height), 
                    ha='center', va='center', 
                    xytext=(0, 15),
                    textcoords='offset points', 
                    fontsize=11, 
                    fontweight='bold')

plt.ylim(0, df['label_name'].value_counts().max() * 1.15)

plt.title("Ukupna distribucija osjećaja u člancima", fontsize=14)
plt.xlabel("Osjećaj")
plt.ylabel("Broj članaka")
plt.savefig("data/graphs/articles/ukupna_distribucija.png")
print("\nSpremljeno: ukupna_distribucija.png s brojkama i postocima")

# --- PIE CHART UKUPNE DISTRIBUCIJE ---
plt.figure(figsize=(10, 8))

counts = df['label_name'].value_counts()
labels = counts.index
values = counts.values

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.1f}%\n({v:d})'.format(p=pct, v=val)
    return my_autopct

#pie charta
plt.pie(values, 
        labels=labels, 
        autopct=make_autopct(values), 
        startangle=140, 
        colors=[custom_palette[label] for label in labels],
        pctdistance=0.85, 
        explode=[0.05] * len(labels)) 

plt.title("Udio osjećaja u člancima", fontsize=15, pad=20)
plt.axis('equal')
plt.tight_layout()

plt.savefig("data/graphs/articles/pie_distribucija.png")
print("Spremljeno: pie_distribucija.png")

# --- DISTRIBUCIJA PO PORTALIMA ---
plt.figure(figsize=(12, 7))
portal_dist = pd.crosstab(df['source'], df['label_name'], normalize='index') * 100
ax = portal_dist.plot(kind='bar', stacked=True, color=[custom_palette[label] for label in portal_dist.columns], figsize=(12, 7))

for n, portal in enumerate(portal_dist.index):
    cum_height = 0
    for sentiment in portal_dist.columns:
        val = portal_dist.loc[portal, sentiment]
        if val > 5:
            ax.text(n, cum_height + (val/2), f'{val:.1f}%', 
                    ha='center', va='center', color='white', fontweight='bold')
        cum_height += val

plt.title("Usporedba osjećaja u člancima po portalima (%)")
plt.legend(title="Osjećaj", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.ylabel("Postotak članaka (%)")
plt.xlabel("Portal")
plt.tight_layout()
plt.savefig("data/graphs/articles/distribucija_portali.png")
print("Spremljeno: distribucija_portali.png")


# --- VREMENSKA PROMJENA ---
df['publish_date'] = pd.to_datetime(df['publish_date'], errors='coerce')
df['month_year'] = df['publish_date'].dt.to_period('M')

plt.figure(figsize=(10, 6))
time_dist = df.groupby(['month_year', 'label_name']).size().unstack(fill_value=0)
time_dist.plot(marker='o', figsize=(10,6), color=[custom_palette[label] for label in time_dist.columns])
plt.title("Trend osjećaja kroz vrijeme")
plt.ylabel("Broj članaka")
plt.xlabel("Vrijeme (Mjesec-Godina)")
plt.legend(title="Osjećaj")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("data/graphs/articles/vremenski_trend.png")
print("Spremljeno: vremenski_trend.png")
