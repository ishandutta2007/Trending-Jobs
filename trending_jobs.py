import matplotlib.pyplot as plt

# 5-Year historical market tracking intervals
years = ['2021-22', '2022-23', '2023-24', '2024-25', '2025-26']

# Fully populated, executable market tracking metrics across aggregators
fde_job_postings = [142, 147, 195, 643, 5330]
ai_eng_job_postings = [1150, 1520, 6080, 18240, 38120]
platform_eng_job_postings = [4200, 6100, 9400, 14800, 21500]
ai_solutions_arch = [310, 480, 2100, 7800, 16400]

# Initialize plot figure dimensions
plt.figure(figsize=(14, 9), facecolor='#f8f9fa')
ax = plt.subplot(111)

# Plot Curve 1: Forward Deployed Engineer (FDE)
plt.plot(years, fde_job_postings, marker='o', color='#0284c7', linewidth=3, markersize=8, label='Forward Deployed Engineer (FDE)', zorder=3)

# Plot Curve 2: AI Engineer
plt.plot(years, ai_eng_job_postings, marker='s', color='#b91c1c', linewidth=3, markersize=8, label='AI Engineer', zorder=3)

# Plot Curve 3: Platform Engineer
plt.plot(years, platform_eng_job_postings, marker='^', color='#059669', linewidth=3, markersize=8, label='Platform Engineer', zorder=3)

# Plot Curve 4: AI Solutions Architect
plt.plot(years, ai_solutions_arch, marker='D', color='#7c3aed', linewidth=3, markersize=8, label='AI Solutions Architect', zorder=3)

# Helper function to prevent repetitive annotation block syntax
def add_annotations(data_list, color_hex, bg_hex, text_y_offset):
    for i, count in enumerate(data_list):
        ax.annotate(
            f"{count:,}", 
            (years[i], data_list[i]), 
            textcoords="offset points", 
            xytext=(0, text_y_offset), 
            ha='center', 
            fontsize=9, 
            fontweight='bold',
            color=color_hex,
            bbox=dict(boxstyle="round,pad=0.2", fc=bg_hex, ec=color_hex, lw=1, alpha=0.85)
        )

# Apply automated annotations with strategic vertical spacing adjustments
add_annotations(fde_job_postings, '#0369a1', '#f0f9ff', -12)
add_annotations(ai_eng_job_postings, '#991b1b', '#fef2f2', 18)
add_annotations(platform_eng_job_postings, '#047857', '#ecfdf5', 12)
add_annotations(ai_solutions_arch, '#6d28d9', '#f5f3ff', 12)

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

# Set comfortable layout boundaries to accommodate extreme scaling discrepancies
plt.ylim(-3000, 43000)
plt.legend(loc='upper left', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1', fontsize=10)

# Save the generated plot in assets folder
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(script_dir, 'assets')
os.makedirs(assets_dir, exist_ok=True)
output_path = os.path.join(assets_dir, 'trending_jobs_growth.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')

plt.tight_layout()
plt.show()
