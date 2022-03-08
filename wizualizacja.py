from matplotlib import pyplot as plt
from matplotlib import image

actions = ['dokumentacja \nprojektowa', 'giben \npodłoga', 'giben \nsufit', 'giben \nściany',  'elcon', 'hundegger \nstropy', 'hundegger \nściany', 'sufit', 'podłoga', 'ściany', 'montaż \nmodułu']

dpi = 72
path = 'hundegger_sufity.png'

im = image.imread(path)
image_size = im.shape[1], im.shape[0]



# serie danych 
ML404X = [1,1,1,1,1,1,1,1,1,1,1]
ML204X = [2,2,2,2,2,2,2,2,2,2,2]
y = [1,2,3,4]

# drukowanko 
plt.scatter(actions, ML404X)
plt.scatter(actions, ML204X)

# nazwy osi
plt.ylabel('moduły')
plt.xlabel('czynności')

# tytuł wykresu
plt.title('Zaawansowanie przygotowania prefabrykatów')

my_yticks = ['ML-404X', 'ML-204X', 'ML-308X', 'ML-203X']
plt.yticks(y, my_yticks)

# legenda
plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig('wykres.png')

plt.show()