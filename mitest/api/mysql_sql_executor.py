# -*- coding:utf-8 -*-

"""
File Name: `mysql_sql_executor`.py
Version:
Description:

Author: wangyongjun
Date: 2018/7/12 17:03
"""
import re
import traceback

from sqlalchemy import create_engine, DDL
from sqlalchemy.pool import NullPool

from mitest.api.comm_log import logger
from mitest.models.mitest_platform import EnvInfo


def sql_execute(sql, env_name='aliuat'):
    """
    """
    # env = env.upper()
    try:
        obj = EnvInfo.query.filter_by(env_name=env_name).first()
        db_info = obj.db_connect
        # db_info = db_connects[env][db_type]

    except Exception as err:
        raise Exception('\n'.join([str(err), traceback.format_exc()]))

    engine = create_engine(db_info, echo=False, poolclass=NullPool)
    return_info = None
    with engine.connect() as conn:
        try:
            if re.match('select', sql.lower().strip()):
                return_info = conn.execute(sql).fetchall()
            elif re.match('exec', sql.lower().strip()):
                sql_new = DDL(sql)
                conn.execute(sql_new)
            else:
                return_info = conn.execute(sql).rowcount
                logger.info("受影响的行: {0}".format(return_info))
        except Exception as err:
            logger.exception(err)
        finally:
            conn.close()

    return return_info