# coding=utf-8
def ppap(item1='pen',item2='apple',item3='pineapple'):

    def song(item1):
        print('I hava a {}'.format(item1))
    def ah(item1, item2):
        print('Ah~ {0} {1}'.format(item2,item1))
    def combine(item1, item2, item3):
        print('{0}~ {1}~ {2}~'.format(item2+' '+item1, item3+' '+item1, item1+' '+item3+' '+item2+' '+item1))

    song(item1) # I have a pen
    song(item2) # I hava an apple
    ah(item1,item2) # Ah~ apple pen
    song(item1) # I have a pen
    song(item3) # I hava a pineapple
    ah(item1,item3) # Ah~ pineapple pen
    combine(item1, item2, item3) # apple pen~ pineapple pen~ pen pineapple apple pen

input_val_1 = input("원하는 과일을 입력해 주세요: ")
input_val_2 = input("원하는 두 번째 과일을 입력해주세요: ")

ppap(item2=input_val_1, item3=input_val_2)


