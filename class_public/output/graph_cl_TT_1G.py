import os

filename = "C:\Users\yacob\Documents\Supaero\Stage\Code\class_modif_1G\CLASS_mod\class_public\output\1G_alpha_fixe_lambda_G_0.500_cl.dat"
os.chmod(filename, 0o644)


if os.access(filename, os.R_OK):
    print("Vous avez la permission de lire le fichier")
else:
    print("Vous n'avez pas la permission de lire le fichier")