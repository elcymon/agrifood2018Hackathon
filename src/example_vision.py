from load_data import *

data = BeetRootData(
    path='./../data/',
    name_stem='beet',
    dataset='Train',
    format='.jpg'
)

print("\n here is beet0.jpg image:")
print(data.get_img(0))

print(".. and here is some stuff with labels:")
for i in range(20):
    state = data.is_good(i)
    position = data.get_pos(i)

    output = "the beetroot in 'beet{}.jpg' is located at ".format(i) + \
             '({},{})'.format(position[0], position[1]) + ", and is "+ \
             ["good" if state == 1 else "bad"][0]

    print(output)


