# 💧 Water Quality Analysis & Prediction

## 1. Giới thiệu
Dự án này thực hiện phân tích, khai phá và dự đoán chất lượng nguồn nước (Water Potability) bằng các kỹ thuật Data Mining và Machine Learning. 
Bộ dữ liệu được sử dụng là Water Quality Dataset từ Kaggle, giải quyết bài toán cấp thiết trong việc giám sát và đánh giá độ an toàn của nước sinh hoạt.

Dự án tiếp cận bài toán theo 2 hướng chính:
* **Unsupervised Learning (Khai phá tri thức):** Phân cụm nguồn nước và tìm kiếm các quy luật kết hợp (Association Rules) giữa các chỉ số hóa học.
* **Predictive Modeling (Học có giám sát & Bán giám sát):** Xây dựng hệ thống tự động cảnh báo nguồn nước ô nhiễm và mô phỏng kịch bản tối ưu chi phí xét nghiệm khi thiếu dữ liệu gán nhãn.

## 2. Dataset Overview
* **Nguồn:** Kaggle Water Quality Dataset
* **Số bản ghi:** 3276
* **Số thuộc tính:** 9 đặc trưng (Features) + 1 Biến mục tiêu (Target)
* **Biến mục tiêu:** `Potability` (0 = Không an toàn/Nước bẩn, 1 = An toàn/Nước uống được)

**Các chỉ số hóa lý chính:**
* `ph`: Độ pH của nước
* `Hardness`: Độ cứng (Capacity of water to precipitate soap)
* `Solids`: Tổng chất rắn hòa tan (TDS)
* `Chloramines`: Lượng Chloramines
* `Sulfate`: Nồng độ Ion Sulfate
* `Conductivity`, `Organic_carbon`, `Trihalomethanes`, `Turbidity`

*Lưu ý:* Dataset gặp tình trạng mất cân bằng lớp (Imbalanced Data) khi lượng mẫu nước Không an toàn chiếm đa số, đồng thời có nhiều dữ liệu bị khuyết (Missing values) ở các cột `ph`, `Sulfate` và `Trihalomethanes`.

## 3. Pipeline Dự án
Quy trình thực hiện tuân thủ chặt chẽ kiến trúc pipeline phân tích dữ liệu:

    Raw Data
       ↓
    Data Preprocessing (Imputation & Scaling via Pipeline)
       ↓
    Association Rule Mining (Apriori)
       ↓
    Water Source Clustering (K-Means)
       ↓
    Machine Learning Models (Random Forest, Gradient Boosting, Logistic Regression)
       ↓
    Semi-supervised Learning (Label Spreading)
       ↓
    Evaluation, Error Analysis & Actionable Insights

## 4. Công nghệ sử dụng
| Nhóm | Công nghệ / Thư viện |
| :--- | :--- |
| **Ngôn ngữ** | Python |
| **Xử lý dữ liệu** | Pandas, NumPy (< 2.0.0) |
| **Trực quan hóa** | Matplotlib, Seaborn |
| **Machine Learning** | Scikit-learn (Random Forest, Gradient Boosting, Label Spreading) |
| **Rule Mining** | mlxtend (Apriori) |
| **Clustering** | KMeans |
| **Tự động hóa** | Papermill |

## 5. Cấu trúc thư mục
Dự án được tổ chức module hóa, tách biệt rạch ròi giữa code xử lý, cấu hình và báo cáo để đảm bảo khả năng tái lập (reproducible).

    DATA_MINING_PROJECT/
    │
    ├── data/
    │   ├── raw/               # Chứa file gốc water_potability.csv
    │   └── processed/         # Chứa file sau khi làm sạch
    │
    ├── notebooks/
    │   ├── 01_eda.ipynb
    │   ├── 02_preprocess.ipynb
    │   ├── 03_mining.ipynb
    │   ├── 04_model.ipynb
    │   ├── 04b_semi.ipynb
    │   └── 05_evaluation.ipynb
    │
    ├── src/                   # Mã nguồn Python (Modules)
    │   ├── __init__.py
    │   ├── preprocess.py      # Script load và clean data
    │   ├── train.py           # Thiết lập ML Pipeline
    │   └── evaluate.py        # Các hàm tính toán metric
    │
    ├── scripts/
    │   └── run_papermill.py   # Script tự động chạy toàn bộ notebook
    │
    ├── outputs/               # Chứa kết quả notebook sau khi run_papermill thực thi
    │
    ├── requirements.txt       # Danh sách thư viện và phiên bản
    └── README.md

## 6. Cài đặt & Khởi chạy (Reproduction)

