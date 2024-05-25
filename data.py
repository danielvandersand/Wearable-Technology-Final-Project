import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def generate_plot(csv_file):
    data = pd.read_csv(csv_file)

    if 'Time (seconds)' not in data.columns or 'X_accel' not in data.columns:
        print(f"Missing required columns in {csv_file}. Found columns: {data.columns}")
        return None

    # Clean or fill NaN values
    if data['X_accel'].isna().any():
        print(f"NaN values found in X_accel, filling with zero.")
        data['X_accel'].fillna(0, inplace=True)

    # Plotting
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.plot(data['Time (seconds)'], data['X_accel'], label='Position X')
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Position')
    ax.legend()
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.getvalue()).decode('utf-8')


def generate_plots():
    plot1 = generate_plot('yours.csv')
    plot2 = generate_plot('yours.csv')
    return plot1, plot2
