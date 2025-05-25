FROM python:3.10-slim

WORKDIR /app

COPY instruction_following_eval/ ./instruction_following_eval/

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r instruction_following_eval/requirements.txt
RUN python3 -m nltk.downloader punkt_tab

RUN mkdir -p /app/output

CMD ["python3", "-m", "instruction_following_eval.evaluation_main", \
     "--input_data=instruction_following_eval/input.jsonl", \
     "--input_response_data=responses.jsonl", \
     "--output_dir=output/"]