import os
import hydra
from logging import getLogger

import sub


logger = getLogger(__name__)


@hydra.main(config_path='conf/config.yaml')
def main(cfg):
    logger.info(cfg.pretty())
    print(cfg)
    logger.debug('main')
    logger.info('main')
    sub.sub()


if __name__ =='__main__':
    main()
