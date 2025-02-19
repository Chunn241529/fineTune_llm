import torch
torch.cuda.empty_cache()

from vllm import LLM, SamplingParams

# Khởi tạo model
llm = LLM(model="ChunThinker/outputs/merged")  # Đường dẫn tới thư mục merged_model

# Tạo tham số sampling
sampling_params = SamplingParams(temperature=0.7, max_tokens=50)

# Generate text
prompts = ["Hello, my name is"]
outputs = llm.generate(prompts, sampling_params)

# In kết quả
for output in outputs:
    print(output.outputs[0].text)