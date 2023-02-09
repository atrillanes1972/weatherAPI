FROM python:2
WORKDIR /logcleaner
COPY deldir.py ./
COPY testconfig.yaml ./
COPY dirprocess.txt ./tmp/
COPY dirarchive.txt ./tmp/
RUN mkdir -p tmp testdir1 testdir2 testdir3 \
    && cd testdir1; touch file1 file2; cd ../testdir2 ; \
    touch file3 file4 ; cd ../testdir3 ; touch file5 file6 \
    && pip install pyyaml
CMD [ "sh","-c","python ./deldir.py ; sh" ]

