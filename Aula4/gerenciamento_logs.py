#!/usr/bin/env python3

import logging

logging.basicConfig(

    filename='app.log',
    level=logging.ERROR,
    format='%(asctime)s [ %(levelname)s ]  %(name)s\n'
    +
    "[%(funcName)s] [%(filename)s, %(lineno)s] %(message)s",
    datefmt="[%d/%m/%Y %H:%M:%S]"

)

logging.debug('Mensagem de debug')
logging.warning('mensagem de warning')
logging.error('mensagem de error')
logging.info('mensagem de informação')


def soma(n1, n2):
    try:
        logging.info('soma efetuada com sucesso')
        return n1+n2
    except Exception:
        logging.error('deu erro')

#print(soma(1, 'bata1'))


CUSTOM = 49

logging.addLevelName(CUSTOM, "CUSTOM")


def alert(self, message, *args, **kwargs):
    if self.isEnabledFor(CUSTOM):
        self._log(CUSTOM, message, args, **kwargs)


logging.Logger.custom = alert

logger = logging.getLogger()
logger.custom('Mensagem de logs customizada ')
