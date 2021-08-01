export MODEL_DIR=models
export TRAIN_DATA="data/train.txt"
export VAL_DATA="data/val.txt"
export BASE_MODEL_NAME="flax-community/gpt2-small-indonesian"

python run_clm_flax.py \
    --num_train_epochs="8" \
    --output_dir="${MODEL_DIR}" \
    --model_name_or_path="${BASE_MODEL_NAME}" \
    --do_train \
    --train_file="${TRAIN_DATA}" \
    --do_eval \
    --validation_file="${VAL_DATA}" \
    --dataloader_num_workers="64" \
    --preprocessing_num_workers="64" \
    --logging_steps="5000" \
    --save_steps="5000" \
    --eval_steps="5000" \
    --overwrite_output_dir \
    --push_to_hub
