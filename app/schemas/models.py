#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :models.py
# @Time      :2021/7/27 18:12
# @Author    :guoyunxi

from pydantic import BaseModel


class StaticResponse(BaseModel):
    code: int
    result: str
    data: str
    msg: str
