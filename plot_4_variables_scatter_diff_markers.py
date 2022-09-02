import matplotlib.pyplot as plt
import numpy as np
import json



def get_marker_time(frame_id):
    marker = ["1","o","s","<"]
    base = 44
    for i in range(len(marker)):
        v_min = i*base
        v_max = (i+1)*base
        if(frame_id >= v_min and frame_id < v_max):
            m = marker[i]
            label = str(v_min)+'ns - '+str(v_max-1)+'ns'

    return m,label


#
filename = 'alpha_intermol_distance_info_sorted.json'
with open(filename,'r') as f:
    data_alpha = json.load(f)

#'uid', 'frame_id', 'cluster_id', 'population', 'vol_alpha', 'radius_alpha', 'vol_sphere', 'radius_sphere', 'diff_r_sphere_alpha', 'nV0', 'intermol_2CA_distance'

print(data_alpha.keys())

len_list=len(data_alpha['population'])




# Visualization with time --------
z = data_alpha['population']
x = data_alpha['radius_alpha']
y = data_alpha['radius_sphere']

save_name = 'cor_r_alpha_sphere_with_time.png'
frame = data_alpha['frame_id']

#data range
vmin, vmax = min(z), max(z)

# get unique marker
marker_list = []
#plot the two dataset with different markers
for i in range(len_list):
    m ,label = get_marker_time(frame[i])
    if(m in marker_list):
        plt.scatter(x[i], y[i], c = z[i], vmin = vmin, vmax = vmax, cmap = "gist_rainbow",edgecolors='black', marker = m)
    else:
        plt.scatter(x[i], y[i], c = z[i], vmin = vmin, vmax = vmax, cmap = "gist_rainbow", marker = m,edgecolors='black',label=label)
        marker_list.append(m)


plt.legend()
cbar = plt.colorbar()
cbar.set_label('Population of Clusters', fontsize= 15)

plt.xlabel(r'$R_\alpha$',fontsize= 15)
plt.ylabel(r'$R_{sphere}$',fontsize= 15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig(save_name,dpi=300,bbox_inches='tight')
plt.close()
plt.show()





# =================================================================================================

# Visualization with time --------
z = data_alpha['population']
x = data_alpha['vol_alpha']
y = data_alpha['vol_sphere']

save_name = 'cor_Vol_alpha_sphere_with_time.png'
frame = data_alpha['frame_id']

#data range
vmin, vmax = min(z), max(z)

# get unique marker
marker_list = []
#plot the two dataset with different markers
for i in range(len_list):
    m ,label = get_marker_time(frame[i])
    if(m in marker_list):
        plt.scatter(x[i], y[i], c = z[i], vmin = vmin, vmax = vmax, cmap = "gist_rainbow",edgecolors='black', marker = m)
    else:
        plt.scatter(x[i], y[i], c = z[i], vmin = vmin, vmax = vmax, cmap = "gist_rainbow", marker = m,edgecolors='black',label=label)
        marker_list.append(m)


plt.legend()
cbar = plt.colorbar()
cbar.set_label('Population of Clusters', fontsize= 15)

plt.xlabel(r'$V_\alpha$',fontsize= 15)
plt.ylabel(r'$V_{sphere}$',fontsize= 15)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.savefig(save_name,dpi=300,bbox_inches='tight',pad_inches=0)
#plt.close()
plt.show()