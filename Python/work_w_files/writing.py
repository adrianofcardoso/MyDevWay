#%%
txt = "Esqueci de digitar essas novas informações \n"

name_archive = "history_02.txt"

with open(name_archive, mode="a") as open_file:
    open_file.write(txt)

# %%
