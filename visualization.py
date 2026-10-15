import matplotlib.pyplot as plt


def show_graph(observations):
    if not observations:
        print("No observations available.")
        return

    targets = [obs.target for obs in observations]
    exposures = [obs.exposure for obs in observations]

    plt.bar(targets, exposures)
    plt.xlabel("Target")
    plt.ylabel("Exposure (seconds)")
    plt.title("Observation Exposure Times")
    plt.show()
