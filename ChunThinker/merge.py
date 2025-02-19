from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

# Tải model gốc (thay thế bằng model bạn đã dùng để fine-tune)
base_model_name = "unsloth/Llama-3.2-3B"  # Thay bằng model gốc của bạn
model = AutoModelForCausalLM.from_pretrained(base_model_name)
tokenizer = AutoTokenizer.from_pretrained(base_model_name)

# Đường dẫn đến thư mục chứa adapter
adapter_path = r"ChunThinker/outputs/checkpoint-1500"

# Tải adapter và merge vào model gốc
model = PeftModel.from_pretrained(model, adapter_path)
model = model.merge_and_unload()  # Merge adapter vào model

# Lưu model đã merge
merged_model_path = (
    r"outputs/merged"
)
model.save_pretrained(merged_model_path)
tokenizer.save_pretrained(merged_model_path)

print("Model merged and saved to", merged_model_path)