**Bước 1: Clone repository**
```
    git clone [https://github.com/VietHung04/WaterQuality.git](https://github.com/VietHung04/WaterQuality.git)
    
    cd WaterQuality
```
**Bước 2: Cài đặt môi trường và thư viện**
```
    Cài đặt thư viện theo requirements (đã ghim numpy < 2.0 để tránh xung đột)

    pip install -r requirements.txt
```
**Bước 3: Chạy Pipeline tự động**
Hệ thống sử dụng Papermill để thực thi tuần tự các notebook và lưu báo cáo vào thư mục outputs/.
```
    python scripts/run_papermill.py
```
## 7. Các thành phần chính

### 7.1. Tiền xử lý (Preprocessing)
Sử dụng `sklearn.pipeline.Pipeline` để đóng gói bước điền khuyết (`SimpleImputer` bằng Mean) và chuẩn hóa (`StandardScaler`). Việc tích hợp này giúp ngăn chặn hoàn toàn rủi ro Rò rỉ dữ liệu (Data Leakage) giữa tập Train và Test.

### 7.2. Khai phá luật kết hợp (Association Rules)
Biến đổi các chỉ số liên tục thành dạng rời rạc (bins) và sử dụng thuật toán **Apriori**. 
* *Insight nổi bật:* Tìm ra các mẫu cảnh báo kép khi sự thay đổi bất thường của độ pH thường kéo theo sự gia tăng của Độ đục (Turbidity) và nồng độ Sulfate.

### 7.3. Phân cụm (Clustering)
Sử dụng **K-Means** với phương pháp Elbow để tìm ra số cụm tự nhiên của nguồn nước (K=3 hoặc 4).
* *Insight nổi bật:* Phân tích hồ sơ cụm (Profiling) giúp nhận diện "Cụm rủi ro cao" chứa các mẫu có tổng chất rắn hòa tan (Solids) và độ dẫn điện (Conductivity) vượt xa mức an toàn.

### 7.4. Mô hình dự đoán (Supervised Learning)
Xử lý mất cân bằng nhãn bằng `class_weight='balanced'`. **Random Forest** là mô hình đạt hiệu suất tốt nhất (vượt trội hoàn toàn so với Logistic Regression) nhờ khả năng phân chia ranh giới không gian dữ liệu phi tuyến tính phức tạp.

### 7.5. Học Bán giám sát (Semi-supervised Learning)
Giải quyết bài toán "Thiếu nhãn" trong thực tế (khi chỉ có 10-30% dữ liệu được gán nhãn do chi phí xét nghiệm cao).
* Sử dụng thuật toán **Label Spreading**.
* *Kết quả:* Đồ thị Learning Curve chứng minh mô hình Bán giám sát vượt trội hơn mô hình Supervised truyền thống ở vùng dữ liệu thiếu nhãn (< 30%), thể hiện khả năng lan truyền nhãn (pseudo-labeling) rất tốt.

## 8. Actionable Insights (Đề xuất hành động)
Phân tích lỗi (Error Analysis) từ Confusion Matrix cung cấp các insight cốt lõi cho việc vận hành trạm quan trắc:
1. **Thiết lập cảm biến ưu tiên:** Tập trung nguồn lực theo dõi `pH` và `Sulfate` theo thời gian thực, đây là 2 đặc trưng quan trọng nhất quyết định chất lượng nước.
2. **Tối ưu ngưỡng quyết định (Threshold Tuning):** Chủ động tăng ngưỡng dự đoán (predict_proba) của mô hình lên > 0.65 để triệt tiêu các ca "False Positives" (Cấp phép nhầm cho nước bẩn), đặt sức khỏe cộng đồng lên hàng đầu.
3. **Tiết kiệm ngân sách xét nghiệm:** Chỉ cần xét nghiệm dán nhãn thủ công cho khoảng 30% mẫu nước và dùng thuật toán Label Spreading để tự động lan truyền nhãn cho phần còn lại, giúp tiết kiệm đến 70% ngân sách phân tích.
4. **Quy trình "Human-in-the-loop":** Các mẫu bị AI phán "Không an toàn" với xác suất thấp (biên 0.4 - 0.5) cần được chuyển cho nhân viên lab xét nghiệm lại để tránh xả bỏ lãng phí nguồn nước sạch (giảm False Negatives).

## 9. Tác giả & License
* **Tác giả:** Phan Việt Hùng, Nguyễn Mạnh Đông, Trần Minh Thành.
* **Mục đích:** Dự án Bài tập lớn học phần Khai phá dữ liệu (Data Mining).
* **License:** Sử dụng cho mục đích học tập và nghiên cứu.
