# ============================================================
# SSSP — MÉTODOS PUROS COM VISUALIZAÇÃO E TEMPO
# - Grafo original
# - Bellman–Ford
# - Dijkstra
# - Simulador inspirado no artigo (frontier, sem sorting)
# ============================================================

import networkx as nx
import matplotlib.pyplot as plt
import time


# ============================================================
# 1. GRAFO
# ============================================================

def criar_grafo():
    G = nx.DiGraph()
    edges = [
        # backbone principal
        (0, 1, 4.0),
        (0, 2, 4.0),
        (0, 4, 1.5),
        (0, 6, 2.0),

        # caminhos intermediários
        (1, 2, 1.5),
        (1, 3, 1.0),
        (1, 5, 1.0),

        (2, 3, 1.0),
        (2, 5, 1.2),

        (3, 3, 1.0),
        (3, 5, 0.8),
        (3, 6, 1.0),

        (4, 3, 1.0),
        (4, 6, 4.0),

        (5, 2, 1.0),
        (5, 3, 1.3),

        # ciclos leves
        (3, 1, 1.1),
        (2, 1, 1.4),

        # atalhos quase-ótimos
        (4, 2, 2.6),
        (6, 4, 3.9),
    ]

    G.add_weighted_edges_from(edges)
    return G


# ============================================================
# 2. ALGORITMOS
# ============================================================

def bellman_ford(G, origem):
    return nx.single_source_bellman_ford_path(G, origem)

def dijkstra(G, origem):
    return nx.single_source_dijkstra_path(G, origem)

def bellman_ford_dist(G, origem):
    return nx.single_source_bellman_ford_path_length(G, origem)

def dijkstra_dist(G, origem):
    return nx.single_source_dijkstra_path_length(G, origem)


def sssp_frontier_simulado(G, origem, K=3):
    INF = 1e9
    dist = {v: INF for v in G.nodes}
    pred = {v: None for v in G.nodes}

    dist[origem] = 0.0
    frontier = {origem}

    while frontier:
        nova = set()
        for _ in range(K):
            for u in list(frontier):
                for v in G.successors(u):
                    w = G[u][v]["weight"]
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        pred[v] = u
                        nova.add(v)
        frontier = nova

    # reconstrução dos caminhos
    paths = {}
    for v in G.nodes:
        if dist[v] == INF:
            continue
        caminho = [v]
        atual = v
        while atual != origem:
            atual = pred[atual]
            caminho.append(atual)
        paths[v] = caminho[::-1]

    return dist, paths


# ============================================================
# 3. VISUALIZAÇÃO
# ============================================================

def plot_caminho(ax, G, pos, caminho=None, titulo=""):
    nx.draw(
        G, pos,
        ax=ax,
        with_labels=True,
        node_size=1800,
        node_color="lightgray",
        edge_color="gray",
        arrows=True
    )

    nx.draw_networkx_edge_labels(
        G, pos,
        edge_labels=nx.get_edge_attributes(G, "weight"),
        ax=ax
    )

    if caminho is not None:
        edges_path = list(zip(caminho[:-1], caminho[1:]))
        nx.draw_networkx_edges(
            G, pos,
            edgelist=edges_path,
            edge_color="red",
            width=4,
            ax=ax
        )

    ax.set_title(titulo)


# ============================================================
# 4. EXECUÇÃO
# ============================================================

if __name__ == "__main__":

    origem = 0
    destino = 5

    G = criar_grafo()

    # -------------------------------
    # TEMPO + CAMINHOS
    # -------------------------------

    t0 = time.perf_counter()
    paths_bf = bellman_ford(G, origem)
    t_bf = time.perf_counter() - t0

    t0 = time.perf_counter()
    paths_dij = dijkstra(G, origem)
    t_dij = time.perf_counter() - t0

    t0 = time.perf_counter()
    dist_sim, paths_sim = sssp_frontier_simulado(G, origem)
    t_sim = time.perf_counter() - t0

    caminho_bf = paths_bf[destino]
    caminho_dij = paths_dij[destino]
    caminho_sim = paths_sim[destino]

    # -------------------------------
    # DISTÂNCIAS
    # -------------------------------

    dist_bf = bellman_ford_dist(G, origem)
    dist_dij = dijkstra_dist(G, origem)

    print("\n=== DISTÂNCIAS ===")
    print("Bellman–Ford:", dist_bf)
    print("Dijkstra    :", dist_dij)
    print("Simulador   :", dist_sim)

    print("\n=== CAMINHOS ===")
    print("Bellman–Ford:", caminho_bf)
    print("Dijkstra    :", caminho_dij)
    print("Simulador   :", caminho_sim)

    print("\n=== TEMPO DE EXECUÇÃO (segundos) ===")
    print(f"Bellman–Ford: {t_bf:.6f}")
    print(f"Dijkstra    : {t_dij:.6f}")
    print(f"Simulador   : {t_sim:.6f}")

    # -------------------------------
    # VISUALIZAÇÃO
    # -------------------------------

    pos = nx.spring_layout(G, seed=42)

    fig, axes = plt.subplots(2, 2, figsize=(11, 12))
    axes = axes.flatten()

    plot_caminho(axes[0], G, pos, None, "Grafo original")
    plot_caminho(axes[1], G, pos, caminho_bf, "Bellman–Ford")
    plot_caminho(axes[2], G, pos, caminho_dij, "Dijkstra")
    plot_caminho(axes[3], G, pos, caminho_sim, "Simulador (sem sorting)")

    plt.tight_layout()
    plt.savefig("grafo.png")
    plt.show()
