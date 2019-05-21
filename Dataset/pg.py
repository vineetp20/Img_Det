import shutil
for i in range(25):
    shutil.copy2('train/Pepsi/1.jpeg', 'train/Pepsi/1{}.jpeg'.format(i))
    shutil.copy2('train/Pepsi/2.jpeg', 'train/Pepsi/2{}.jpeg'.format(i))
    shutil.copy2('train/Pepsi/3.jpeg', 'train/Pepsi/3{}.jpeg'.format(i))
    shutil.copy2('train/Pepsi/4.png', 'train/Pepsi/4{}.png'.format(i))
