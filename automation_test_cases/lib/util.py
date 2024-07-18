import logging
import os
import shutil

logging.basicConfig(level=logging.INFO, format='[%(asctime)s.%(msecs)03d] %(levelname)s %(filename)s(line:%(lineno)d): %(message)s')


def create_log_folder(log):
    logging.info("Create log folder: {}".format(log))
    if os.path.exists(log):
        logging.info("Log folder already exists, remove previous files")
        shutil.rmtree(log)
    if not os.path.exists(log):
        os.makedirs(log)
        logging.info("Completed log folder creation.")

