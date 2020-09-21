FROM nablac0d3/sslyze
RUN pip install dnspython
COPY smtp-sslyze.py /smtp-sslyze.py
RUN chmod +x /smtp-sslyze.py
ENTRYPOINT ["/smtp-sslyze.py"]