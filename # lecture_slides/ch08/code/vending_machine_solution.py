# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 18:16:21 2016

@author: Yunho
"""
import sys
print sys.getdefaultencoding()
# 자판기 
# TODO: 물건 수급 - 판매중 상태에서 관리자 모드를 활성화 시키는 코드를 입력하면 문이 열린다.
# TODO: 관리자 모드 - 관리자는 물품을 선택하고 해당 물품의 숫자를 보충할 수 있다. 
# TODO: 여기에서 10개가 넘으면 저장공간이 꽉 찼다는 메세지를 보낸다. 
# TODO: 물건을 고르고, 물건을 골랐을 때, 
# TODO: 비용이 적절하면 물건과 함께 거스름돈이 나온다., 
# TODO: 비용이 모자라면 금액을 더 입력해달라는 메세지가 나온다. 
# TODO: 물건이 떨어지면 [매진] 메시지를 출력하시오

vending_condition = True

admin_code = 9190

total_money = 0 

item1_name = "사탕"
item1_price = 300
item1_num = 5

item2_name = "과자"
item2_price = 1000
item2_num = 6

def init_screen():
    print "!!관리자 모드입니다 ver1.2 !!"
    print "[1.{}: 재고{}개 2.{}: 재고{}개 99.나가기]".format(item1_name, item1_num, item2_name, item2_num)
    print "물품의 재고를 채워넣습니다." 
    adding_item_id = int(raw_input("item id: "))
    return adding_item_id

def shut_down_vending(total_money):
    print "모든 상품이 매진되었습니다."
    print "[거스름돈 {0}원 입니다.]".format(total_money)
    total_money = 0
    
while vending_condition:
    
    #재고 체크
    if item1_num == 0 and item2_num == 0:
        shut_down_vending(total_money)
        break
    else:
        print "자동판매기 [현재금액 {0}원]".format(total_money) 
        # hidden code = 0130
        print "[1.{}: 재고{}개 2.{}: 재고{}개 3.동전넣기 4.동전반환]".format(item1_name, item1_num, item2_name, item2_num)
    
        # 기본적으로 윈도우용 spyder의 console 문제. Pycharm에서 정상작동. 맥에서 정상작동
        # vending_machine_mode = int(raw_input(u"번호를 선택해주세요: ")) # 표기는 문제 없으나 루프에 문제
        # python 3.x
        # print "번호를 선택해주세요:", end =" " 
        # python 2.7.x
        # print "번호를 선택해주세요: ",;
        # python 2.7.x & window & spyder & 제어문상에서의 raw_input
        vending_machine_mode = int(raw_input("select mode: "))
        print "========"
    
        if vending_machine_mode == admin_code:
            admin_condition = True
            while admin_condition:
                # admin mode
                adding_item_id = init_screen()
                
                if adding_item_id == 99:
                    admin_condition = False
                    continue
                else:
                    print "몇 개를 넣으시겠습니까?" 
                    adding_item_ea = int(raw_input("item ea: "))
                    if adding_item_id == 1:
                        if item1_num+adding_item_ea <=10:
                            item1_num += adding_item_ea
                            print "{}을/를 {}개 보충했습니다".format(item1_name, adding_item_ea)
                        else:
                            print "{}은/는 최대재고량에 도달했습니다.".format(item1_name)
                            return_item_ea = adding_item_ea + item1_num -10
                            item1_num = 10
                            print "{}을/를 {}개 반환했습니다".format(item1_name, return_item_ea)
                            
                    elif adding_item_id == 2: 
                        if item2_num+adding_item_ea <=10:
                            item2_num += adding_item_ea
                            print "{}을/를 {}개 보충했습니다".format(item2_name, adding_item_ea)
                        else:
                            print "{}은/는 최대재고량에 도달했습니다.".format(item2_name)
                            return_item_ea = adding_item_ea + item2_num - 10
                            item2_num = 10
                            print "{}을/를 {}개 반환했습니다".format(item2_name, return_item_ea)
                    else:
                        print "잘못입력하셨습니다."
            
        elif vending_machine_mode == 1:
            if item1_num != 0:
                if item1_price <= total_money:
                    print "구매하신 상품 [{}]을/를 확인하세요.".format(item1_name)
                    total_money -= item1_price
                    item1_num -= 1
                else:
                    print "금액이 모자랍니다."
            else:
                print "해당 상품은 매진입니다."
        elif vending_machine_mode == 2:
            if item2_num != 0:
                if item2_price <= total_money:
                    print "구매하신 상품 [{}]을/를 확인하세요.".format(item2_name)
                    total_money -= item2_price
                    item2_num -= 1
                else:
                    print "금액이 모자랍니다."
            else:
                print "해당 상품은 매진입니다."
        elif vending_machine_mode == 3:
            # 물건 판매 - 소비자는 금액을 입력
            inserted_money = int(raw_input("insert coin: "))
            total_money += inserted_money
            print "[투입하신 금액은 {0}원 입니다.]".format(inserted_money)
        
        elif vending_machine_mode == 4:
            # 반환 버튼을 누르면 현재 금액을 반환
            print "[거스름돈 {0}원 입니다.]".format(total_money)
            total_money = 0
        else: 
            # wrong number
            print "== 잘못된 값을 입력하셨습니다 ==" 
else: 
    print u"재고가 소진되어 영업을 종료합니다."
