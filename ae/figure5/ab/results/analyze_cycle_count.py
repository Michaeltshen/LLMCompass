import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

matmul_input_cc, matmul_output_cc = [], []
matmul_read_cc, matmul_write_cc = [], []
matmul_compute_cc = []
matmul_reduction_cc = []

xaxis_labels_m = []
xaxis_labels_nk = []

def abbreviate_value(val):
    if val == '1024':
        return '1k'
    elif val == '2048':
        return '2k'
    elif val == '4096':
        return '4k'
    elif val == '8192':
        return '8k'
    elif val == '16384':
        return '16k'
    elif val == '32768':
        return '32k'
    else:
        return val

with open('matmul_A100_sim_slurm_best_configs.csv', 'r') as best_config_file:
    best_config_reader = csv.DictReader(best_config_file)
    for best_row in best_config_reader:
        m = best_row['m']
        n = best_row['n']
        k = best_row['k']
        cycle_count = best_row['cycle_count']

        with open('matmul_cycle_count_info.csv', 'r') as matmul_file:
            matmul_reader = csv.DictReader(matmul_file)
            for matmul_row in matmul_reader:
                if (matmul_row['m'] == m and matmul_row['n'] == n and
                    matmul_row['k'] == k and matmul_row['total'] == cycle_count):
                    xaxis_labels_m.append(f"m={abbreviate_value(m)}")
                    xaxis_labels_nk.append(f"n=k={abbreviate_value(k)}")
                    matmul_input_cc.append(int(matmul_row['mk_input']) + int(matmul_row['kn_input']))
                    matmul_output_cc.append(int(matmul_row['mn_output']))
                    matmul_read_cc.append(int(matmul_row['read']))
                    matmul_write_cc.append(int(matmul_row['write']))
                    matmul_compute_cc.append(int(matmul_row['compute']) + int(matmul_row['final_compute']))
                    matmul_reduction_cc.append(int(matmul_row['reduction']))
                    break

num_bars = len(matmul_input_cc)

colors = {
    'Input CC': '#B22222',
    'Output CC': '#228B22',
    'Read CC': '#4169E1',
    'Write CC': '#FFD700',
    'Compute CC': '#4B0082',
    'Reduction CC': '#A9A9A9'
}

def plot_single_stacked_bar(ax, idx, title):
    ax.bar(0, matmul_input_cc[idx], color=colors['Input CC'], edgecolor='black', label='Input CC')
    ax.bar(0, matmul_output_cc[idx], bottom=matmul_input_cc[idx], color=colors['Output CC'], edgecolor='black', label='Output CC')
    ax.bar(0, matmul_read_cc[idx], bottom=np.array(matmul_input_cc[idx]) + np.array(matmul_output_cc[idx]), color=colors['Read CC'], edgecolor='black', label='Read CC')
    ax.bar(0, matmul_write_cc[idx], bottom=np.array(matmul_input_cc[idx]) + np.array(matmul_output_cc[idx]) + np.array(matmul_read_cc[idx]), color=colors['Write CC'], edgecolor='black', label='Write CC')
    ax.bar(0, matmul_compute_cc[idx], bottom=np.array(matmul_input_cc[idx]) + np.array(matmul_output_cc[idx]) + np.array(matmul_read_cc[idx]) + np.array(matmul_write_cc[idx]), color=colors['Compute CC'], edgecolor='black', label='Compute CC')
    ax.bar(0, matmul_reduction_cc[idx], bottom=np.array(matmul_input_cc[idx]) + np.array(matmul_output_cc[idx]) + np.array(matmul_read_cc[idx]) + np.array(matmul_write_cc[idx]) + np.array(matmul_compute_cc[idx]), color=colors['Reduction CC'], edgecolor='black', label='Reduction CC')

    ax.set_title(title, size=10)
    ax.set_xticks([])
    ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='grey', axis='y', alpha=0.7)
    
    total_height = (matmul_input_cc[idx] + matmul_output_cc[idx] + matmul_read_cc[idx] +
                    matmul_write_cc[idx] + matmul_compute_cc[idx] + matmul_reduction_cc[idx])
    y_labels = [0, 0.25 * total_height, 0.5 * total_height, 0.75 * total_height, total_height]
    ax.set_yticks(y_labels)
    ax.set_yticklabels([0] + [f"{label:.1e}" for label in y_labels[1:]])
    ax.set_ylim(0, 1.1 * total_height)

fig, axes = plt.subplots(2, 11, figsize=(17, 6))
fig.suptitle('Matrix Multiplication Cycle Count Analysis', fontsize=20)

for i in range(11):
    plot_single_stacked_bar(axes[0, i], i, f'n=k=12k {xaxis_labels_m[i]}')
    plot_single_stacked_bar(axes[1, i], i + 11, f'm=8k {xaxis_labels_nk[i + 11]}')

labels = ['Input CC', 'Output CC', 'Read CC', 'Write CC', 'Compute CC', 'Reduction CC']
colors = ['#B22222', '#228B22', '#4169E1', '#FFD700', '#4B0082', "#A9A9A9"]
custom_handles = [mpatches.Patch(color=color, label=label) for label, color in zip(labels, colors)]
fig.legend(handles=custom_handles, labels=labels, loc='upper center', bbox_to_anchor=(0.5, 0.15), ncol=6, fontsize=15)

plt.tight_layout(rect=[0, 0.175, 1, 0.95])
plt.savefig('cycle_count_analysis_individual.png')
plt.show()
