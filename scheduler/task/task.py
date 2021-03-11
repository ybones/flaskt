# -*- coding: utf-8 -*-
"""
Created on 2021/3/8

@author     : yu
@desc       : 调度器
trigger ：
    "date" : from apscheduler.triggers.date import DateTrigger
    "interval": from apscheduler.triggers.interval import IntervalTrigger
    "cron": from apscheduler.triggers.cron import CronTrigger
"""
import logging

from apscheduler.schedulers.gevent import GeventScheduler

sche = GeventScheduler()


@sche.scheduled_job('cron', id='print_info', day_of_week='0-6', hour=21)
def print_info():
    """每天21点执行一次"""
    logging.info("hello scheduler")


def init(app):
    sche.start()
