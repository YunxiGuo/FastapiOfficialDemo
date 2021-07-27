# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :items.py
# @Time      :2021/7/26 14:54
# @Author    :guoyunxi


from fastapi import APIRouter

router = APIRouter()

items = [{"item_id": 1, "item_name": "lucy"}, {"item_id": 2, "item_name": "lily"}]


@router.get(path="/items", tags=["items"])
async def get_items():
    """

    :return:
    """
    return items


@router.get(path="/items/{item_id}", tags=["items"])
async def get_item(item_id: int):
    for item in items:
        if item.get("item_id") == item_id:
            return item
    return
