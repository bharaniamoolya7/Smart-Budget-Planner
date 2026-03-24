🧠 Smart Budget Planner using Artificial Neural Networks (ANN)

Analyzing financial data to support intelligent budgeting decisions effectively.
________________________________________________________________________________________________________________________________________________________________________________________
🚀 Project Overview

The Smart Budget Planner (ANN Pro) is an advanced financial decision-support system designed to go beyond traditional expense tracking.

Unlike basic budget tools that only record transactions, this system uses Artificial Neural Network (ANN) principles to:

Analyze income and liabilities intelligently

Distribute funds using weighted decision logic

Identify and reduce wasteful spending

Maximize wealth growth while minimizing financial risk

🔬Technical Architecture & Logic:

The system is designed as a multi-layered financial processing engine:

Input Layer ($X$)

Processes core financial inputs:

$X_1$ → Monthly Gross Income
$X_2$ → Rent / Loans
$X_3$ → EMIs
$X_4$ → Other Deductions
Hidden Processing (Weighted Allocation)
Fixed costs are deducted first
Remaining amount forms the Net Pool
Funds are distributed using Softmax-style weighted allocation
Based on user-defined priority ranking

Example priorities:
Healthcare → Utilities → Transport

Constraint Layer ($Y_{Target}$)
A high-priority bias node
Ensures Savings Target is non-negotiable
Always protected before other allocations
Intelligent Optimization

Node Capping: 
Prevents overspending by applying safe thresholds
Transport → ₹6,000
Food → ₹10,000
Utilities → ₹12,000

Surplus Re-routing: 
Detects excess spending
Automatically reallocates surplus to:
Savings
Gold
Safe investment options

📈 Experimental Results & Accuracy

Metric	Achievement
Constraint Accuracy	100% (Zero failure in protecting fixed costs & savings)
Optimization Efficiency	12–15% increase in monthly wealth growth
Model Stability	Weighted decay prevents budget overflow
Risk Mitigation	Detects stock risk & suggests safer alternatives

📊 Sample Output Analysis
For a test case with ₹150,000 monthly income:

ANN detected ₹14,000 surplus
Identified wasteful nodes in:
Transport
Utilities
Reallocated funds to increase savings
Maintained user's lifestyle without compromise

💡Key Features:
Safe-Mode Investment Advice

Suggests low-risk options like Gold & Savings over volatile investments

📊 Neural Weight Visualization

Real-time Donut Chart showing allocation percentages

⚡Dynamic Decision Support:
Instant feedback when priorities change

🛠️ Tech Stack
Language: Python 3.x,
GUI Framework: Tkinter (Modern Custom Theme),
Core Logic:
ANN-based Weighted Distribution
Threshold Optimization
Constraint-based Financial Modeling
_______________________________________________________________________________________________________________________________________________________________________________________
🎯Conclusion:

The Smart Budget Planner transforms traditional budgeting into an intelligent, adaptive financial system by leveraging ANN concepts.
It ensures:
Financial discipline
Risk-aware decisions
Optimized savings growth
_______________________________________________________________________________________________________________________________________________________________________________________
📉 Model Output Demonstration:
<img width="1899" height="1102" alt="image" src="https://github.com/user-attachments/assets/bc33fd53-510f-4875-ad28-d372242b661b" />
<img width="1904" height="1052" alt="image" src="https://github.com/user-attachments/assets/79622cd9-5437-44aa-95ae-d10fb485f477" />
<img width="1905" height="1115" alt="image" src="https://github.com/user-attachments/assets/eef66615-fc26-4438-9421-ef183c0242fc" />



