
# ✈️ SkyCast-Predictive-API 🤖

**SkyCast-Predictive-API** is a high-performance machine learning service designed to provide real-time airfare price predictions. Built with **FastAPI** and powered by an **XGBoost regression model**, this API serves as the "prediction engine" for the SkyCast ecosystem.

---

## 🚀 Key Features
* **Real-time Inference:** Fast airfare predictions based on route distance and passenger count.
* **Machine Learning Integration:** Serves a pre-trained **XGBoost** pipeline (v1.6.1 compatible).
* **RESTful Architecture:** Clean API endpoints for seamless integration.
* **Auto-Documentation:** Interactive API testing via Swagger UI (`/docs`).

---

## 🛠️ Tech Stack
* **Backend:** FastAPI
* **ML:** XGBoost, Scikit-Learn (1.6.1)
* **Server:** Uvicorn

---

## ⚙️ Installation & Setup
1. `git clone https://github.com/YOUR_USERNAME/SkyCast-Predictive-API.git`
2. `pip install -r requirements.txt`
3. `uvicorn main:app --reload`

---

## 🌐 Ecosystem
This API is the backend engine for the **[SkyCast-AI-Flight-Intelligence Dashboard](YOUR_DASHBOARD_REPO_LINK)**.

---

## 👨‍💻 Author
**Alisha** - [LinkedIn](https://www.linkedin.com/in/alisha-verma-b6a823222/)


# 3. Create Requirements File
echo "fastapi`nuvicorn`npandas`njoblib`nscikit-learn==1.6.1`nnumpy<2.0.0`nxgboost" > requirements.txt

# 4. Final Push to GitHub (REPLACE THE URL BELOW WITH YOUR ACTUAL REPO URL)
git add .; git commit -m "Initial commit: Complete FastAPI Predictive Engine"; git branch -M main; git remote add origin https://github.com/YOUR_USERNAME/SkyCast-Predictive-API.git; git push -u origin main
