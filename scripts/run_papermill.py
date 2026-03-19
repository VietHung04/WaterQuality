# scripts/run_papermill.py

import papermill as pm
import os

# Đảm bảo thư mục output chuẩn theo yêu cầu của Rubric là outputs
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)

pipeline = [
    ("notebooks/01_eda.ipynb", f"{output_dir}/01_eda_out.ipynb"),
    ("notebooks/02_preprocess.ipynb", f"{output_dir}/02_preprocess_out.ipynb"),
    ("notebooks/03_mining.ipynb", f"{output_dir}/03_mining_out.ipynb"),
    ("notebooks/04_model.ipynb", f"{output_dir}/04_model_out.ipynb"),
    ("notebooks/04b_semi.ipynb", f"{output_dir}/04b_semi_out.ipynb"),
    ("notebooks/05_evaluation.ipynb", f"{output_dir}/05_evaluation_out.ipynb"),
]

# Lấy đường dẫn tuyệt đối của thư mục notebooks để ép Papermill chạy tại đây
notebooks_dir = os.path.join(os.getcwd(), "notebooks")

for input_nb, output_nb in pipeline:
    print(f"Running {input_nb} ...")

    pm.execute_notebook(
        input_path=input_nb,
        output_path=output_nb,
        parameters={},
        cwd=notebooks_dir  # SỬA Ở ĐÂY: Ép kernel chạy ở thư mục notebooks
    )

print("Pipeline completed successfully! All outputs are saved in 'outputs/'.")