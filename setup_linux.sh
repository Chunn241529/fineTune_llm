#!/bin/bash

# Kiểm tra xem môi trường ảo đã tồn tại chưa
if [ -d ".venv" ]; then
    echo "Môi trường ảo virtual environment đã tồn tại."
else
    # Tạo mới môi trường ảo
    echo "Đang tạo mới virtual environment..."
    python3 -m venv .venv

    # Kiểm tra việc tạo môi trường ảo có thành công không
    if [ ! -d ".venv" ]; then
        echo "Lỗi khi tạo môi trường ảo virtual environment."
        exit 1
    fi
fi

# Kích hoạt môi trường ảo
echo "Kích hoạt môi trường ảo virtual environment..."
source .venv/bin/activate


echo "Install packed"


python3 -m pip install --upgrade pip
pip3 install torch torchvision torchaudio
pip3 install ipykernel
pip3 install vllm

echo "Đã xong!"
