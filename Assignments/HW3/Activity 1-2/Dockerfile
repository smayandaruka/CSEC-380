FROM python:3
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
COPY HW3-ACT1-STEP2 /HW3-ACT1-STEP2.py
CMD ["python3", "HW3-ACT1-STEP2"]