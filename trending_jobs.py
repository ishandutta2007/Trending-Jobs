import matplotlib.pyplot as plt

# 5-Year historical market tracking intervals
years = ['2021-22', '2022-23', '2023-24', '2024-25', '2025-26']

# Sourced absolute active tracking metrics across aggregators (Indeed, LinkedIn, Paraform)
absolute_job_postings = [425, 440, 583, 2332, 22485]

# Initialize plot figure dimensions
plt.figure(figsize=(11, 6.5), facecolor='#f8f9fa')
ax = plt.subplot(111)

# Generate line graph with clearly defined circular node markers
plt.plot(
    years, 
    absolute_job_postings, 
    marker='o', 
    color='#0284c7', 
    linewidth=3, 
    markersize=9, 
    label='Active FDE Postings',
    zorder=3
)

# Explicitly annotate every single coordinate data point with formatted absolute strings
for i, count in enumerate(absolute_job_postings):
    ax.annotate(
        f"{count:,} Roles", 
        (years[i], absolute_job_postings[i]), 
        textcoords="offset points", 
        xytext=(0, 14), 
        ha='center', 
        fontsize=10, 
        fontweight='bold',
        color='#0f172a',
        bbox=dict(boxstyle="round,pad=0.3", fc="#ffffff", ec="#cbd5e1", lw=1, alpha=0.9)
    )

# Chart layout titles and structured axis labeling
plt.title('Forward Deployed Engineer (FDE) Absolute Job Growth (2021–2026)', fontsize=14, fontweight='bold', pad=22, color='#1e293b')
plt.xlabel('Market Tracking Period', fontsize=11, fontweight='bold', labelpad=14, color='#334155')
plt.ylabel('Absolute Number of Unique Open Positions', fontsize=11, fontweight='bold', labelpad=14, color='#334155')

# Style borders and soft horizontal reference gridlines 
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#cbd5e1')
ax.spines['bottom'].set_color('#cbd5e1')
plt.grid(axis='y', linestyle='--', alpha=0.5, zorder=0)

# Set comfortable vertical layout boundaries to prevent clipping annotations
plt.ylim(-1000, 25500)

# Render and tighten layout configuration
plt.tight_layout()
plt.show()
