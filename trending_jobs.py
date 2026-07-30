import matplotlib.pyplot as plt

# 5-Year historical market tracking intervals
years = ['2021-22', '2022-23', '2023-24', '2024-25', '2025-26']

# Sourced absolute active tracking metrics for both tech families
fde_job_postings = [120, 160, 643, 5330, 21390]
ai_eng_job_postings = [1420, 3100, 7440, 15600, 38100]

# Initialize plot figure dimensions
plt.figure(figsize=(12, 7.5), facecolor='#f8f9fa')
ax = plt.subplot(111)

# Plot Curve 1: Forward Deployed Engineer (FDE)
plt.plot(
    years, 
    fde_job_postings, 
    marker='o', 
    color='#0284c7', 
    linewidth=3, 
    markersize=8, 
    label='Forward Deployed Engineer (FDE)',
    zorder=3
)

# Plot Curve 2: AI Engineer
plt.plot(
    years, 
    ai_eng_job_postings, 
    marker='s', 
    color='#b91c1c', 
    linewidth=3, 
    markersize=8, 
    label='AI Engineer',
    zorder=3
)

# Explicitly annotate Forward Deployed Engineer (FDE) data points
for i, count in enumerate(fde_job_postings):
    ax.annotate(
        f"{count:,}", 
        (years[i], fde_job_postings[i]), 
        textcoords="offset points", 
        xytext=(-10, -18) if i == 3 else (0, 12), 
        ha='center', 
        fontsize=9, 
        fontweight='bold',
        color='#0369a1',
        bbox=dict(boxstyle="round,pad=0.2", fc="#f0f9ff", ec="#0284c7", lw=1, alpha=0.85)
    )

# Explicitly annotate AI Engineer data points 
for i, count in enumerate(ai_eng_job_postings):
    ax.annotate(
        f"{count:,}", 
        (years[i], ai_eng_job_postings[i]), 
        textcoords="offset points", 
        xytext=(0, 12), 
        ha='center', 
        fontsize=9, 
        fontweight='bold',
        color='#991b1b',
        bbox=dict(boxstyle="round,pad=0.2", fc="#fef2f2", ec="#b91c1c", lw=1, alpha=0.85)
    )

# Chart layout titles and structured axis labeling
plt.title('Absolute Job Posting Market Growth Comparison (2021–2026)', fontsize=14, fontweight='bold', pad=22, color='#1e293b')
plt.xlabel('Market Tracking Period', fontsize=11, fontweight='bold', labelpad=14, color='#334155')
plt.ylabel('Absolute Number of Unique Open Positions', fontsize=11, fontweight='bold', labelpad=14, color='#334155')

# Style borders and soft horizontal reference gridlines 
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#cbd5e1')
ax.spines['bottom'].set_color('#cbd5e1')
plt.grid(axis='y', linestyle='--', alpha=0.5, zorder=0)

# Set comfortable vertical layout boundaries to prevent clipping annotations
plt.ylim(-2000, 43000)

# Add clear chart legend positioning
plt.legend(loc='upper left', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1', fontsize=10)

# Render and tighten layout configuration
plt.tight_layout()
plt.show()
