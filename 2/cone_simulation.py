import argparse
import random
import math

def estimate_cone_volume(n_simulations):
    total_volume = 0

    for _ in range(n_simulations):
        x = random.uniform(-1, 1)  # Valeur aléatoire entre -1 et 1 pour l'axe x
        y = random.uniform(-1, 1)  # Valeur aléatoire entre -1 et 1 pour l'axe y
        z = random.uniform(0, 1)   # Valeur aléatoire entre 0 et 1 pour l'axe z (hauteur du cône)

        # Vérifier si le point (x, y, z) est dans le cône (z <= 1 - abs(x) - abs(y))
        if z <= 1 - abs(x) - abs(y):
            # Calculer le volume du cône pour ce point
            volume = (1/3) * math.pi * (1 - z)**2
            total_volume += volume

    # Estimation du volume du cône
    estimated_volume = total_volume / n_simulations

    # Volume théorique du cône
    theoretical_volume = (1/3) * math.pi

    return estimated_volume, theoretical_volume

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Estimation du volume du cône")
    parser.add_argument("-n", "--nbsimul", type=int, help="Nombre de simulations.")
    args = parser.parse_args()

    if args.nbsimul is None or args.nbsimul <= 0:
        print("Veuillez fournir un entier positif pour le nombre de simulations.")
    else:
        estimated_volume, theoretical_volume = estimate_cone_volume(args.nbsimul)
        print(f"Estimated cone volume: {estimated_volume:.4f}")
        print(f"Theoretical cone volume: {theoretical_volume:.4f}")
