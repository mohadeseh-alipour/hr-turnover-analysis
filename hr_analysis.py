# ============================================================
# HR Analytics - Employee Turnover Analysis
# Author: Mohadeseh Alipour
# Dataset: IBM HR Analytics (via seaborn / built-in CSV)
# Tools: pandas, matplotlib, seaborn
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import warnings
import os

warnings.filterwarnings("ignore")

# ── Style ────────────────────────────────────────────────────
sns.set_theme(style="whitegrid", palette="muted")
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ============================================================
# 1. LOAD DATA
# ============================================================
def load_data(path: str = "data/hr_data.csv") -> pd.DataFrame:
    """Load the IBM HR Analytics dataset."""
    df = pd.read_csv(path)
    print(f"✅ Dataset loaded: {df.shape[0]} rows × {df.shape[1]} columns")
    return df


# ============================================================
# 2. DATA CLEANING & PREPARATION
# ============================================================
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Basic cleaning and feature engineering."""
    # Drop columns with no variance (IBM dataset quirks)
    drop_cols = ["EmployeeCount", "Over18", "StandardHours"]
    df = df.drop(columns=[c for c in drop_cols if c in df.columns])

    # Encode Turnover as binary
    df["Turnover_Flag"] = (df["Turnover"] == "Yes").astype(int)

    # Tenure buckets
    df["TenureBucket"] = pd.cut(
        df["YearsAtCompany"],
        bins=[0, 1, 3, 6, 10, 100],
        labels=["<1 yr", "1–3 yrs", "3–6 yrs", "6–10 yrs", "10+ yrs"],
    )

    # Age groups
    df["AgeGroup"] = pd.cut(
        df["Age"],
        bins=[18, 25, 35, 45, 60],
        labels=["18–25", "26–35", "36–45", "46–60"],
    )

    print("✅ Data cleaned and features engineered")
    return df


# ============================================================
# 3. KPI SUMMARY
# ============================================================
def print_kpis(df: pd.DataFrame) -> None:
    """Print key HR KPIs to console."""
    total       = len(df)
    attrited    = df["Turnover_Flag"].sum()
    rate        = attrited / total * 100
    avg_age     = df["Age"].mean()
    avg_tenure  = df["YearsAtCompany"].mean()
    avg_salary  = df["MonthlyIncome"].mean()

    print("\n" + "=" * 45)
    print("         HR ANALYTICS — KPI SUMMARY")
    print("=" * 45)
    print(f"  Total Employees       : {total:,}")
    print(f"  Employees Left        : {attrited:,}")
    print(f"  Overall Turnover Rate: {rate:.1f}%")
    print(f"  Average Age           : {avg_age:.1f} years")
    print(f"  Average Tenure        : {avg_tenure:.1f} years")
    print(f"  Average Monthly Income: ${avg_salary:,.0f}")
    print("=" * 45 + "\n")


# ============================================================
# 4. VISUALISATIONS
# ============================================================

def plot_turnover_overview(df: pd.DataFrame) -> None:
    """Pie chart — overall turnover split."""
    counts = df["Turnover"].value_counts()
    colors = ["#4C72B0", "#DD8452"]

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(
        counts,
        labels=counts.index,
        autopct="%1.1f%%",
        startangle=90,
        colors=colors,
        wedgeprops={"edgecolor": "white", "linewidth": 2},
    )
    ax.set_title("Overall Turnover Rate", fontsize=15, fontweight="bold", pad=15)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/01_turnover_overview.png", dpi=150)
    plt.close()
    print("📊 Saved: 01_turnover_overview.png")


def plot_turnover_by_department(df: pd.DataFrame) -> None:
    """Bar chart — turnover rate by department."""
    dept = (
        df.groupby("Department")["Turnover_Flag"]
        .mean()
        .mul(100)
        .reset_index()
        .rename(columns={"Turnover_Flag": "TurnoverRate"})
        .sort_values("TurnoverRate", ascending=False)
    )

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=dept, x="Department", y="TurnoverRate", palette="Blues_d", ax=ax)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax.set_title("Turnover Rate by Department", fontsize=14, fontweight="bold")
    ax.set_xlabel("")
    ax.set_ylabel("Turnover Rate (%)")
    for bar in ax.patches:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.5,
            f"{bar.get_height():.1f}%",
            ha="center", va="bottom", fontsize=11
        )
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/02_turnover_by_department.png", dpi=150)
    plt.close()
    print("📊 Saved: 02_turnover_by_department.png")


def plot_turnover_by_tenure(df: pd.DataFrame) -> None:
    """Bar chart — turnover rate by tenure bucket."""
    tenure = (
        df.groupby("TenureBucket", observed=True)["Turnover_Flag"]
        .mean()
        .mul(100)
        .reset_index()
        .rename(columns={"Turnover_Flag": "TurnoverRate"})
    )

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=tenure, x="TenureBucket", y="TurnoverRate", palette="Oranges_d", ax=ax)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax.set_title("Turnover Rate by Tenure", fontsize=14, fontweight="bold")
    ax.set_xlabel("Years at Company")
    ax.set_ylabel("Turnover Rate (%)")
    for bar in ax.patches:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.5,
            f"{bar.get_height():.1f}%",
            ha="center", va="bottom", fontsize=11
        )
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/03_turnover_by_tenure.png", dpi=150)
    plt.close()
    print("📊 Saved: 03_turnover_by_tenure.png")


def plot_salary_vs_turnover(df: pd.DataFrame) -> None:
    """Box plot — monthly income distribution by turnover."""
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(
        data=df, x="Turnover", y="MonthlyIncome",
        palette={"No": "#4C72B0", "Yes": "#DD8452"}, ax=ax
    )
    ax.set_title("Monthly Income vs Turnover", fontsize=14, fontweight="bold")
    ax.set_xlabel("Turnover")
    ax.set_ylabel("Monthly Income ($)")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/04_salary_vs_turnover.png", dpi=150)
    plt.close()
    print("📊 Saved: 04_salary_vs_turnover.png")


def plot_age_distribution(df: pd.DataFrame) -> None:
    """Histogram — age distribution by turnover."""
    fig, ax = plt.subplots(figsize=(9, 5))
    for label, color in zip(["No", "Yes"], ["#4C72B0", "#DD8452"]):
        subset = df[df["Turnover"] == label]["Age"]
        ax.hist(subset, bins=20, alpha=0.6, label=f"Turnover: {label}", color=color, edgecolor="white")
    ax.set_title("Age Distribution by Turnover", fontsize=14, fontweight="bold")
    ax.set_xlabel("Age")
    ax.set_ylabel("Number of Employees")
    ax.legend()
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/05_age_distribution.png", dpi=150)
    plt.close()
    print("📊 Saved: 05_age_distribution.png")


def plot_satisfaction_heatmap(df: pd.DataFrame) -> None:
    """Heatmap — turnover rate by job role and job satisfaction."""
    pivot = df.pivot_table(
        index="JobRole",
        columns="JobSatisfaction",
        values="Turnover_Flag",
        aggfunc="mean"
    ).mul(100).round(1)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(
        pivot, annot=True, fmt=".1f", cmap="YlOrRd",
        linewidths=0.5, ax=ax, cbar_kws={"label": "Turnover Rate (%)"}
    )
    ax.set_title("Turnover Rate (%) by Job Role & Satisfaction Level", fontsize=13, fontweight="bold")
    ax.set_xlabel("Job Satisfaction (1=Low → 4=High)")
    ax.set_ylabel("")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/06_satisfaction_heatmap.png", dpi=150)
    plt.close()
    print("📊 Saved: 06_satisfaction_heatmap.png")


def plot_overtime_turnover(df: pd.DataFrame) -> None:
    """Grouped bar — turnover rate by overtime."""
    ot = (
        df.groupby("OverTime")["Turnover_Flag"]
        .mean()
        .mul(100)
        .reset_index()
        .rename(columns={"Turnover_Flag": "TurnoverRate"})
    )

    fig, ax = plt.subplots(figsize=(6, 5))
    sns.barplot(data=ot, x="OverTime", y="TurnoverRate", palette=["#4C72B0", "#DD8452"], ax=ax)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax.set_title("Turnover Rate by Overtime", fontsize=14, fontweight="bold")
    ax.set_xlabel("Overtime")
    ax.set_ylabel("Turnover Rate (%)")
    for bar in ax.patches:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.5,
            f"{bar.get_height():.1f}%",
            ha="center", va="bottom", fontsize=12
        )
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/07_overtime_turnover.png", dpi=150)
    plt.close()
    print("📊 Saved: 07_overtime_turnover.png")


# ============================================================
# 5. MAIN
# ============================================================
def main():
    df = load_data()
    df = clean_data(df)
    print_kpis(df)

    plot_turnover_overview(df)
    plot_turnover_by_department(df)
    plot_turnover_by_tenure(df)
    plot_salary_vs_turnover(df)
    plot_age_distribution(df)
    plot_satisfaction_heatmap(df)
    plot_overtime_turnover(df)

    print("\n✅ All charts saved to /outputs — ready for GitHub!")


if __name__ == "__main__":
    main()
