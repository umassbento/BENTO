
from options import opt
import logging
from command2json import command2json
from translator import run_cl_cmd, json2cl_upload, json2cl_run
import json

if __name__ == '__main__':

    logger = logging.getLogger()
    if opt.verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    logging.info(opt)

    if opt.upload is not None:
        cmd = {u'upload': opt.upload}
        json_cmd = command2json(cmd)
        cl_cmd = json2cl_upload(json_cmd)
        run_cl_cmd(cl_cmd)
    elif opt.run is not None:
        list_module = opt.run.split(u",")

        cmd = {u'list_module': list_module, u'data': opt.data}
        json_cmd = command2json(cmd)

        list_cl_cmd = json2cl_run(json_cmd)

        for cl_cmd in list_cl_cmd:
            run_cl_cmd(cl_cmd)










    else:
        raise RuntimeError(u"Invalid arguments!")

    pass