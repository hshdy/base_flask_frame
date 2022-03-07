#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
--------------------------------------------
# Author: hsh
# Name: requests_hook
# DATE: 2019/9/16-16:41
--------------------------------------------
"""

import logging
import logging.config
import time

from flask import request

from __const import CONST
from globals import GLOBAL
from logger.logger_service import logger


class RequestHook:
    def init_hook(self):
        app = GLOBAL.get_flask_app()

        @app.before_first_request
        def bf_first_request():
            logger.info("into before first request")

        @app.before_request
        def bf_request():
            logger.info("enter into before request")

        @app.after_request
        def aft_request(response):
            logger.info("enter into after request")
            _request_log(response)
            return response

        def _request_log(response, *args, **kws):
            now = time.time()
            request_start_time = getattr(request, "request_start_time", None)
            real_ip = request.headers.get("X-Real-Ip", request.remote_addr)

            _response = response.get_json(silent=True)
            code = _response.get("code", CONST.BIZ_CODE_FAIL) if _response else CONST.BIZ_CODE_FAIL

            # 预留心跳检测
            if request.endpoint != "HEARTBEAT_ENDPOINT":
                data = dict(
                    request_time=str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
                    remote_addr=real_ip,
                    status_code=response.status_code,
                    code=code,
                    method=request.method,
                    url=request.url,
                    endpoint=request.endpoint,
                    args=request.args.to_dict(),
                    form=request.form.to_dict(),
                    json=request.json,
                    response=_response,
                    elapsed=now - request_start_time if request_start_time else None,
                )

                logger = logging.getLogger("request")
                logger.info(data)

            return response
