import json
import os
import logging

def run_cl_cmd(cl_cmd):
    os.system(cl_cmd)
    logging.info(u"finish running: {}".format(cl_cmd))

def json2cl_upload(json_cmd):
    cmd = json.loads(json_cmd)
    cl_cmd = u'cl upload {}'.format(cmd[u'upload'])
    return cl_cmd

def json2cl_run(json_cmd):
    cmd = json.loads(json_cmd)

    cl_cmd = []

    for module in cmd[u'list_module']:
        if module == u'ner_re':
            cl_cmd.append(u'cl run {}'.format(u"--request-docker-image foxlf823/cpu_ner_re:0.2 :ner_and_re_pipeline :{} "
                                              u":default.config 'python3 ner_and_re_pipeline/main.py -whattodo 2 "
                                              u"-config default.config -output ner_and_re_pipeline/output "
                                              u"-input {}/corpus -predict ./predict'".format(cmd[u'data'], cmd[u'data'])))
        else:
            raise RuntimeError(u"no module named {}".format(module))

    return cl_cmd


