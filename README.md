# 👥 HR Analytics — Employee Turnover Analysis

> **A data analytics project exploring the drivers of employee turnover using Python.**  
> Built as part of my data analytics portfolio.

---

## 📌 Project Overview

Employee turnover is one of the most costly challenges for any organization. This project analyzes the **IBM HR Analytics dataset** to identify the key factors driving turnover and provide actionable business insights.

**Questions this project answers:**
- What is the overall turnover rate?
- Which departments and job roles have the highest turnover?
- Does salary impact the likelihood of leaving?
- How does tenure affect turnover?
- Does working overtime increase the risk of leaving?
- Which employee segments are most at risk?

---

## 📊 Key Findings

| KPI | Value |
|-----|-------|
| Overall Turnover Rate | ~16.1% |
| Highest-risk Department | Sales |
| Highest-risk Tenure | < 1 year |
| Overtime employees turnover | ~30% vs ~10% (no overtime) |
| Lower income → Higher turnover | Confirmed via boxplot |

---

## 📁 Project Structure

```
hr_analytics/
│
├── data/
│   └── hr_data.csv             # IBM HR Analytics dataset
│
├── outputs/
│   ├── 01_turnover_overview.png
│   ├── 02_turnover_by_department.png
│   ├── 03_turnover_by_tenure.png
│   ├── 04_salary_vs_turnover.png
│   ├── 05_age_distribution.png
│   ├── 06_satisfaction_heatmap.png
│   └── 07_overtime_turnover.png
│
├── hr_analysis.py              # Main analysis script
├── download_data.py            # Dataset downloader
├── requirements.txt
└── README.md
```

---

## 🛠️ Tools & Libraries

- **Python 3.9+**
- **pandas** — data manipulation and feature engineering
- **matplotlib** — chart creation
- **seaborn** — statistical visualizations

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/hr-analytics-turnover.git
cd hr-analytics-turnover
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Download the dataset**
```bash
python download_data.py
```

**4. Run the analysis**
```bash
python hr_analysis.py
```

Charts will be saved automatically in the `/outputs` folder.

---

## 📈 Visualizations

| Chart | Insight |
|-------|---------|
| Turnover Overview | 16.1% of employees left |
| By Department | Sales has the highest turnover rate |
| By Tenure | Employees with < 1 year are most at risk |
| Salary vs Turnover | Employees who left had lower average income |
| Age Distribution | Younger employees (18–25) show higher turnover |
| Satisfaction Heatmap | Low satisfaction + specific roles = high risk |
| Overtime vs Turnover | Overtime employees are 3× more likely to leave |

---

## 💡 Business Recommendations

1. **Focus retention efforts on new hires** — the first year is critical
2. **Review overtime policies** — overworked employees leave at 3× the rate
3. **Audit compensation in Sales** — highest turnover department
4. **Monitor low-satisfaction roles** — early intervention reduces turnover costs

---

## 📂 Dataset

**IBM HR Analytics Employee Turnover & Performance**  
Originally published on Kaggle. Contains 1,470 employee records with 35 features including demographics, job role, satisfaction scores, salary, and turnover status.
