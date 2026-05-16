# 🧪 AI Medical Report Explainer

![Screenshot](https://media.discordapp.net/attachments/1397190732535697570/1397190781164326934/gif.gif?ex=68d48a10&is=68d33890&hm=f158923a6c382a0cab64dc3294042de159691aa7e84e8c94c0707a0ee3432afb&=&width=1210&height=656) 

An advanced AI-powered web application to automatically **analyze**, **explain**, and **diagnose** lab reports using OCR, Natural Language Processing (NLP), Named Entity Recognition (NER), and deep learning.

This tool allows patients and healthcare professionals to **upload lab reports (PDFs or images)** and receive:
- 🧠 Human-like explanations of medical terms and results
- 🧬 Intelligent lab value extraction (NER + Regex fallback)
- 📈 Graphical chart visualization (e.g., CBC)
- 🤖 ML-based diagnosis (using both tabular and CNN image models)
- 💬 A chatbot interface for Q&A about the uploaded report
- 📄 Downloadable AI-generated report summary (PDF)

---

## 🚀 Features

- 🔍 **OCR Extraction**: Supports PDF and image formats via Tesseract
- ✨ **Text Cleaning & Parsing**: Cleans and structures raw OCR data
- 🧬 **NER-Based Lab Value Extraction**: Uses HuggingFace-based NER models for high-accuracy recognition
- 📊 **CBC Graph Generation**: Auto-generates charts from extracted values
- 💡 **AI Explanation**: Uses `LLaMA3` or `MedLLaMA2` for rich, simplified medical insights
- 🧠 **Dual Diagnosis**:
  - From Lab Values (Rule-Based)
  - From Uploaded Image using CNN (`ConvNeXt-Tiny`) trained on PathMNIST
- 💬 **Chatbot**: Ask anything about the medical report and receive context-aware responses
- 📄 **Exportable PDF Report**

---

## 🛠️ Technologies Used

- `Python`, `Streamlit`, `PyTorch`, `Transformers`, `Tesseract OCR`
- `ConvNeXt-Tiny` for medical image-based diagnosis
- `Matplotlib` for chart generation
- HuggingFace Transformers for NER and chatbot models
- PDF processing using `PyMuPDF` and `ReportLab`

---

## 📦 Setup Instructions

### 🔗 1. Clone the Repository

git clone https://github.com/coderstale/ai-med-report-explainer.git
cd ai-med-report-explainer

🧪 2. Create and Activate a Virtual Environment

python3 -m venv vit_resnet_env
source vit_resnet_env/bin/activate  # or `.\vit_resnet_env\Scripts\activate` on Windows

📥 3. Install Dependencies

pip install -r requirements.txt

Note: This project uses Git LFS for large models. Make sure Git LFS is installed:

git lfs install
git lfs pull

📁 4. Run the App

streamlit run app/app.py


⸻

🧠 Key Challenges Faced
- OCR Accuracy: Handling noisy data and misread values using regex and NER fallback
- NER Generalisation: Not all lab reports follow standard formats—had to handle variability and fallbacks
- Pipeline Integration: Seamlessly combining OCR, AI, charts, and PDF generation in one Streamlit interface

⸻

🔭 Future Improvements
- ✅ Replace rule-based diagnosis with a trained ML model using tabular lab data
- ✅ Expand chart visualisations to include other panels (e.g., liver/kidney functions)
- 🔬 Integrate real medical LLMs (e.g., Med-PaLM, ClinicalBERT) with local inference
- 🧾 Include multiple file upload support (e.g., previous & current reports)
- 🏥 Integration with FHIR-based medical records for real-world applications
- 📊 Dashboard view for doctors to monitor patient trends

⸻

🔍 For Research

This tool provides a foundation for explainable AI in healthcare, merging vision, NLP, and deep learning. It is ideal for:
- Medical NLP research
- Healthcare analytics projects
- AI explainability use cases
- Educational demonstrations for students and practitioners

⸻

🙌 Credits
- Inspired by the need to make medical lab reports more understandable for patients
- Developed by Ayushi Rana

⸻

📜 License

MIT License
