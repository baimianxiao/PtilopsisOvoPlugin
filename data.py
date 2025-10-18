# -*- coding: utf-8 -*-

from dataclasses import *





@dataclass
class GroupMessageData:
    """

    """
    group_id: int
    message_id: int

@dataclass
class PokeData:
    """
    戳一戳事件
    """
    target_id: int
    target_name: str
    source_id: int
    source_name: str
    source_group_id: int

@dataclass
class EventData:
    """
    消息事件
    """
    type: str
    name: str
    data: GroupMessageData | PokeData