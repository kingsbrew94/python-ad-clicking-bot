from services.sango_activity import SangoActivity
from services.page import Page 
from services import helpers as hp
from components.structure import Struct
from datetime import datetime, date


class Sango(SangoActivity):

    _inst = None
    
    def __init__(self, data: dict):
        super().__init__(data['user_id'])
        self.browse()
        self._active_user = None
        Sango._inst = self
        self._video_flag = False

    @staticmethod
    def get_instance():
        return Sango._inst
    
    def _continue_preempted_activity(self):
        if self.is_preempted():
            if Page.get() == 'LOGIN':
                self.activity()
            elif Page.get() == 'MY':
                self.logout()
                self.logged_accounts().append(self._active_user)
            elif (Page.get() == 'TASK') or (Page.get() == 'RECORD'):
                self.watch_video()
    
    def _initialize(self, user_accounts):
        
        self._continue_preempted_activity()
        for acc in user_accounts:
            if hp.stop_on_command():
                break

            if hp.resting_time():
                return False
            
            if acc['USERNAME'] in self.logged_accounts():
                if acc['LEVEL'] == 'Lv.0':
                    print("Account with the username '{}' is at level 0 Please upgrade.".format(acc['USERNAME']))
                continue
            print(acc)
            Struct.set_credits(acc['CREDIT'])
            if (not self.login(acc['USERNAME'], acc['PASSWORD'])) and (not self.at_home()):
                print('Unable to login, your login credentials may be invalid!')
                print(f"USERNAME: {acc['USERNAME']}", f"PASSWORD: {acc['PASSWORD']}", sep='\n')
                if len(self.user_accounts()) > 1:
                    print('Moving to next account...')
                continue

            if hp.stop_on_command():
                self.logout()
                break

            self._active_user = acc['USERNAME']
            self.watch_video()
            self.preempt(False)
            if self._video_flag is True:
                hp.add_logs({'LOGS': acc['USERNAME'], 'DATE_ADDED': datetime.now()})
                self.logged_accounts().append(self._active_user)
        self.logged_accounts().clear()
        print("\n==================================================\n")
        print("Activity Log Ended @ :: {}\n".format(datetime.now()))
        return True
    
    def _filter_logs(self, accounts, usernames) -> list:
        filtered_accounts = []
        for usrn in usernames:
            for acc in accounts:
                if not(usrn == acc['USERNAME']):
                    filtered_accounts.append(acc)
        return filtered_accounts if len(usernames) > 0 else accounts
    
    def activity(self):
        print("\n==================================================\n")
        print("Activity Log Started @ :: {}\n".format(datetime.now()))
        if hp.resting_time():
            return False
        
        accounts  = self.user_accounts()
        usernames = []
        for acc in accounts:
            if hp.stop_on_command():
                break
            res = hp.log_exists(acc['USERNAME'], date.today())
            if (res is not None) and (len(res) > 0):
                usernames.append(acc['USERNAME'])
        self.preempt(False)
        return self._initialize(self._filter_logs(accounts, usernames))

    def login(self, username: str, password: str) -> bool:

        self.watch_loader()
        flag = self.login_form_exists()

        flag = flag and self.watch_loader()

        if flag:
            self.bot_login(username, password)
            if (self.watch_loader() and self.login_form_exists()) or (Page.get() == 'LOGIN'):
                flag = False
                self.clear_login_form()
            else:
                self.logged_accounts().append(username)
        return flag
    
    def watch_video(self):
        if self._watch_video():
            self.logout()
        else:
            print('Watching video was not allowed: '
                  'this exception occurs when your membership account has not been upgraded or '
                  'the time to watch video has reached its limit.')
            print(
                'Suggestions: Please upgrade your membership from Lv.0 to any level or if the time limit has been reached'
                ' I will try again later, Thank you.')
            
    def _watch_video(self) -> bool:
        flag = True
        self._video_flag = False
        if self.watch_loader():
            self.click_record()
            gct = self.available_credit()
            credit = int(gct.text if gct is not None else self.given_credit())
            print('Credit: {}'.format(credit))
            print('About Watching video...')
            if self.watch_at_record() is False:
                self._video_flag = credit > 0
                while credit > 0:
                    self.init_task_decision()
                    if not self.choose_commission():
                        self.click_record()
                        if not self.watch_at_record():
                            self.logout()
                            flag = False
                            self._video_flag = False
                            break
                    self.watch_at_record()
                    gct = self.available_credit()
                    credit = int(gct.text if gct is not None else (credit - 1))
                    print('Video watched successfully!')
        return flag
            
    def logout(self):
        if self.watch_loader():
            print('Logging out...')
            self.bot_logout()

