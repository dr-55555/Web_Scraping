from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter

# Data for the table
data = [
    ["Field", "Paper 1", "Paper 2", "Paper 3", "Paper 4"],
    ["Title", "Random Forest based Fake Job Detection", 
     "Online Recruitment Fraud (ORF) Detection Using Deep Learning Approaches",
     "A machine learning approach to detecting fraudulent job types",
     "Identifying fake job posting using selective features and resampling techniques"],
    ["Parameters", "Dataset: Kaggle (17k jobs), Metrics: Accuracy, Precision, Recall, F1",
     "Dataset: 3 combined sources (50k jobs), Metrics: Accuracy, Recall, F1",
     "Dataset: Kaggle, Metrics: Accuracy, Precision, Recall",
     "Dataset: Kaggle, Metrics: Accuracy, Precision, Recall, F1"],
    ["Problem Statement", "Detect fake job postings online using ML for user safety",
     "Detect fake job posts accurately despite severe class imbalance",
     "Detect fake job posts on online platforms",
     "Identify fraudulent job postings using ML"],
    ["Algorithm", "Random Forest, Decision Tree, SVM, Naive Bayes, MLP",
     "BERT + SMOBD SMOTE, RoBERTa + G-SMOTE",
     "Gradient Boosting, Random Forest",
     "Random Forest, Gradient Boosting"],
    ["Gaps", "Imbalanced data, low recall for minority class, limited real-world testing",
     "Class imbalance, high accuracy but poor recall, no real-time/multilingual analysis",
     "Imbalanced data, no deep learning, no real-time deployment",
     "Imbalanced dataset, no advanced NLP, no deep learning"],
    ["Accuracy", "Random Forest: 92.86%",
     "BERT: 97.03%, RoBERTa: 81.35%",
     "Gradient Boosting: 97%, Random Forest: 96%",
     "Random Forest: 97%, Gradient Boosting: 96%"]
]

# PDF file path
pdf_path = "Fake_Job_Detection_Table.pdf"
pdf = SimpleDocTemplate(pdf_path, pagesize=letter)
elements = []

# Create and style table
table = Table(data, colWidths=[120, 140, 140, 140, 140])
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 8),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
])
table.setStyle(style)

elements.append(table)
pdf.build(elements)

print(f"PDF generated successfully: {pdf_path}")
