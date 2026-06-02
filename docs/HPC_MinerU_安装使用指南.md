# MinerU 在 KU Leuven HPC 上安装与使用指南

> 适用环境：KU Leuven tier2 HPC，GPU 分区 `gpu_v100`（Tesla V100 32GB × 8）
> 更新时间：2026-05-31
> MinerU 版本：3.2.1

---

## 目录

1. [环境信息](#环境信息)
2. [第一步：上传 PDF 到 HPC](#第一步上传-pdf-到-hpc)
3. [第二步：批量处理文件名](#第二步批量处理文件名)
4. [第三步：申请 GPU 计算节点](#第三步申请-gpu-计算节点)
5. [第四步：创建环境并安装](#第四步创建环境并安装)
6. [第五步：交互式测试](#第五步交互式测试)
7. [第六步：批量提交 Slurm 作业](#第六步批量提交-slurm-作业)
8. [第七步：下载结果到本地](#第七步下载结果到本地)
9. [附录：后端引擎选择](#附录后端引擎选择)
10. [附录：常见故障排查](#附录常见故障排查)

---

## 环境信息

| 项目 | 值 |
|------|-----|
| 登录节点 | `tier2-p-login-4` |
| GPU 分区 | `gpu_v100` |
| GPU 型号 | Tesla V100-SXM2 32GB × 8 / 节点 |
| CPU | Xeon，每 GPU 配 8 核 |
| 内存 | 每节点 256GB |
| CUDA | 12.6.0（`module load CUDA/12.6.0`） |
| 网络 | ✅ 可连接 HuggingFace（模型自动下载） |
| 用户存储 | `/data/leuven/373/vsc37343/` |

---

## 第一步：上传 PDF 到 HPC

### 从 Windows 本地上传

在 Windows PowerShell 中执行：

```powershell
scp -r "D:\04_claude_code\01_Fitness\fitness-advisor\fitness_PDF_source\*.pdf" vsc37343@tier2-p-login-4:/data/leuven/373/vsc37343/PDF/
```

### 从 AutoDL 云服务器转发

```bash
scp -r /root/fitness_PDF_source/*.pdf vsc37343@tier2-p-login-4:/data/leuven/373/vsc37343/PDF/
```

> 两种方式任选其一。上传完成后在 HPC 上 `ls /data/leuven/373/vsc37343/PDF/` 确认文件齐全。

---

## 第二步：批量处理文件名

原始文件名含大量空格和中文标点，会干扰命令行参数解析。在 **登录节点** 上执行：

```bash
cd /data/leuven/373/vsc37343/PDF/

# 批量替换空格和特殊字符为下划线
for f in *.pdf; do
    newname=$(echo "$f" | sed 's/[ ()：（）【】「」&、]/_/g' | sed 's/__*/_/g')
    if [ "$f" != "$newname" ]; then
        mv "$f" "$newname"
        echo "改名: $f → $newname"
    fi
done

# 确认
ls -lh
```

改名后文件名示例：

| 改名前 | 改名后 |
|--------|--------|
| `邓树勋 运动生理学 3版 教材_14010277.pdf` | `邓树勋_运动生理学_3版_教材_14010277.pdf` |
| `运动解剖学  第3版_13741834.pdf` | `运动解剖学_第3版_13741834.pdf` |
| `中国居民膳食指南（2022年）.pdf` | `中国居民膳食指南_2022年_.pdf` |

---

## 第三步：申请 GPU 计算节点

> ⚠️ **不要在登录节点跑 OCR**，会耗尽登录节点内存导致作业被杀。

申请交互式 GPU 会话（1 张 V100，4 小时）：

```bash
srun --partition=gpu_v100 \
     --gres=gpu:1 \
     --time=04:00:00 \
     --ntasks=1 \
     --cpus-per-task=8 \
     --mem=64G \
     --pty bash
```

等分配成功后终端提示符会变成计算节点的主机名。

---

## 第四步：创建环境并安装

在 **计算节点** 上执行（一次性操作）：

### 4.1 加载 CUDA

```bash
module load CUDA/12.6.0
```

### 4.2 创建 conda 环境

```bash
conda create -n mineru python=3.10 -y
conda activate mineru
```

### 4.3 安装 PyTorch（GPU 版）

```bash
conda install pytorch torchvision pytorch-cuda=12.6 -c pytorch -c nvidia -y
```

### 4.4 验证 GPU 可用

```bash
python3 -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
```

**预期输出：**

```
True
Tesla V100-SXM2-32GB
```

### 4.5 安装 MinerU 完整版

```bash
pip install "mineru[all]"
```

安装包约 5-8 GB，包含 PyTorch、CUDA 库、transformers、OCR 模型等依赖。

### 4.6 验证安装

```bash
mineru --version
```

**预期输出：**

```
mineru, version 3.2.1
```

---

## 第五步：交互式测试

在继续批量处理之前，先拿一本最小的教材跑通流程。

### 5.1 创建输出目录

```bash
mkdir -p /data/leuven/373/vsc37343/output/
```

### 5.2 测试一本（推荐 hybrid-auto-engine）

```bash
mineru -p /data/leuven/373/vsc37343/PDF/运动解剖学_第3版_13741834.pdf \
       -o /data/leuven/373/vsc37343/output/运动解剖学/ \
       -b hybrid-auto-engine
```

首次运行会自动从 HuggingFace 下载模型（约 2-4 GB），等待约 2-5 分钟。

### 5.3 确认输出

```bash
ls -lh /data/leuven/373/vsc37343/output/运动解剖学/
```

**预期输出结构：**

```
运动解剖学/
├── 运动解剖学_第3版_13741834.md    # 主要 Markdown 文件
├── images/                          # 提取的图片
├── layout/                          # 布局可视化
└── ...
```

### 5.4 检查 Markdown 质量

```bash
head -100 /data/leuven/373/vsc37343/output/运动解剖学/运动解剖学_第3版_13741834.md
```

确认表格是否保留、公式是否以 LaTeX 格式呈现、章节标题是否识别正确。

> 如果 hybrid-auto-engine 失败（如网络波动），改用纯 pipeline：
> ```bash
> mineru -p /data/leuven/373/vsc37343/PDF/运动解剖学_第3版_13741834.pdf \
>        -o /data/leuven/373/vsc37343/output/运动解剖学/ \
>        -b pipeline
> ```

---

## 第六步：批量提交 Slurm 作业

测试通过后，用 Slurm 脚本后台批量处理全部 14 本教材。

### 6.1 创建 Slurm 提交脚本

在登录节点上创建文件 `~/mineru_batch.sh`：

```bash
#!/bin/bash
#SBATCH --partition=gpu_v100
#SBATCH --gres=gpu:1
#SBATCH --time=12:00:00
#SBATCH --job-name=mineru_ocr
#SBATCH --output=/data/leuven/373/vsc37343/mineru_%j.log
#SBATCH --error=/data/leuven/373/vsc37343/mineru_%j.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G

# 加载环境
module load CUDA/12.6.0
source $(conda info --base)/etc/profile.d/conda.sh
conda activate mineru

# 路径配置
PDF_DIR="/data/leuven/373/vsc37343/PDF"
OUT_DIR="/data/leuven/373/vsc37343/output"
BACKEND="hybrid-auto-engine"   # 可改为 pipeline

mkdir -p "$OUT_DIR"

# 初始化统计
TOTAL=0
SUCCESS=0
FAIL=0

for f in "$PDF_DIR"/*.pdf; do
    name=$(basename "$f" .pdf)
    TOTAL=$((TOTAL + 1))

    echo "========================================="
    echo "[$(date)] 处理 ($TOTAL): $name"
    echo "========================================="

    mineru -p "$f" -o "$OUT_DIR/$name/" -b "$BACKEND"

    if [ $? -eq 0 ]; then
        echo "[$(date)] ✅ 完成: $name"
        SUCCESS=$((SUCCESS + 1))
    else
        echo "[$(date)] ⚠️ hybrid 失败，尝试 pipeline: $name"
        mineru -p "$f" -o "$OUT_DIR/$name/" -b pipeline
        if [ $? -eq 0 ]; then
            echo "[$(date)] ✅ pipeline 完成: $name"
            SUCCESS=$((SUCCESS + 1))
        else
            echo "[$(date)] ❌ 失败: $name"
            FAIL=$((FAIL + 1))
        fi
    fi
done

echo "========================================="
echo "[$(date)] 处理完毕"
echo "  总计: $TOTAL  成功: $SUCCESS  失败: $FAIL"
echo "========================================="
```

### 6.2 提交作业

```bash
sbatch ~/mineru_batch.sh
```

返回类似：`Submitted batch job 123456`

### 6.3 查看状态

```bash
# 查看作业队列
squeue -u $USER

# 查看实时日志
tail -f /data/leuven/373/vsc37343/mineru_123456.log

# 查看错误日志
tail -f /data/leuven/373/vsc37343/mineru_123456.err
```

### 6.4 预计时间

| 教材 | 页数（估） | V100 处理时间（估） |
|------|:-----:|:-----:|
| NSCA-certification-handbook | 73 | 1 分钟 |
| NASM 体能训练手册 | ~100 | 2 分钟 |
| 执教的语言 | ~200 | 3 分钟 |
| 解剖列车 | ~300 | 5 分钟 |
| 运动解剖学 | ~350 | 6 分钟 |
| 运动生理学 | ~450 | 8 分钟 |
| 中国居民膳食指南 | ~400 | 7 分钟 |
| NSCA-CSCS | ~700 | 12 分钟 |
| NASM-CPT | ~600 | 10 分钟 |
| 运动测试与运动处方指南 | ~500 | 9 分钟 |
| ACE | ~900 | 15 分钟 |
| Essentials of Exercise Science | ~500 | 9 分钟 |
| ACSM运动营养学 | ~400 | 7 分钟 |
| **总计** | **~5500** | **~1.5-2 小时** |

---

## 第七步：下载结果到本地

作业完成后，在 **Windows PowerShell** 中执行：

```powershell
scp -r vsc37343@tier2-p-login-4:/data/leuven/373/vsc37343/output/ "D:\04_claude_code\01_Fitness\fitness-advisor\extracted_output\"
```

---

## 附录：后端引擎选择

| 引擎 | 精度 | 速度 | 显存需求 | 需要联网 | 适用场景 |
|------|:--:|:--:|:------:|:------:|------|
| `hybrid-auto-engine` | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ≥8GB | ✅ 首次 | **推荐**，精度最高 |
| `vlm-auto-engine` | ⭐⭐⭐⭐⭐ | ⭐⭐ | ≥8GB | ✅ 首次 | 精度最高但更慢 |
| `pipeline` | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ≥4GB | ❌ | 离线可用，稳定无幻觉 |

> V100 32GB 三个引擎都能跑。建议 `hybrid-auto-engine` 优先，失败降 `pipeline`。

---

## 附录：常见故障排查

| 错误信息 | 原因 | 解决方法 |
|------|------|------|
| `LocalEntryNotFoundError` | HuggingFace 下载模型失败 | 检查网络 `curl https://huggingface.co`；或换 `-b pipeline` |
| `CUDA out of memory` | 显存不足 | 换 `-b pipeline`（显存需求更低） |
| `No supported documents found` | 文件名含特殊字符或路径错误 | 用 `ls` 确认文件存在，检查第二步改名是否完成 |
| `Module not found: CUDA/12.6.0` | 未加载 CUDA module | `module load CUDA/12.6.0` |
| `conda: command not found` | 登录节点 conda 未初始化 | `source $(conda info --base)/etc/profile.d/conda.sh` |
| `Module slurm not found` | 在登录节点跑了 `srun` | 确认在登录节点执行 `srun`（正常行为），登录后终端会切换到计算节点 |
| 计算节点无外网 | 部分 HPC 节点限制外网 | 用 `-b pipeline`（纯本地，不联网） |

---

## 快捷命令速查

```bash
# 申请 GPU 节点
srun --partition=gpu_v100 --gres=gpu:1 --time=04:00:00 --ntasks=1 --cpus-per-task=8 --mem=64G --pty bash

# 加载环境
module load CUDA/12.6.0 && source $(conda info --base)/etc/profile.d/conda.sh && conda activate mineru

# 验证
python3 -c "import torch; print(torch.cuda.get_device_name(0))"

# 测试一本
mineru -p /path/to/file.pdf -o /path/to/output/ -b hybrid-auto-engine

# 批量提交
sbatch ~/mineru_batch.sh

# 查看状态
squeue -u $USER

# 取消作业
scancel <JOB_ID>
```
