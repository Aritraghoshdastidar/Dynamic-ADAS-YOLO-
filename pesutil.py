import sys
import psutil
import subprocess
from pathlib import Path

# ── CONFIG ──────────────────────────────────────────────────────────────────────
YOLOV7_REPO    = Path(r"C:\yolov7-main\yolov7-main")
YOLOV11_REPO   = Path(r"C:\PESU\CIE\bdd100k_yolov11")

MODEL_HEAVY    = YOLOV7_REPO / "runs/train/yolov7x-finetune-fast/weights/best.pt"
MODEL_LIGHT    = YOLOV11_REPO / "runs/detect/train4/weights/best.pt"

DETECT7_SCRIPT = YOLOV7_REPO / "detect.py"
PREDICT11_SCRIPT = YOLOV11_REPO / "runs/detect/train4/weights/predict1.py"

OUTPUT_DIR     = Path(r"C:\Users\aritr\OneDrive\Desktop\CIE\runs")

CPU_THRESHOLD  = 50  # %
RAM_THRESHOLD  = 30  # %
# ────────────────────────────────────────────────────────────────────────────────

def get_system_load():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    return cpu, ram

def select_model():
    cpu, ram = get_system_load()
    print(f"[INFO] CPU: {cpu:.1f}% | RAM: {ram:.1f}%")
    if cpu > CPU_THRESHOLD or ram > RAM_THRESHOLD:
        print("[INFO] High load = using LIGHT model (YOLOv11).")
        return "light", MODEL_LIGHT, PREDICT11_SCRIPT
    else:
        print("[INFO] Sufficient resources = using HEAVY model (YOLOv7).")
        return "heavy", MODEL_HEAVY, DETECT7_SCRIPT

def run_inference(script_path: Path, weights_path: Path, img_source: str, variant: str):
    print(f"[INFO] Running {script_path.name} on {img_source}")

    if variant == "light":
        # Run YOLOv11
        cmd = [
            sys.executable,
            str(script_path),
            "--weights", str(weights_path),
            "--source", img_source,
            "--output", str(OUTPUT_DIR / "yolov11_output")
        ]
    else:
        # Run YOLOv7 with extra output control
        cmd = [
            sys.executable,
            str(script_path),
            "--weights", str(weights_path),
            "--source", img_source,
            "--conf", "0.25",
            "--save-txt",
            "--save-conf",
            "--project", str(OUTPUT_DIR),
            "--name", "yolov7_output"
        ]

    subprocess.run(cmd, check=True)
    print(f"[INFO] Done. Results saved in {OUTPUT_DIR}\\{variant}_output")

def run():
    variant, model_path, script_path = select_model()

    # ── Replace with your image source ──
    img = r"C:\Users\aritr\Downloads\210801775.jpg"

    run_inference(script_path, model_path, img, variant)

if __name__ == "__main__":
    run()
