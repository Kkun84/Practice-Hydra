import os
import hydra
from logging import getLogger

import sub


log = getLogger(__name__)


@hydra.main(config_path='conf/config.yaml')
def main(cfg):
    print(cfg.pretty())
    print(cfg)
    log.debug('main')
    log.info('main')
    sub.sub()


if __name__ =='__main__':
    main()
