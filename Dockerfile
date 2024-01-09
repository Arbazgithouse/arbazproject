FROM python:3.12
WORKDIR .
COPY parse_xml_file.py .
CMD ["python","parse_xml_file.py"]