#!/usr/bin/env python
class  My_assertion:
    @staticmethod
    def my_assert(expect_res,actual_res):
        try:
            if actual_res.find(expect_res)==-1:
                return False
            else:
                return True
        except Exception as e:
            raise   e
