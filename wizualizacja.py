from matplotlib import pyplot as plt
from matplotlib import image

actions = ['dokumentacja \nprojektowa', 'giben \npodłoga', 'giben \nsufit', 'giben \nściany',  'elcon', 'hundegger \nstropy', 'hundegger \nściany', 'sufit', 'podłoga', 'ściany', 'montaż \nmodułu']

# serie danych 
ML404X = [1,1,1,1,1,1,1,1,1,1,1]
ML204X = [2,2,2,2,2,2,2,2,2,2,2]
y = [1,2,3,4]

# drukowanko 
ML404X_colors = ['g','g','g','g','r','r','g','r', 'r', 'r', 'r']
ML204X_colors = ['g','g','g','g','r','r','g','r', 'r', 'r', 'r']

plt.scatter(actions, ML404X, color = ML404X_colors, s= 200, marker = 's')
plt.scatter(actions, ML204X, color = ML404X_colors, s= 200, marker = 's')

# nazwy osi
plt.ylabel('moduły')
plt.xlabel('czynności')

# obrócenie nazw
plt.xticks(rotation=90)

# tytuł wykresu
plt.title('Zaawansowanie przygotowania prefabrykatów')

my_yticks = ['ML-404X', 'ML-204X', 'ML-308X', 'ML-203X']
plt.yticks(y, my_yticks)

# legenda
plt.legend()

plt.grid(color = 'k', linewidth = 0.05)

plt.tight_layout()

plt.savefig('wykres.png', dpi=199)

plt.show()