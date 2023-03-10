import argparse
import os
import shutil
from tqdm import tqdm
import logging
import yaml
import random
from utils.common import read_yaml, create_directories
from utils.data_mgmt import process_posts

STAGE = "One"


def main(config_path, params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    source_data = config["source_data"]
    input_data = os.path.join(source_data["data_dir"], source_data["data_file"])
    split = params["prepare"]["split"]
    seed = params["prepare"]["seed"]
    random.seed(seed)
    artifacts = config["artifacts"]
    prepared_data_dir_path = os.path.join(artifacts["ARTIFACTS_DIR"], artifacts["PREPARED_DATA"])
    create_directories([prepared_data_dir_path])
    train_data_path = os.path.join(prepared_data_dir_path, artifacts["TRAIN_DATA"])
    test_data_path = os.path.join(prepared_data_dir_path, artifacts["TEST_DATA"])
    encoded = "utf8"

    with open(input_data, encoding=encoded) as fd_in:
        with open(train_data_path, "w",encoding=encoded) as fd_out_train:
            with open(test_data_path, "w", encoding=encoded) as fd_out_test:
                process_posts(fd_in, fd_out_train, fd_out_test, "<python>", split)













if __name__=="__name__":
    args=argparse.ArgumentParser()
    args.add_argument("--congig", "-c", default="configs/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")

    parsed_args=args.parse_args()
    try:
        logging.info("\n *******")
        logging.info(f">>> Stage {STAGE} Started <<<<")
        main(config_path = parsed_args.config, params_path= parsed_args.params)
        logging.info(f">>>Stage {STAGE} has completed")
    except Exception as e:
        logging.exception(e)
        raise e
