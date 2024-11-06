#!/app/python-base/.venv/bin/python
import os
import logging
#BOILERPLATE
#TODO: usar função
#TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL","WARNING").upper()
log = logging.Logger("teste", log_level)
ch = logging.StreamHandler() #Console\ Terminal \ stderr
ch.setLevel(log_level)
#formatação
fmt = logging.Formatter(
    "%(asctime)s\t%(name)s\t%(levelname)s\t"
    "l:%(lineno)d\tf:%(filename)s:\t%(message)s"
)

ch.setFormatter(fmt)
log.addHandler(ch)

print("-Sem formatação")
logging.debug("Mensagem para o dev, qe, sysadmin")
logging.info("Mensagem geral para usuários")
logging.warning("Aviso que não causa erro")
logging.error("Erro que afeta uma única execução")
logging.critical("Erro geral ex.banco de dados sumiu")
print("*"*40)
print("-Com formatação")

log.debug("Mensagem para o dev, qe, sysadmin")
log.info("Mensagem geral para usuários")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma única execução")
log.critical("Erro geral ex. algo parou de funcionar, banco de dados sumiu")


try:
    1/0
except ZeroDivisionError as e:
    logging.error("Deu erro %s", str(e))