import random

class ClassHelper:
    def __init__(self, stu_lst):
        self.stu_lst = stu_lst

    def pick(self, n): # n명 뽑기
        if self.stu_lst:
            if n <= len(self.stu_lst):
                lst = []
                tmp_lst = self.stu_lst[:]

                for idx in range(n):
                    stu_name = random.choice(tmp_lst)
                    lst.append(stu_name)
                    tmp_lst.remove(stu_name)
                    
                return lst
            else:
                return '숫자가 너무 큼'
        else:
            return '빈 리스트'

    def match_pair(self): # 조 짜기
        lsts = []
        tmp_lst = self.stu_lst[:]

        while tmp_lst:
            match_lst = random.sample(tmp_lst, 2)
            lsts.append(match_lst)      

            for rm_stu in match_lst:
                tmp_lst.remove(rm_stu)

            if 3 >= len(tmp_lst):
                lsts.append(tmp_lst)
                return ClassHelper.p_print(lsts)

    @staticmethod
    def p_print(lsts): # 인쇄용?
        return_strs = ''

        if len(lsts):
            cnt = 1

            for lst in lsts:
                return_strs += f'{cnt} 조 : {lst}\n'
                cnt += 1

            return return_strs
        else:
            return '빈 리스트'

ch = ClassHelper(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
# ch = ClassHelper([])

print(ch.pick(2))
print(ch.match_pair())