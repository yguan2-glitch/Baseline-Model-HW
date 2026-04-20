# Baseline Model Comparison and Recommendation

## Project Overview
This project compares four classical NLP baseline pipelines for 20-topic document classification and recommends one baseline model for initial deployment based on validation metrics and business constraints.

The goal of this project is to compare model performance using accuracy and macro F1, select a model aligned with business priorities (especially avoiding weak performance on minority classes), and provide next-step experiments and deployment considerations.

## Project Structure
- baseline_analysis.py — runnable Python entry script
- requirements.txt — Python dependencies
- README.md — setup and execution instructions

## Setup Instructions
Install dependencies using:

pip install -r requirements.txt

## Run Instructions
Run the script using:

python baseline_analysis.py

This script will output the validation results, identify the best model by accuracy and macro F1, provide a final recommendation, explain the reasoning, suggest next experiments, and include a production readiness checklist.

## One-line Reproducible Run
Run the following command in a fresh terminal:

git clone https://github.com/yguan2-glitch/Baseline-Model-HW.git ; cd Baseline-Model-HW ; pip install -r requirements.txt ; python baseline_analysis.py

This command should fully reproduce the results without requiring any manual changes.

## Alternative Setup (Optional Virtual Environment)
If a clean environment is preferred:

git clone https://github.com/yguan2-glitch/Baseline-Model-HW.git
cd Baseline-Model-HW
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python baseline_analysis.py

## Reproducibility Notes
No manual configuration is required. All dependencies are listed in requirements.txt. The script runs on CPU and is lightweight. This project is designed as a reproducible mini handoff, and the reviewer should be able to run it directly using the provided commands.

## Expected Output
Running the script will print the performance comparison of all baseline pipelines, identify the best model by accuracy and macro F1, recommend a model for deployment, provide metric-based and business-based justification, suggest three follow-up experiments, and include a production readiness checklist.

## Notes for Reviewer
The selected model prioritizes macro F1 to ensure balanced performance across all classes. The pipeline remains simple enough to support weekly retraining. The design aligns with deployment constraints such as low latency and maintainability.
