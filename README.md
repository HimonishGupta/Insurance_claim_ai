#  AI-Powered Insurance Claim Document Parser

This project is an AI-powered web app that automates the extraction of key information from scanned health insurance claim documents (PDFs). It uses **OCR**, **LLMs**, and a clean UI to streamline group health insurance claims processing.


---

##  Problem: Slow and Manual Claims Processing for Group Health Insurance

In group health insurance (used by companies to insure their employees), when employees file claims, the process is:

-  **Manual and slow** — requiring multiple document uploads, back-and-forth communication  
-  **Error-prone** — due to incorrect or missing documents  
-  **Time-consuming** for both HR teams and insurers  
-  **Frustrating for employees** — especially during medical emergencies

This delays claims settlement, creates a poor customer experience, and puts pressure on both insurance operations and the employer’s HR team.

---

##  AI Solution: Intelligent Claims Document Parser & Validator using LLMs

This project proposes an **AI-based assistant** that helps insurers and HR teams process claims quickly and accurately.

###  What the AI Tool Will Do:

-  Parse medical bills, discharge summaries, and claim forms (PDFs, images, or scanned docs) using **OCR + LLM**
-  Extract key fields:  
   `Patient name, Hospital, Admission/Discharge dates, Diagnosis, Amount claimed, etc.`
-  Check policy compliance:
   - Is the disease covered?
   - Was the hospital in-network?
   - Are room rent limits exceeded?
-  Validate completeness:
   - Have all required documents been submitted?
   - Are scanned documents readable?
   - Are amounts consistent across bills?
-  Generate a **structured claim summary** for internal teams to quickly approve or flag for review

---

##  Tools/Tech Used

| Area           | Tools/Frameworks                              |
|----------------|-----------------------------------------------|
| OCR            | Tesseract, easyOCR                            |
| NLP / LLM      | HuggingFace Transformers, LangChain           |
| Web App        | Streamlit or Gradio                           |
| Deployment     | FastAPI, Docker                               |
| Data Simulation| Synthetic fake PDFs for testing               |

---

##  Business Value

-  **Reduces claim processing time**  
-  **Improves accuracy and reduces fraud**  
-  **Improves HR & employee experience**  
-  **Easily scalable across multiple clients**

---

##  Demo

![image](https://github.com/user-attachments/assets/e31d095d-d7b8-40e7-81b7-206665abf841)


---

##  Tech Stack

| Tool           | Purpose                          |
|----------------|----------------------------------|
| Python         | Core programming language        |
| Streamlit      | Web app UI framework             |
| Tesseract OCR  | Extract text from scanned PDFs   |
| pdf2image      | Convert PDF pages to images      |
| Pillow (PIL)   | Image handling                   |

---



