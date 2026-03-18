# scripts/run_papermill.py

import papermill as pm
import os

# đảm bảo thư mục output tồn tại
os.makedirs("notebooks/output", exist_ok=True)

pipeline = [
    ("notebooks/01_eda.ipynb", "notebooks/output/01_eda_out.ipynb"),
    ("notebooks/02_preprocess.ipynb", "notebooks/output/02_preprocess_out.ipynb"),
    ("notebooks/03_mining.ipynb", "notebooks/output/03_mining_out.ipynb"),
    ("notebooks/04_model.ipynb", "notebooks/output/04_model_out.ipynb"),
    ("notebooks/04b_semi.ipynb", "notebooks/output/04b_semi_out.ipynb"),
    ("notebooks/05_evaluation.ipynb", "notebooks/output/05_evaluation_out.ipynb"),
]

for input_nb, output_nb in pipeline:
    print(f"Running {input_nb} ...")

    pm.execute_notebook(
        input_path=input_nb,
        output_path=output_nb,
        parameters={}
    )

print("Pipeline completed successfully!")