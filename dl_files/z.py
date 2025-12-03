from os import system
from random import randint
from time import time,sleep


def c():
    system('cls')
def w():
    system('pause')
def rd(min_val, max_val):
    return randint(min_val, max_val)
product_dict = {
    '1': {'name': '厦门龙眼干', 'price': 100, 'intr': '厦门生产龙眼干，营养价值高，营养丰富，味道鲜美。','yj':100},
    '2': {'name': '厦门姜母鸭', 'price': 150, 'intr': '厦门生产姜母鸭，营养价值高，十分美味，肉质鲜美。','yj':150},
}
def dashboard():
    begin_time = time()
    while True:
        c()
        print('===AI助力乡村振兴-电商平台===')
        for key, info in product_dict.items():
            print(str(key) + '. '+info['name']+'\n\t'+info['intr']+ '\n\t价格(￥):'+str(info['price']))
        print('===请选择商品(0刷新)===')

        choi = input()
        if choi == '0':
            if time() - begin_time >= 10:
                # 每10秒随机打折
                for key in product_dict.keys():
                    discount = rd(2, 10) / 10
                    product_dict[key]['price'] = int(product_dict[key]['yj'] * discount)
                begin_time = time()
            print('\n\n刷新中',end='')
            sleep(0.5)
            continue

        try:
            choi_num = int(choi)
            if 1 <= choi_num <= len(product_dict):
                choi_key = str(choi_num)
                info = product_dict[choi_key]
                print('\n商品信息')
                print('名称: '+info['name']+'\n价格: '+str(info['price'])+'元\n说明: '+info['intr']+'\n')

                while True:
                    try:
                        buy_num = int(input('购买数量:'))
                        if buy_num <= 0:
                            print('数量必须大于0！')
                            continue
                        break
                    except ValueError:
                        print('请输入有效的数字！')

                total = buy_num * info['price']
                print('\n完成!购买了'+str(buy_num)+'件'+info["name"]+'!')
                print('为乡村振兴建设贡献了'+str(total)+'元！')
                w()
            else:
                print('输入的商品编号不存在！')
                w()
        except ValueError:
            print('请输入有效的数字！')
            w()

if __name__ == '__main__':
    dashboard()