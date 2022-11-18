import time

from services.general import General
from components import structure as struct, record as rec, task as tk
import random as rn


class SangoActivity(General):

    def __init__(self, user_id: str):
        super().__init__(user_id)
        self._social_media = None
        self._task = tk.Task()
        self._rec = rec.Record()

    def init_task_decision(self):
        self.decide_hall()
        self.click_task()
        self.choose_hall()
        self.choose_level()
    
    def given_credit(self):
        return struct.Struct.get_credits()

    def click_task(self):
        if self.watch_loader():
            self.get_navbar().task_link().click()

    def decide_hall(self):
        if self.watch_loader():
            credit = int(self.given_credit())
            halls = ['fb','tiktok'] * (credit if credit > 1 else 2)
            rn.shuffle(halls)
            self._social_media = rn.choice(halls)

    def choose_level(self):
        if self.watch_loader():
            if struct.Struct.account_level() == 'Lv.0':
                self._task.level0_link().click()
            elif struct.Struct.account_level() == 'Lv.1':
                self._task.level1_link().click()
            elif struct.Struct.account_level() == 'Lv.2':
                self._task.level2_link().click()
            elif struct.Struct.account_level() == 'Lv.3':
                self._task.level3_link().click()

    def choose_hall(self):
        if self.watch_loader():
            self._task.tiktok_link()
            if self._social_media == 'fb':
                self._task.facebook_link().click()
            elif self._social_media == 'tiktok':
                self._task.tiktok_link().click()

    def choose_commission(self):
        flag = False
        if self.watch_loader():
            commission = self._task.commissions_link()
            if commission is not None:
                commission.click()
            else:
                time.sleep(1.5)
                self.reload_page()
                self.choose_commission()
            time.sleep(2.5)
            flag = commission is None
        return flag
                

    def click_record(self):
        if self.watch_loader():
            self.get_navbar().record_link().click()
            self.watch_loader()

    def available_credit(self):
        self.watch_loader()
        return self._rec.credit()

    def adtime_expired(self):
        print('Waiting for advert time to complete.')
        if self.watch_loader():
            time.sleep(10)
        return True

    def click_wos(self):
        res = self.record_exists()
        if res is not None:
            res.wos_button().click()

    def watch_at_record(self) -> bool:
        flag = self.record_exists() is not None
        if flag:
            print('Watching video...')
            self.click_wos()
            self.switch_tab(0)
            if self.adtime_expired():
                self.click_wos()
                self.switch_tab(-1)
                time.sleep(1)
                self.close_tab()
                self.switch_tab(0)
                time.sleep(3)
        return flag

    def record_exists(self):
        flag = None
        if self.watch_loader():
            self._rec.progress_link().click()
            try:
                self._rec.sample_button()
                flag = self._rec
            except:
                pass
        return flag
