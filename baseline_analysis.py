# baseline_analysis.py

results = [
    {"pipeline": "Count + MultinomialNB", "accuracy": 0.6544, "macro_f1": 0.6259},
    {"pipeline": "Count + LogisticRegression", "accuracy": 0.6228, "macro_f1": 0.6138},
    {"pipeline": "TFIDF + MultinomialNB", "accuracy": 0.6913, "macro_f1": 0.6655},
    {"pipeline": "TFIDF + LinearSVC", "accuracy": 0.6824, "macro_f1": 0.6713},
]

best_accuracy = max(results, key=lambda x: x["accuracy"])
best_macro_f1 = max(results, key=lambda x: x["macro_f1"])

chosen_pipeline = "TFIDF + LinearSVC"

experiments = [
    {
        "change": "Change ngram_range from (1,1) to (1,2)",
        "expected_impact": "May improve topic classification by capturing short phrases instead of only single words.",
        "metric": "Macro F1"
    },
    {
        "change": "Tune LinearSVC C from default to 0.1, 1, 5, and 10",
        "expected_impact": "May improve class separation and help balance performance across weaker classes.",
        "metric": "Macro F1 and accuracy"
    },
    {
        "change": "Set min_df from default to 2 or 3 in TF-IDF",
        "expected_impact": "May reduce noise from very rare words and improve generalization.",
        "metric": "Validation macro F1"
    }
]

checklist = [
    "Confirm the selected model meets the minimum macro F1 target before release.",
    "Track production accuracy, macro F1, and per-class performance after deployment.",
    "Retrain the model weekly to address expected data drift.",
    "Prepare a rollback plan so the previous stable model can be restored quickly.",
    "Run error analysis on minority and weak classes before go-live."
]

print("=" * 60)
print("BASELINE MODEL COMPARISON AND RECOMMENDATION")
print("=" * 60)

print("\nValidation Results:")
for r in results:
    print(f"- {r['pipeline']}: accuracy={r['accuracy']:.4f}, macro_f1={r['macro_f1']:.4f}")

print("\nBest by Accuracy:")
print(f"- {best_accuracy['pipeline']} ({best_accuracy['accuracy']:.4f})")

print("\nBest by Macro F1:")
print(f"- {best_macro_f1['pipeline']} ({best_macro_f1['macro_f1']:.4f})")

print("\nRecommended Pipeline to Ship First:")
print(f"- {chosen_pipeline}")

print("\nRecommendation Summary:")
print("- I would ship TFIDF + LinearSVC first because it has the highest macro F1, which matters most when the business wants to avoid weak performance on minority or weaker classes.")
print("- It is also still a simple classical model, so weekly retraining is realistic under the deployment constraint.")
print("- The main post-deployment risk to monitor is class-level performance drift.")

print("\nNext Experiments:")
for i, exp in enumerate(experiments, start=1):
    print(f"{i}. Exact Change: {exp['change']}")
    print(f"   Expected Impact: {exp['expected_impact']}")
    print(f"   Success Metric: {exp['metric']}")

print("\nProduction Readiness Checklist:")
for item in checklist:
    print(f"- {item}")

print("\nDone.")